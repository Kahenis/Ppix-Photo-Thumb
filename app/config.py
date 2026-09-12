"""Stockage local de la configuration."""

from __future__ import annotations

import json
import os
import uuid
from pathlib import Path
from typing import Any

APP_DIR_NAME = "PPixPhotoThumb"
CONFIG_FILE = "config.json"
QUEUE_FILE = "queue.json"


def app_dir() -> Path:
    base = os.environ.get("APPDATA") or os.environ.get("XDG_CONFIG_HOME")
    if base:
        path = Path(base) / APP_DIR_NAME
    else:
        path = Path.home() / f".{APP_DIR_NAME.lower()}"
    path.mkdir(parents=True, exist_ok=True)
    return path


def default_config() -> dict[str, Any]:
    return {
        "client_identifier": str(uuid.uuid4()),
        "plex_token": "",
        "account_token": "",
        "server_url": "",
        "server_name": "",
        "server_machine_id": "",
        "prefer_local": True,
        "verify_ssl": True,
        "verify_thumbs_http": False,
        "include_videos": True,
        "workers": 2,
        "delay_ms": 200,
        "timeout_sec": 45,
        "retries": 3,
        "transcode_size": 512,
        "cache_warn_mb": 512,
        "auto_resume": True,
        "prevent_sleep": True,
        "theme": "dark",
        "last_section_keys": [],
    }


class Settings:
    def __init__(self) -> None:
        self.path = app_dir() / CONFIG_FILE
        self.data = default_config()
        self.load()

    def load(self) -> None:
        if self.path.exists():
            try:
                raw = json.loads(self.path.read_text(encoding="utf-8"))
                if isinstance(raw, dict):
                    self.data.update(raw)
            except (OSError, json.JSONDecodeError):
                pass
        if not self.data.get("client_identifier"):
            self.data["client_identifier"] = str(uuid.uuid4())
            self.save()

    def save(self) -> None:
        tmp = self.path.with_suffix(".tmp")
        tmp.write_text(json.dumps(self.data, indent=2, ensure_ascii=False), encoding="utf-8")
        tmp.replace(self.path)

    def get(self, key: str, default: Any = None) -> Any:
        return self.data.get(key, default)

    def set(self, key: str, value: Any) -> None:
        self.data[key] = value
        self.save()

    def update(self, values: dict[str, Any]) -> None:
        self.data.update(values)
        self.save()


class QueueStore:
    def __init__(self) -> None:
        self.path = app_dir() / QUEUE_FILE

    def load(self) -> dict[str, Any] | None:
        if not self.path.exists():
            return None
        try:
            data = json.loads(self.path.read_text(encoding="utf-8"))
            return data if isinstance(data, dict) else None
        except (OSError, json.JSONDecodeError):
            return None

    def save(self, payload: dict[str, Any]) -> None:
        tmp = self.path.with_suffix(".tmp")
        tmp.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")
        tmp.replace(self.path)

    def clear(self) -> None:
        if self.path.exists():
            try:
                self.path.unlink()
            except OSError:
                pass
