## Auto-formatting Tool

A decorator-based utility that standardizes Python functions for AI agent consumption.

### Features

- **Type Introspection**: Extracts and formats type hints from function signatures
- **Documentation Generation**: Standardizes documentation for agent understanding
- **Tool Wrapping**: Transforms Python functions into agent-compatible tools
- **Self-describing Functions**: Enables runtime inspection of tool capabilities

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
