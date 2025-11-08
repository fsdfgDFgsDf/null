# updater.py
# --------------------------------------------------------------
# 1. CONFIG – edit only these three lines
# --------------------------------------------------------------
REPO_RAW_ROOT = "https://raw.githubusercontent.com/fsdfgDFgsDf/null/main"
# ^^^ example: https://raw.githubusercontent.com/torvalds/linux/master

LOCAL_ROOT = "."                     # folder where files live (relative to script)
BRANCH     = "main"                  # change if you use master, dev, etc.

# --------------------------------------------------------------
# 2. IMPLEMENTATION – no changes needed below
# --------------------------------------------------------------
import sys
import os
import hashlib
import urllib.request
from pathlib import Path
from urllib.error import HTTPError, URLError

# Build the exact URL for a relative path
def raw_url(rel_path: str) -> str:
    return f"{REPO_RAW_ROOT.rstrip('/')}/{rel_path.lstrip('/')}"

# SHA-256 of a file (or empty string if missing)
def file_hash(path: Path) -> str:
    if not path.exists():
        return ""
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

# Download a single file
def download_file(rel_path: str) -> bytes:
    url = raw_url(rel_path)
    try:
        with urllib.request.urlopen(url) as resp:
            return resp.read()
    except HTTPError as e:
        print(f"[ERROR] {e.code} {url}")
        sys.exit(2)
    except URLError as e:
        print(f"[ERROR] Network error: {e}")
        sys.exit(2)

# ------------------------------------------------------------------
def main():
    local_root = Path(LOCAL_ROOT).resolve()
    updated = False

    # Walk the *local* tree – we only update files that already exist locally
    for local_path in local_root.rglob("*"):
        if local_path.is_dir():
            continue

        rel = local_path.relative_to(local_root).as_posix()
        remote_data = download_file(rel)
        remote_hash = hashlib.sha256(remote_data).hexdigest()
        local_hash  = file_hash(local_path)

        if remote_hash != local_hash:
            # Write new content
            local_path.parent.mkdir(parents=True, exist_ok=True)
            local_path.write_bytes(remote_data)
            print(f"[UPDATED] {rel}")
            updated = True
        else:
            print(f"[UNCHANGED] {rel}")

    sys.exit(1 if updated else 0)

if __name__ == "__main__":
    main()