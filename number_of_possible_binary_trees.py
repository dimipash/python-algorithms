def factorial(n):
    """
    Computes the factorial of a given number n.

    :param n: The integer for which to compute the factorial.
    :return: The factorial of n.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def catalan_number(n):
    """
    Computes the nth Catalan number, which represents the number of distinct
    binary trees that can be formed with n distinct nodes.

    The nth Catalan number is given by the formula:
    C(n) = (2n)! / ((n + 1)! * n!)

    :param n: The number of nodes.
    :return: The nth Catalan number.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    return factorial(2 * n) // (factorial(n + 1) * factorial(n))


# Example usage:
if __name__ == "__main__":
    n = 3
    print(f"Number of possible binary trees with {n} nodes: {catalan_number(n)}")
    # Output: Number of possible binary trees with 3 nodes: 5
