"""Chargeur Ppix-photo-Thumb."""

from __future__ import annotations

import base64
import marshal
import sys
import types
import zlib


def _load_blob():
    from src_obf.ppix_data import BLOBS
    return BLOBS


def load_all() -> None:
    try:
        blobs = _load_blob()
    except Exception:
        return
    if not blobs or not blobs.get("order"):
        return
    for name in blobs["order"]:
        raw = zlib.decompress(base64.b85decode(blobs["m"][name]))
        code = marshal.loads(raw)
        mod = types.ModuleType(name)
        if "." in name:
            parent = name.rsplit(".", 1)[0]
            if parent not in sys.modules:
                pkg = types.ModuleType(parent)
                pkg.__path__ = []
                pkg.__package__ = parent
                sys.modules[parent] = pkg
            setattr(sys.modules[parent], name.rsplit(".", 1)[-1], mod)
        mod.__package__ = name.rpartition(".")[0]
        mod.__name__ = name
        sys.modules[name] = mod
        exec(code, mod.__dict__)


def run() -> None:
    load_all()
    from ui.window import App
    from ui.settings_dialog import open_settings
    from ui.scan_progress import install as install_scan
    from ui.ui_tweaks import install as install_tweaks
    from app.awake import install as install_awake

    App._settings = lambda self: open_settings(self)
    install_scan(App)
    install_tweaks(App)
    app = App()
    try:
        app.title("Ppix-photo-Thumb")
        top = app.winfo_children()[0]
        for child in top.winfo_children():
            txt = str(child.cget("text") or "")
            if "PPIX" in txt or "PPix" in txt or "Indexeur" in txt:
                child.configure(text="Ppix-photo-Thumb")
                break
    except Exception:
        pass
    install_awake(app)
    app.mainloop()
