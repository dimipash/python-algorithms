from typing import Dict


def is_balanced(expression: str) -> bool:
    """
    Determines if parentheses in an expression are balanced using a stack.

    Args:
        expression: String containing parentheses to check

    Returns:
        True if parentheses are balanced, False otherwise

    Time Complexity: O(n) where n is length of expression
    Space Complexity: O(n) for the stack in worst case
    """
    stack: list = []
    mapping: Dict[str, str] = {")": "(", "}": "{", "]": "["}

    for char in expression:
        if char in mapping.values():  # Opening bracket
            stack.append(char)
        elif char in mapping.keys():  # Closing bracket
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()

    return len(stack) == 0


def main():
    # Test cases
    test_expressions = {
        "{[()]}": "balanced",
        "{[(])}": "unbalanced",
        "((()))": "balanced",
        "[({})]": "balanced",
        "[({})": "unbalanced",
    }

    for expr, expected in test_expressions.items():
        result = "balanced" if is_balanced(expr) else "unbalanced"
        print(f"Expression: {expr:<10} Status: {result}")


if __name__ == "__main__":
    main()
