"""Empêche la mise en veille Windows pendant un travail long."""

from __future__ import annotations

import sys

ES_CONTINUOUS = 0x80000000
ES_SYSTEM_REQUIRED = 0x00000001
ES_DISPLAY_REQUIRED = 0x00000002


def _call(flags: int) -> None:
    if sys.platform != "win32":
        return
    try:
        import ctypes

        ctypes.windll.kernel32.SetThreadExecutionState(flags)
    except Exception:
        pass


def stay_awake() -> None:
    _call(ES_CONTINUOUS | ES_SYSTEM_REQUIRED | ES_DISPLAY_REQUIRED)


def allow_sleep() -> None:
    _call(ES_CONTINUOUS)


def install(app) -> None:
    def pulse() -> None:
        working = bool(getattr(app, "_scanning", False) or getattr(app, "_generating", False))
        enabled = bool(app.settings.get("prevent_sleep", True))
        if working and enabled and not (
            hasattr(app, "_gen_ctrl") and app._generating and app._gen_ctrl.is_paused()
        ):
            stay_awake()
        else:
            allow_sleep()
        try:
            app.after(20000, pulse)
        except Exception:
            allow_sleep()

    orig_close = app._close

    def close() -> None:
        allow_sleep()
        orig_close()

    app._close = close
    app.after(1000, pulse)
