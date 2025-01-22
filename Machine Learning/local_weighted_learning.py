import numpy as np
from typing import Tuple, Optional
import matplotlib.pyplot as plt


class LocalWeightedLearning:
    """
    Implementation of Local Weighted Learning using locally weighted linear regression.

    Time Complexity: O(n * q * d^3), where:
        n: number of training samples
        q: number of query points
        d: number of features

    Space Complexity: O(n * d), where:
        n: number of training samples
        d: number of features

    Example:
        >>> X = np.array([[1], [2], [3], [4], [5]])
        >>> y = np.array([2.1, 3.8, 6.2, 7.5, 9.0])
        >>> model = LocalWeightedLearning(tau=1.0)
        >>> model.fit(X, y)
        >>> predictions = model.predict(np.array([[2.5]]))
    """

    def __init__(self, tau: float = 1.0):
        """
        Args:
            tau: Bandwidth parameter controlling the extent of local weighting
        """
        self.tau = tau
        self.X_train = None
        self.y_train = None

    def _compute_weights(self, X: np.ndarray, query_point: np.ndarray) -> np.ndarray:
        """Calculate Gaussian kernel weights based on distance from query point"""
        distances = np.sum((X - query_point) ** 2, axis=1)
        return np.exp(-distances / (2 * self.tau**2))

    def fit(self, X: np.ndarray, y: np.ndarray) -> None:
        """Store training data for later use in predictions"""
        self.X_train = np.column_stack([X, np.ones_like(X)])  # Add bias term
        self.y_train = y

    def predict(self, X_query: np.ndarray) -> np.ndarray:
        """
        Make predictions for query points using locally weighted regression

        Args:
            X_query: Query points to make predictions for

        Returns:
            Array of predictions
        """
        X_query = np.column_stack([X_query, np.ones_like(X_query)])  # Add bias term
        predictions = []

        for x_q in X_query:
            # Compute weights for current query point
            weights = self._compute_weights(self.X_train[:, :-1], x_q[:-1])
            W = np.diag(weights)

            # Weighted least squares solution
            try:
                beta = np.linalg.solve(
                    self.X_train.T @ W @ self.X_train, self.X_train.T @ W @ self.y_train
                )
                pred = x_q @ beta
            except np.linalg.LinAlgError:
                # Fallback to mean prediction if matrix is singular
                pred = np.mean(self.y_train)

            predictions.append(pred)

        return np.array(predictions)

    def plot_fit(
        self,
        X_train: np.ndarray,
        y_train: np.ndarray,
        X_query: np.ndarray,
        predictions: np.ndarray,
    ) -> None:
        """Visualize the training data and model predictions"""
        plt.figure(figsize=(10, 6))
        plt.scatter(X_train, y_train, color="blue", label="Training Data")
        plt.plot(X_query, predictions, color="red", label="LWL Predictions")
        plt.title("Local Weighted Learning")
        plt.xlabel("X")
        plt.ylabel("y")
        plt.legend()
        plt.grid(True)
        plt.show()


if __name__ == "__main__":
    # Generate sample data
    X = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])
    y = np.array([1.5, 1.8, 2.5, 3.5, 5.0, 6.0, 6.5, 8.0, 8.5, 10.0])

    # Create and fit model
    model = LocalWeightedLearning(tau=1.5)
    model.fit(X, y)

    # Generate predictions
    X_query = np.linspace(1, 10, 100).reshape(-1, 1)
    predictions = model.predict(X_query)

    # Visualize results
    model.plot_fit(X, y, X_query, predictions)
