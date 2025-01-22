import numpy as np
from typing import Tuple
import matplotlib.pyplot as plt


class LinearRegressor:
    """
    Linear Regression implementation using gradient descent.

    Time Complexity: O(n_samples * n_iterations)
    Space Complexity: O(n_features)

    Example:
        >>> X = np.array([[1500], [1800], [2400], [3000], [3500]])
        >>> y = np.array([300000, 400000, 500000, 600000, 700000])
        >>> model = LinearRegressor(learning_rate=0.01, n_iterations=1000)
        >>> model.fit(X, y)
        >>> predictions = model.predict(X)
    """

    def __init__(self, learning_rate: float = 0.01, n_iterations: int = 1000):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.weights = None
        self.bias = None
        self.history = {"loss": []}

    def fit(self, X: np.ndarray, y: np.ndarray) -> None:
        """
        Fit linear regression using gradient descent.

        Args:
            X: Training data of shape (n_samples, n_features)
            y: Target values of shape (n_samples,)
        """
        n_samples, n_features = X.shape

        # Initialize parameters
        self.weights = np.zeros(n_features)
        self.bias = 0

        # Gradient descent
        for _ in range(self.n_iterations):
            # Forward pass
            y_pred = self._forward(X)

            # Compute gradients
            dw = (1 / n_samples) * np.dot(X.T, (y_pred - y))
            db = (1 / n_samples) * np.sum(y_pred - y)

            # Update parameters
            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db

            # Track loss
            loss = self._compute_loss(y, y_pred)
            self.history["loss"].append(loss)

    def predict(self, X: np.ndarray) -> np.ndarray:
        """Make predictions for input data"""
        return self._forward(X)

    def _forward(self, X: np.ndarray) -> np.ndarray:
        """Forward pass computation"""
        return np.dot(X, self.weights) + self.bias

    def _compute_loss(self, y_true: np.ndarray, y_pred: np.ndarray) -> float:
        """Compute Mean Squared Error loss"""
        return np.mean((y_true - y_pred) ** 2)

    def score(self, X: np.ndarray, y: np.ndarray) -> float:
        """Calculate R-squared score"""
        y_pred = self.predict(X)
        ss_tot = np.sum((y - y.mean()) ** 2)
        ss_res = np.sum((y - y_pred) ** 2)
        return 1 - (ss_res / ss_tot)

    def plot_regression(self, X: np.ndarray, y: np.ndarray) -> None:
        """Plot the regression line and data points"""
        plt.figure(figsize=(10, 6))
        plt.scatter(X, y, color="blue", label="Data points")
        plt.plot(X, self.predict(X), color="red", label="Regression line")
        plt.title("Linear Regression")
        plt.xlabel("X")
        plt.ylabel("y")
        plt.legend()
        plt.show()


def train_test_split(X: np.ndarray, y: np.ndarray, test_size: float = 0.2) -> Tuple:
    """Split data into training and testing sets"""
    n_samples = len(X)
    n_test = int(n_samples * test_size)
    indices = np.random.permutation(n_samples)
    test_idx, train_idx = indices[:n_test], indices[n_test:]
    return X[train_idx], X[test_idx], y[train_idx], y[test_idx]


if __name__ == "__main__":
    # Generate sample data
    X = np.array([[1500], [1800], [2400], [3000], [3500]])
    y = np.array([300000, 400000, 500000, 600000, 700000])

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # Create and train model
    model = LinearRegressor(learning_rate=1e-7, n_iterations=1000)
    model.fit(X_train, y_train)

    # Make predictions
    y_pred = model.predict(X_test)

    # Print metrics
    print(f"R-squared score: {model.score(X_test, y_test):.4f}")
    print(f"Final loss: {model.history['loss'][-1]:.2f}")

    # Plot results
    model.plot_regression(X, y)
