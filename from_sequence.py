def fibonacci(n):
    """
    Generate a Fibonacci sequence of length n.

    The Fibonacci sequence is defined as follows:
    - The first two numbers are 0 and 1.
    - Each subsequent number is the sum of the two preceding ones.

    Args:
        n (int): The number of Fibonacci numbers to generate.

    Returns:
        list: A list containing the first n Fibonacci numbers.

    Time Complexity: O(n)
        We perform a single loop that iterates n-2 times.

    Space Complexity: O(n)
        We store n Fibonacci numbers in the sequence list.

    Example:
        >>> fibonacci(10)
        [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]

    # Initialize the sequence with the first two Fibonacci numbers
    seq = [0, 1]

    # Generate subsequent Fibonacci numbers
    for _ in range(2, n):
        # Append the sum of the last two numbers
        seq.append(seq[-1] + seq[-2])

    return seq


# Example usage
if __name__ == "__main__":
    # Generate the first 10 Fibonacci numbers
    result = fibonacci(10)
    print(f"First 10 Fibonacci numbers: {result}")

    # Generate the first 15 Fibonacci numbers
    result = fibonacci(15)
    print(f"First 15 Fibonacci numbers: {result}")
