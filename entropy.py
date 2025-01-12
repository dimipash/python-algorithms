"""
Entropy Calculator

Calculates the Shannon entropy of a probability distribution using the formula:
H = -Σ p(x) * log2(p(x))
where p(x) are the probabilities of each outcome.

Time Complexity: O(n) where n is number of probabilities
Space Complexity: O(1) as it uses vectorized operations
"""


def calculate_entropy(probabilities: np.ndarray) -> float:
    """
    Calculate Shannon entropy of a probability distribution.

    Args:
        probabilities (np.ndarray): Array of probability values that sum to 1

    Returns:
        float: Entropy value in bits

    Raises:
        ValueError: If probabilities don't sum to 1 or contain negative values
    """
    if not np.isclose(np.sum(probabilities), 1.0):
        raise ValueError("Probabilities must sum to 1")
    if np.any(probabilities < 0):
        raise ValueError("Probabilities cannot be negative")

    # Filter out zero probabilities to avoid log(0)
    probabilities = probabilities[probabilities > 0]

    # Calculate entropy using vectorized operations
    return -np.sum(probabilities * np.log2(probabilities))


def main() -> None:
    """
    Demonstrate entropy calculation with example distributions.
    """
    # Test cases
    distributions = [
        np.array([0.5, 0.5]),  # Fair coin
        np.array([0.7, 0.3]),  # Biased coin
        np.array([1.0, 0.0]),  # Certain outcome
        np.array([0.25, 0.25, 0.25, 0.25]),  # Fair die
    ]

    for prob in distributions:
        entropy = calculate_entropy(prob)
        print(f"Entropy: {entropy:.4f} bits")


if __name__ == "__main__":
    main()
