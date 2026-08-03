from app import mcp

import uuid
import hashlib
import json
import base64
import secrets
import string


@mcp.tool()
def generate_uuid() -> str:
    """
    Generate a random UUID.
    """
    return str(uuid.uuid4())


@mcp.tool()
def sha256_hash(text: str) -> str:
    """
    Generate SHA256 hash of text.
    """
    return hashlib.sha256(text.encode()).hexdigest()


@mcp.tool()
def format_json(text: str) -> str:
    """
    Pretty format JSON.
    """
    data = json.loads(text)
    return json.dumps(data, indent=4)


@mcp.tool()
def base64_encode(text: str) -> str:
    """
    Encode text to Base64.
    """
    return base64.b64encode(text.encode()).decode()


@mcp.tool()
def base64_decode(text: str) -> str:
    """
    Decode Base64 text.
    """
    return base64.b64decode(text.encode()).decode()


@mcp.tool()
def generate_password(length: int = 12) -> str:
    """
    Generate a secure random password.
    """

    alphabet = (
        string.ascii_letters
        + string.digits
        + "!@#$%^&*"
    )

    return "".join(
        secrets.choice(alphabet)
        for _ in range(length)
    )