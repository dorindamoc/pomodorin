import json
from pathlib import Path

from .model import AppSettings

SETTINGS_PATH = Path.home() / ".pomodorin" / "settings.json"


def load_settings() -> AppSettings:
    if not SETTINGS_PATH.exists():
        return AppSettings()

    with SETTINGS_PATH.open("r", encoding="utf-8") as f:
        data = json.load(f)

    return AppSettings(**data)


def save_settings(settings: AppSettings) -> None:
    SETTINGS_PATH.parent.mkdir(parents=True, exist_ok=True)
    with SETTINGS_PATH.open("w", encoding="utf-8") as f:
        json.dump(settings.model_dump(), f, indent=4)
