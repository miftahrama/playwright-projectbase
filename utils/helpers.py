"""
Common utility helpers for test automation.
"""
import os
import json
from datetime import datetime


def get_timestamp() -> str:
    """Get current timestamp string."""
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def load_json_file(file_path: str) -> dict:
    """Load and parse a JSON file."""
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json_file(file_path: str, data: dict) -> None:
    """Save data to a JSON file."""
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def ensure_dir(directory: str) -> str:
    """Ensure directory exists, create if not."""
    os.makedirs(directory, exist_ok=True)
    return directory


def get_project_root() -> str:
    """Get project root directory."""
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_test_data_path(filename: str) -> str:
    """Get full path to test data file."""
    return os.path.join(get_project_root(), "test-data", filename)