"""Utilities to fetch and load the small text datasets used across chapters."""

from pathlib import Path
from urllib.request import urlretrieve

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "data"


def download_text_file(url: str, dest: Path) -> Path:
    """Download `url` to `dest` unless `dest` already exists locally."""
    dest = Path(dest)
    if not dest.exists():
        dest.parent.mkdir(parents=True, exist_ok=True)
        urlretrieve(url, dest)
    return dest


def read_text(name: str, data_dir: Path = DATA_DIR) -> str:
    """Read a UTF-8 text file from the data directory, independent of the working directory."""
    return (Path(data_dir) / name).read_text(encoding="utf-8")
