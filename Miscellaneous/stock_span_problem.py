def calculate_span(prices):
    n = len(prices)
    span = [0] * n  # Initialize span list with zeros
    stack = []  # Initialize an empty stack

    for i in range(n):
        # Pop elements from the stack while the top element is less than or equal to current price
        while stack and prices[stack[-1]] <= prices[i]:
            stack.pop()

        # Calculate span
        if not stack:
            span[i] = i + 1  # Include current day
        else:
            span[i] = i - stack[-1]

        # Push current index onto stack
        stack.append(i)

    # Time Complexity: O(n), where n is the number of days
    # Each element is pushed and popped from the stack at most once.
    # Space Complexity: O(n), due to the stack and span list.
    return span


# Example usage
if __name__ == "__main__":
    # Test Case 1
    stock_prices = [100, 80, 60, 70, 60, 75, 85]
    print(calculate_span(stock_prices))  # Output: [1, 1, 1, 2, 1, 4, 6]

    # Test Case 2
    stock_prices = [10, 20, 30, 25, 35]
    print(calculate_span(stock_prices))  # Output: [1, 2, 3, 1, 5]

    # Test Case 3
    stock_prices = [7, 7, 7, 7]
    print(calculate_span(stock_prices))  # Output: [1, 2, 3, 4]

    # Test Case 4
    stock_prices = [1]
    print(calculate_span(stock_prices))  # Output: [1]

    # Test Case 5
    stock_prices = []
    print(calculate_span(stock_prices))  # Output: []

    # Test Case 6
    stock_prices = [1, 2, 3, 4, 5]
    print(calculate_span(stock_prices))  # Output: [1, 2, 3, 4, 5]

    # Test Case 7
    stock_prices = [5, 4, 3, 2, 1]
    print(calculate_span(stock_prices))  # Output: [1, 1, 1, 1, 1]
