#!/usr/bin/env python3
"""PPix Photo-thumb — application Windows."""

from __future__ import annotations

import os
import sys


def _prepare_path() -> None:
    if getattr(sys, "frozen", False):
        base = getattr(sys, "_MEIPASS", os.path.dirname(sys.executable))
    else:
        base = os.path.dirname(os.path.abspath(__file__))
    if base not in sys.path:
        sys.path.insert(0, base)
    os.chdir(base if os.path.isdir(base) else os.path.dirname(base))


def main() -> None:
    _prepare_path()
    from ppix_boot import run

    run()


if __name__ == "__main__":
    main()
