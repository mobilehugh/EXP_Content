#!/usr/bin/env python3
"""Run the shared EXP repository sync tool from this checkout."""

import os
from pathlib import Path
import sys

script = Path(__file__).resolve().parent.parent / "EXP_Web" / "sync_repos.py"
os.execv(sys.executable, [sys.executable, str(script), *sys.argv[1:]])
