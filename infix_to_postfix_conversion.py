def infix_to_postfix(expression):
    """
    Converts an infix expression to postfix (Reverse Polish) notation using the Shunting Yard algorithm.

    Parameters:
    expression (str): The infix expression string with space-separated tokens.

    Returns:
    str: The postfix expression as a string with space-separated tokens.

    Time Complexity: O(n), where n is the number of tokens in the expression.
    Space Complexity: O(n), due to the stack and output list used during conversion.
    """
    # Define operator precedence and associativity
    # Precedence: higher value means higher precedence
    # Associativity: 'L' for left, 'R' for right
    precedence = {
        "+": (1, "L"),
        "-": (1, "L"),
        "*": (2, "L"),
        "/": (2, "L"),
        "^": (3, "R"),
    }

    output = []  # List to hold the postfix expression
    stack = []  # Stack to hold operators

    tokens = expression.split()  # Split the expression into tokens

    for token in tokens:
        if token.isalnum():  # If the token is an operand (alphabetical or numerical)
            output.append(token)
        elif token in precedence:  # If the token is an operator
            # Pop operators from the stack to the output list based on precedence and associativity
            assoc, prec = precedence[token]
            while (
                stack
                and stack[-1] != "("
                and precedence.get(stack[-1], (0, "L"))[0] >= prec
            ):
                if precedence[stack[-1]][1] == "R" and precedence[stack[-1]][0] == prec:
                    break
                output.append(stack.pop())
            stack.append(token)
        elif token == "(":  # If the token is a left parenthesis
            stack.append(token)
        elif token == ")":  # If the token is a right parenthesis
            # Pop operators from the stack to the output list until a left parenthesis is found
            while stack and stack[-1] != "(":
                output.append(stack.pop())
            if stack and stack[-1] == "(":
                stack.pop()  # Remove the left parenthesis from the stack
            else:
                raise ValueError("Unmatched right parenthesis")
        else:
            raise ValueError(f"Invalid token: {token}")

    # Pop any remaining operators from the stack to the output list
    while stack:
        if stack[-1] == "(":
            raise ValueError("Unmatched left parenthesis")
        output.append(stack.pop())

    return " ".join(output)
