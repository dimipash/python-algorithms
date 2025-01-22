def evaluate_prefix(expression):
    """
    Evaluates a prefix (Polish) notation expression.

    Time Complexity: O(n), where n is the number of tokens in the expression.
    Space Complexity: O(n), due to the stack and token list.

    Parameters:
    expression (str): The prefix expression string with space-separated tokens.

    Returns:
    int or float: The result of the expression evaluation.

    Raises:
    ValueError: If there are insufficient operands for an operator or invalid tokens.
    ZeroDivisionError: If division by zero is attempted.
    """
    stack = []
    tokens = expression.split()
    tokens = tokens[::-1]  # Reverse for right-to-left processing

    for token in tokens:
        try:
            # Attempt to convert the token to a float (handles integers and floats)
            number = float(token)
            stack.append(number)
        except ValueError:
            # If not a number, it must be an operator; check for sufficient operands
            if len(stack) < 2:
                raise ValueError("Insufficient operands for operator.")
            b = stack.pop()
            a = stack.pop()
            if token == "+":
                result = a + b
            elif token == "-":
                result = a - b
            elif token == "*":
                result = a * b
            elif token == "/":
                if b == 0:
                    raise ZeroDivisionError("Division by zero is not allowed.")
                result = a / b
            else:
                raise ValueError(f"Invalid operator: {token}")
            # Push the result back onto the stack
            if isinstance(result, float) and result.is_integer():
                stack.append(int(result))
            else:
                stack.append(result)

    if len(stack) != 1:
        raise ValueError("Invalid expression: too many operands.")

    return stack[0]


# Example usage
if __name__ == "__main__":
    # Test Case 1
    prefix_expr = "* + 2 3 4"
    print(evaluate_prefix(prefix_expr))  # Output: 20

    # Test Case 2
    prefix_expr = "+ 2 3"
    print(evaluate_prefix(prefix_expr))  # Output: 5

    # Test Case 3
    prefix_expr = "- 5 2"
    print(evaluate_prefix(prefix_expr))  # Output: 3

    # Test Case 4
    prefix_expr = "/ 10 2"
    print(evaluate_prefix(prefix_expr))  # Output: 5

    # Test Case 5
    prefix_expr = "+ -2 3"
    print(evaluate_prefix(prefix_expr))  # Output: 1

    # Test Case 6
    prefix_expr = "+ 2"
    try:
        print(evaluate_prefix(prefix_expr))
    except ValueError as e:
        print(e)  # Output: Insufficient operands for operator.

    # Test Case 7
    prefix_expr = "/ 5 0"
    try:
        print(evaluate_prefix(prefix_expr))
    except ZeroDivisionError as e:
        print(e)  # Output: Division by zero is not allowed.

    # Test Case 8
    prefix_expr = "+ a 3"
    try:
        print(evaluate_prefix(prefix_expr))
    except ValueError as e:
        print(e)  # Output: Invalid operator: a
