from typing import Optional
import re
from flask.wrappers import Request


def validate_int(req: Request, field: str, *, default: int = 0, required: bool = False) -> int:
    """Validate an integer, returns the integer if valid, otherwise the default.

    Raises ValueError if the field is required and the valid is not valid.
    """
    value = req.args.get(field, "")
    if value == "" and required:
        raise ValueError(f"Required parameter '{field}' is missing")
    try:
        return int(value)
    except ValueError:
        if required:
            raise ValueError(f"{field} expects an integer but got '{value}'")
        return default


def validate_color(
    req: Request, field: str, *, default: str = "#ffffff", required: bool = False
) -> str:
    """Validate a color, returns the color if valid hex code (3, 4, 6, or 8 characters), otherwise the default.

    Raises ValueError if the field is required and the valid is not valid.
    """
    value = req.args.get(field, "")
    if value == "" and required:
        raise ValueError(f"Required parameter '{field}' is missing")
    hex_digits = re.sub(r"[^a-fA-F0-9]", "", value)
    if len(hex_digits) not in (3, 4, 6, 8):
        if required:
            raise ValueError(f"{field} expects a hex color but got '{value}'")
        return default
    return f"#{hex_digits}"


def validate_video_id(
    req: Request, field: str, *, default: str = "", required: bool = False
) -> str:
    """Validate a video ID, returns the video ID if valid, otherwise the default.

    Raises ValueError if the field is required and the valid is not valid.
    """
    value = req.args.get(field, "")
    if value == "" and required:
        raise ValueError(f"Required parameter '{field}' is missing")
    if not re.match(r"^[a-zA-Z0-9_-]+$", value):
        if required:
            raise ValueError(f"{field} expects a video ID but got '{value}'")
        return default
    return value


def validate_string(req: Request, field: str, *, required: bool = False) -> str:
    """Validate a string, returns the string if valid, otherwise the default.

    Raises ValueError if the field is required and the valid is not valid.
    """
    value = req.args.get(field, "")
    if value == "" and required:
        raise ValueError(f"Required parameter '{field}' is missing")
    return value
