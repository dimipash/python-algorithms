"""
Binomial Distribution Calculator

Provides functions to calculate binomial probabilities and generate 
random samples from a binomial distribution. The binomial distribution
models the number of successes in n independent trials.

Formula: P(X = k) = C(n,k) * p^k * (1-p)^(n-k)
where:
- n is number of trials
- k is number of successes
- p is probability of success per trial

Time Complexity: O(n) for probability calculation
Space Complexity: O(1) for probability, O(size) for random generation
"""

from math import comb
import numpy as np
import matplotlib.pyplot as plt


def binomial_probability(n: int, k: int, p: float) -> float:
    """
    Calculate probability mass function for binomial distribution.

    Args:
        n (int): Number of trials
        k (int): Number of successes
        p (float): Probability of success on each trial

    Returns:
        float: Probability of exactly k successes in n trials

    Raises:
        ValueError: If p not in [0,1] or k > n
    """
    if not 0 <= p <= 1:
        raise ValueError("Probability p must be between 0 and 1")
    if k > n:
        raise ValueError("Number of successes cannot exceed number of trials")

    return comb(n, k) * (p**k) * ((1 - p) ** (n - k))


def plot_binomial_distribution(n: int, p: float, size: int = 1000) -> None:
    """
    Generate and plot random samples from binomial distribution.

    Args:
        n (int): Number of trials
        p (float): Probability of success
        size (int): Number of random samples to generate
    """
    # Generate random variables
    random_variables = np.random.binomial(n, p, size)

    # Create histogram
    plt.figure(figsize=(8, 6))
    plt.hist(
        random_variables,
        bins=range(n + 2),
        density=True,
        alpha=0.7,
        color="blue",
        edgecolor="black",
    )

    # Customize plot
    plt.title(f"Binomial Distribution (n={n}, p={p})")
    plt.xlabel("Number of Successes")
    plt.ylabel("Probability")
    plt.xticks(range(n + 1))
    plt.grid(True)
    plt.show()


def main() -> None:
    """
    Demonstrate binomial distribution calculations and visualization.
    """
    # Parameters
    n, p = 10, 0.5

    # Calculate probabilities for k=0 to n
    for k in range(n + 1):
        prob = binomial_probability(n, k, p)
        print(f"P(X = {k}) = {prob:.4f}")

    # Plot distribution
    plot_binomial_distribution(n, p)


if __name__ == "__main__":
    main()
