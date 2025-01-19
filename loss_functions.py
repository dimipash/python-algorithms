from typing import Union, Optional
import numpy as np


class LossFunctions:
    """
    Implementation of common loss functions for machine learning.

    Time Complexity: O(n) for all loss calculations
    Space Complexity: O(1) for all loss calculations

    Example:
        >>> loss = LossFunctions()
        >>> y_true = np.array([1, 0, 1, 1])
        >>> y_pred = np.array([0.9, 0.1, 0.8, 0.6])
        >>> bce_loss = loss.binary_cross_entropy(y_true, y_pred)
    """

    def __init__(self, epsilon: float = 1e-15):
        """
        Args:
            epsilon: Small constant to avoid log(0)
        """
        self.epsilon = epsilon

    def mean_squared_error(self, y_true: np.ndarray, y_pred: np.ndarray) -> float:
        """
        Calculate Mean Squared Error loss.

        MSE = (1/n) * Σ(y_true - y_pred)²
        """
        return np.mean((y_true - y_pred) ** 2)

    def root_mean_squared_error(self, y_true: np.ndarray, y_pred: np.ndarray) -> float:
        """
        Calculate Root Mean Squared Error loss.

        RMSE = √((1/n) * Σ(y_true - y_pred)²)
        """
        return np.sqrt(self.mean_squared_error(y_true, y_pred))

    def mean_absolute_error(self, y_true: np.ndarray, y_pred: np.ndarray) -> float:
        """
        Calculate Mean Absolute Error loss.

        MAE = (1/n) * Σ|y_true - y_pred|
        """
        return np.mean(np.abs(y_true - y_pred))

    def binary_cross_entropy(self, y_true: np.ndarray, y_pred: np.ndarray) -> float:
        """
        Calculate Binary Cross-Entropy loss.

        BCE = -(1/n) * Σ(y_true * log(y_pred) + (1-y_true) * log(1-y_pred))
        """
        # Clip predictions to avoid log(0)
        y_pred = np.clip(y_pred, self.epsilon, 1 - self.epsilon)
        return -np.mean(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))

    def categorical_cross_entropy(
        self, y_true: np.ndarray, y_pred: np.ndarray
    ) -> float:
        """
        Calculate Categorical Cross-Entropy loss.

        CCE = -(1/n) * Σ(y_true * log(y_pred))
        """
        y_pred = np.clip(y_pred, self.epsilon, 1.0)
        return -np.mean(np.sum(y_true * np.log(y_pred), axis=1))

    def huber_loss(
        self, y_true: np.ndarray, y_pred: np.ndarray, delta: float = 1.0
    ) -> float:
        """
        Calculate Huber loss.

        Combines MSE and MAE to be less sensitive to outliers.
        """
        error = y_true - y_pred
        is_small_error = np.abs(error) <= delta
        squared_loss = 0.5 * error**2
        linear_loss = delta * np.abs(error) - 0.5 * delta**2
        return np.mean(np.where(is_small_error, squared_loss, linear_loss))


def compare_losses(y_true: np.ndarray, y_pred: np.ndarray) -> None:
    """Compare different loss functions for given predictions"""
    loss = LossFunctions()

    losses = {
        "MSE": loss.mean_squared_error(y_true, y_pred),
        "RMSE": loss.root_mean_squared_error(y_true, y_pred),
        "MAE": loss.mean_absolute_error(y_true, y_pred),
        "Huber": loss.huber_loss(y_true, y_pred),
    }

    print("\nLoss Comparison:")
    for name, value in losses.items():
        print(f"{name}: {value:.4f}")


if __name__ == "__main__":
    # Regression example
    y_true_reg = np.array([3, -0.5, 2, 7])
    y_pred_reg = np.array([2.5, 0.0, 2, 8])

    print("Regression Losses:")
    compare_losses(y_true_reg, y_pred_reg)

    # Classification example
    y_true_cls = np.array([1, 0, 1, 1])
    y_pred_cls = np.array([0.9, 0.1, 0.8, 0.6])

    loss = LossFunctions()
    bce = loss.binary_cross_entropy(y_true_cls, y_pred_cls)
    print(f"\nBinary Cross-Entropy: {bce:.4f}")
