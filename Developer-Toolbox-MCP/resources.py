from app import mcp


@mcp.resource("toolbox://version")
def version():

    return "1.0.0"


@mcp.resource("toolbox://info")
def info():

    return """
Developer Toolbox MCP

Available Tools

• generate_uuid
• sha256_hash
• format_json
• base64_encode
• base64_decode
• generate_password
"""


@mcp.resource("toolbox://help")
def help_resource():

    return """
Developer Toolbox MCP Help

Use the available tools to generate UUIDs,
hash text,
format JSON,
encode/decode Base64,
and generate secure passwords.
"""