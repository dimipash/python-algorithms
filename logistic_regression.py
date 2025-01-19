import numpy as np
from typing import Tuple, Optional
import matplotlib.pyplot as plt


class LogisticRegressor:
    """
    Logistic Regression implementation using gradient descent.

    Time Complexity: O(n_samples * n_iterations)
    Space Complexity: O(n_features)

    Example:
        >>> X = np.array([[1], [2], [3], [4], [5]])
        >>> y = np.array([0, 0, 0, 1, 1])
        >>> model = LogisticRegressor(learning_rate=0.1, n_iterations=1000)
        >>> model.fit(X, y)
        >>> predictions = model.predict(X)
    """

    def __init__(self, learning_rate: float = 0.01, n_iterations: int = 1000):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.weights = None
        self.bias = None

    def _sigmoid(self, z: np.ndarray) -> np.ndarray:
        """Apply sigmoid activation function"""
        return 1 / (1 + np.exp(-z))

    def fit(self, X: np.ndarray, y: np.ndarray) -> None:
        """
        Fit logistic regression using gradient descent.

        Args:
            X: Training features of shape (n_samples, n_features)
            y: Binary target values of shape (n_samples,)
        """
        n_samples, n_features = X.shape

        # Initialize parameters
        self.weights = np.zeros(n_features)
        self.bias = 0

        # Gradient descent
        for _ in range(self.n_iterations):
            # Forward pass
            linear_pred = np.dot(X, self.weights) + self.bias
            predictions = self._sigmoid(linear_pred)

            # Compute gradients
            dw = (1 / n_samples) * np.dot(X.T, (predictions - y))
            db = (1 / n_samples) * np.sum(predictions - y)

            # Update parameters
            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db

    def predict_proba(self, X: np.ndarray) -> np.ndarray:
        """Predict probability of class 1"""
        linear_pred = np.dot(X, self.weights) + self.bias
        return self._sigmoid(linear_pred)

    def predict(self, X: np.ndarray, threshold: float = 0.5) -> np.ndarray:
        """Predict class labels"""
        probabilities = self.predict_proba(X)
        return (probabilities >= threshold).astype(int)

    def score(self, X: np.ndarray, y: np.ndarray) -> float:
        """Calculate accuracy score"""
        predictions = self.predict(X)
        return np.mean(predictions == y)

    def plot_decision_boundary(self, X: np.ndarray, y: np.ndarray) -> None:
        """Plot the decision boundary and data points"""
        plt.figure(figsize=(10, 6))

        # Plot data points
        plt.scatter(
            X[y == 0], np.zeros(sum(y == 0)), color="blue", label="Class 0", alpha=0.5
        )
        plt.scatter(
            X[y == 1], np.ones(sum(y == 1)), color="red", label="Class 1", alpha=0.5
        )

        # Plot decision boundary
        x_boundary = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)
        y_boundary = self.predict_proba(x_boundary)
        plt.plot(x_boundary, y_boundary, "g-", label="Decision Boundary")

        plt.title("Logistic Regression Decision Boundary")
        plt.xlabel("Feature Value")
        plt.ylabel("Probability / Class")
        plt.legend()
        plt.grid(True)
        plt.show()


def train_test_split(
    X: np.ndarray,
    y: np.ndarray,
    test_size: float = 0.2,
    random_state: Optional[int] = None,
) -> Tuple:
    """Split arrays into random train and test subsets"""
    if random_state is not None:
        np.random.seed(random_state)

    n_samples = len(X)
    n_test = int(n_samples * test_size)
    indices = np.random.permutation(n_samples)

    test_idx = indices[:n_test]
    train_idx = indices[n_test:]

    return (X[train_idx], X[test_idx], y[train_idx], y[test_idx])


if __name__ == "__main__":
    # Generate sample data
    X = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])
    y = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Create and train model
    model = LogisticRegressor(learning_rate=0.1, n_iterations=1000)
    model.fit(X_train, y_train)

    # Make predictions
    y_pred = model.predict(X_test)
    probabilities = model.predict_proba(X_test)

    # Print results
    print(f"Accuracy: {model.score(X_test, y_test):.4f}")
    for i, (x, pred, prob) in enumerate(zip(X_test, y_pred, probabilities)):
        print(f"Sample {i+1}: X={x[0]}, Predicted={pred}, Probability={prob:.4f}")

    # Plot results
    model.plot_decision_boundary(X, y)
