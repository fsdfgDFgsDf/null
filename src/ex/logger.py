from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
LOG_DIR  = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)

LOGFILE = LOG_DIR / f"{datetime.now():%d - %m}.log"

def _now(): 
    return datetime.now().strftime("%H:%M:%S")

def log(lvl: str, code: str, msg: str) -> None:
    """Append [ LVL: CODE ] MSG to daily log file."""
    with LOGFILE.open("a", encoding="utf-8", buffering=1) as f:  # line buffering

        f.write(f"[ {lvl}: {code} ] {msg}\n")

# Update checking, if this file updates locally, then the updater.py works!
