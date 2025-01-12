"""
Binary Multiplication Algorithm

Multiplies two binary numbers represented as strings. The algorithm converts 
binary strings to integers, performs multiplication, and converts back to binary.

Time Complexity: O(n) where n is the length of the binary numbers
Space Complexity: O(1) as only fixed variables are used
"""


def binary_multiplication(bin1: str, bin2: str) -> str:
    """
    Multiply two binary numbers represented as strings.

    Args:
        bin1 (str): First binary number as string
        bin2 (str): Second binary number as string

    Returns:
        str: Product of the two numbers in binary

    Raises:
        ValueError: If inputs are not valid binary strings

    Examples:
        >>> binary_multiplication('1011', '110')
        '1000110'
    """
    if not (set(bin1) <= {"0", "1"} and set(bin2) <= {"0", "1"}):
        raise ValueError("Inputs must be valid binary strings")

    # Convert binary strings to integers
    num1 = int(bin1, 2)
    num2 = int(bin2, 2)

    # Perform multiplication
    product = num1 * num2

    # Convert result back to binary, removing '0b' prefix
    return bin(product)[2:]


def main() -> None:
    """
    Demonstrate binary multiplication with sample cases.
    """
    test_cases = [
        ("1011", "110"),  # 11 * 6
        ("1010", "101"),  # 10 * 5
        ("1101", "100"),  # 13 * 4
        ("1", "1"),  # 1 * 1
        ("0", "1010"),  # 0 * 10
    ]

    for bin1, bin2 in test_cases:
        result = binary_multiplication(bin1, bin2)
        print(f"{bin1} * {bin2} = {result}")


if __name__ == "__main__":
    main()
