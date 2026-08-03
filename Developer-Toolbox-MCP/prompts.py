from app import mcp


@mcp.prompt()
def explain_tool(tool_name: str):

    return f"""
Explain how the tool '{tool_name}' works.

Include:

• Purpose

• Example

• Real-world use case
"""


@mcp.prompt()
def generate_documentation(tool_name: str):

    return f"""
Generate professional documentation for

{tool_name}
"""


@mcp.prompt()
def suggest_use_cases(tool_name: str):

    return f"""
Suggest five practical use cases for

{tool_name}
"""