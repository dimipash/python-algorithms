def evaluate_postfix(expression):
    """
    Evaluates a postfix (Reverse Polish Notation) expression and returns the result.

    Parameters:
    expression (str): The postfix expression string with space-separated tokens.

    Returns:
    int or float: The result of the postfix expression evaluation.

    Time Complexity: O(n), where n is the number of tokens in the expression.
    Space Complexity: O(n), due to the stack used for storing operands.
    """
    stack = []
    for token in expression.split():
        try:
            # Attempt to convert the token to a float (handles both integers and floats)
            number = float(token)
            stack.append(number)
        except ValueError:
            # If not a number, it must be an operator; pop the top two operands
            if len(stack) < 2:
                raise ValueError("Insufficient operands for operator.")
            b = stack.pop()
            a = stack.pop()
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                if b == 0:
                    raise ZeroDivisionError("Division by zero is not allowed.")
                stack.append(a / b)
            else:
                raise ValueError(f"Invalid operator: {token}")
    # Check if there is exactly one result in the stack
    if len(stack) != 1:
        raise ValueError("Invalid expression: too many operands.")
    result = stack[0]
    # Convert to int if the result is a whole number
    if isinstance(result, float) and result.is_integer():
        return int(result)
    else:
        return result


# Example usage
if __name__ == "__main__":
    postfix_expr = "5 1 2 + 4 * + 3 -"
    print(evaluate_postfix(postfix_expr))  # Output: 14

    # Additional test cases
    print(evaluate_postfix("2 3 +"))  # Output: 5
    print(evaluate_postfix("1 2 * 3 +"))  # Output: 5
    print(evaluate_postfix("3 5 -"))  # Output: -2
    print(evaluate_postfix("2.5 3.5 +"))  # Output: 6.0
    print(evaluate_postfix("4.0 2.0 /"))  # Output: 2.0
    # Error-prone test cases
    # print(evaluate_postfix("4 0 /"))       # Raises ZeroDivisionError
    # print(evaluate_postfix("1 2 + 3"))     # Raises ValueError for too many operands
    # print(evaluate_postfix("a b +"))       # Raises ValueError for invalid tokens
