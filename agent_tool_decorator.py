from typing import Union
import inspect
from typing import get_type_hints, Callable

def tool(func: Callable):
    func_name = func.__name__
    doc = func.__doc__.strip() if func.__doc__ else "No description."

    # Get function signature and type hints
    sig = inspect.signature(func)
    type_hints = get_type_hints(func)

    # Format input arguments
    inputs = []
    for param_name, param in sig.parameters.items():
        hint = type_hints.get(param_name, 'Any')
        inputs.append(f"{param_name}: {hint.__name__ if hasattr(hint, '__name__') else str(hint)}")
    
    # Format output type
    return_type = type_hints.get('return', 'Any')
    output_type = return_type.__name__ if hasattr(return_type, '__name__') else str(return_type)

    # Attach metadata to the function
    def to_string():
        return (f"Tool Name: {func_name}, Description: {doc}, "
                f"Arguments: {', '.join(inputs)}, Outputs: {output_type}")
    
    func.to_string = to_string
    return func

@tool
def calculator(a: int, b: int, operator: str) -> Union[int, str]:
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

print(calculator.to_string())

#The output is:
# (venv) zeyad@zeyads-MacBook-Pro Ai-Agent % python agent_tool_decorator.py
# Tool Name: calculator, Description: Calculates the sum, difference, product, or quotient of two numbers.
# Args:
#     a (int): The first number.
#     b (int): The second number.
#     operator (str): The operation to perform. Valid options are "sum", "difference", "product", and "quotient"
# Returns:
#     int: The result of the calculation, Arguments: a: int, b: int, operator: str, Outputs: int

# https://huggingface.co/learn/agents-course/unit1/tools#auto-formatting-tool-sections
# The description is injected in the system prompt.