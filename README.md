<<<<<<< HEAD
# agent_tool_decorator
=======
# AI-Powered Code Tools

A collection of utilities for equipping and enhancing AI agents with standardized interfaces and capabilities.

## Auto-formatting Tool

A decorator-based utility that standardizes Python functions for AI agent consumption.

## Get Started

 - python -m venv venv
 - source venv/bin/activate
 - python auto_formatting_tool.py

### Features

- **Type Introspection**: Extracts and formats type hints from function signatures
- **Documentation Generation**: Standardizes documentation for agent understanding
- **Tool Wrapping**: Transforms Python functions into agent-compatible tools
- **Self-describing Functions**: Enables runtime inspection of tool capabilities

### Example Usage

```python
from auto_formatting_tool import tool

@tool
def calculator(a: int, b: int, operator: str) -> int:
    """
    Calculates the sum, difference, product, or quotient of two numbers.
    Args:
        a (int): The first number.
        b (int): The second number.
        operator (str): The operation to perform. Valid options are "sum", "difference", "product", and "quotient"
    Returns:
        int: The result of the calculation
    """
    if operator == "sum":
        return a + b
    elif operator == "difference":
        return a - b
    elif operator == "product":
        return a * b
    elif operator == "quotient":
        return a / b
    else:
        return "Invalid operator"

# Access the tool's metadata
print(calculator.to_string())
```

## Technical Implementation

Built with Python's inspect and typing modules to:

- Extract function signatures and type hints
- Format documentation consistently
- Add metadata methods to decorated functions
- Preserve original functionality while enhancing with metadata

## Use Cases

- Equip AI agents with standardized tool interfaces
- Create self-documenting function libraries for LLMs
- Build consistent API surfaces for agent interaction
- Enable runtime discovery of tool capabilitie
>>>>>>> 0e99e6c (Initial public release: AI agent tool decorator)
