"""
Extended Euclidean Algorithm

Finds GCD of two numbers and coefficients of Bézout's identity:
ax + by = gcd(a,b)
Returns (gcd, x, y) where gcd is the greatest common divisor and
x, y are coefficients of the linear combination.

Time Complexity: O(log min(a,b)) 
Space Complexity: O(log min(a,b)) for recursion stack
"""


def extended_gcd(a: int, b: int) -> tuple:
    """
    Calculate GCD and coefficients of Bézout's identity.

    Args:
        a (int): First integer
        b (int): Second integer

    Returns:
        tuple: (gcd, x, y) where ax + by = gcd

    Examples:
        >>> extended_gcd(30, 21)
        (3, -2, 3)
        >>> extended_gcd(35, 15)
        (5, 1, -2)
    """
    if a == 0:
        return b, 0, 1

    # Recursive call
    gcd, x1, y1 = extended_gcd(b % a, a)

    # Update coefficients
    x = y1 - (b // a) * x1
    y = x1

    return gcd, x, y


def main() -> None:
    """
    Demonstrate extended GCD algorithm with examples.
    """
    test_cases = [
        (30, 21),  # GCD = 3
        (35, 15),  # GCD = 5
        (48, 18),  # GCD = 6
        (17, 13),  # Coprime numbers
    ]

    for a, b in test_cases:
        gcd, x, y = extended_gcd(a, b)
        print(f"GCD({a}, {b}) = {gcd}")
        print(f"{a}({x}) + {b}({y}) = {gcd}")
        print(f"Verification: {a*x + b*y == gcd}\n")


if __name__ == "__main__":
    main()
