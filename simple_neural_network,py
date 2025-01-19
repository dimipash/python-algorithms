import numpy as np
from typing import List, Tuple
import matplotlib.pyplot as plt


class SimpleNeuralNetwork:
    """
    Implementation of a basic feedforward neural network.

    Time Complexity: O(n_samples * n_features * n_hidden)
    Space Complexity: O(n_hidden * n_features)

    Example:
        >>> model = SimpleNeuralNetwork([10, 16, 1])
        >>> model.fit(X_train, y_train, epochs=10)
        >>> predictions = model.predict(X_test)
    """

    def __init__(self, layer_sizes: List[int], learning_rate: float = 0.01):
        """
        Args:
            layer_sizes: List of neurons per layer (input, hidden, output)
            learning_rate: Learning rate for gradient descent
        """
        self.layer_sizes = layer_sizes
        self.learning_rate = learning_rate
        self.weights = []
        self.biases = []
        self.history = {"loss": [], "accuracy": []}

        # Initialize weights and biases
        for i in range(len(layer_sizes) - 1):
            self.weights.append(
                np.random.randn(layer_sizes[i], layer_sizes[i + 1]) * 0.01
            )
            self.biases.append(np.zeros((1, layer_sizes[i + 1])))

    def sigmoid(self, x: np.ndarray) -> np.ndarray:
        """Sigmoid activation function"""
        return 1 / (1 + np.exp(-np.clip(x, -500, 500)))

    def sigmoid_derivative(self, x: np.ndarray) -> np.ndarray:
        """Derivative of sigmoid function"""
        sx = self.sigmoid(x)
        return sx * (1 - sx)

    def forward(self, X: np.ndarray) -> Tuple[List[np.ndarray], List[np.ndarray]]:
        """
        Forward pass through the network

        Args:
            X: Input data of shape (n_samples, n_features)

        Returns:
            Tuple of activations and weighted sums per layer
        """
        activations = [X]
        weighted_sums = []

        for i in range(len(self.weights)):
            z = np.dot(activations[-1], self.weights[i]) + self.biases[i]
            weighted_sums.append(z)
            activations.append(self.sigmoid(z))

        return activations, weighted_sums

    def backward(
        self,
        X: np.ndarray,
        y: np.ndarray,
        activations: List[np.ndarray],
        weighted_sums: List[np.ndarray],
    ) -> Tuple[List[np.ndarray], List[np.ndarray]]:
        """Backward pass to compute gradients"""
        m = X.shape[0]
        delta = activations[-1] - y

        weight_gradients = []
        bias_gradients = []

        for i in range(len(self.weights) - 1, -1, -1):
            weight_gradients.insert(0, np.dot(activations[i].T, delta) / m)
            bias_gradients.insert(0, np.sum(delta, axis=0, keepdims=True) / m)

            if i > 0:
                delta = np.dot(delta, self.weights[i].T) * self.sigmoid_derivative(
                    weighted_sums[i - 1]
                )

        return weight_gradients, bias_gradients

    def fit(
        self,
        X: np.ndarray,
        y: np.ndarray,
        epochs: int = 100,
        batch_size: int = 32,
        verbose: bool = True,
    ) -> None:
        """Train the neural network"""
        m = X.shape[0]

        for epoch in range(epochs):
            # Mini-batch gradient descent
            for i in range(0, m, batch_size):
                batch_X = X[i : i + batch_size]
                batch_y = y[i : i + batch_size]

                # Forward pass
                activations, weighted_sums = self.forward(batch_X)

                # Backward pass
                weight_gradients, bias_gradients = self.backward(
                    batch_X, batch_y, activations, weighted_sums
                )

                # Update weights and biases
                for j in range(len(self.weights)):
                    self.weights[j] -= self.learning_rate * weight_gradients[j]
                    self.biases[j] -= self.learning_rate * bias_gradients[j]

            # Compute metrics
            predictions = self.predict(X)
            loss = self.compute_loss(y, predictions)
            accuracy = self.compute_accuracy(y, predictions)

            self.history["loss"].append(loss)
            self.history["accuracy"].append(accuracy)

            if verbose and epoch % 10 == 0:
                print(f"Epoch {epoch}: Loss = {loss:.4f}, Accuracy = {accuracy:.4f}")

    def predict(self, X: np.ndarray) -> np.ndarray:
        """Make predictions"""
        return self.forward(X)[0][-1]

    def compute_loss(self, y_true: np.ndarray, y_pred: np.ndarray) -> float:
        """Compute binary cross-entropy loss"""
        epsilon = 1e-15
        y_pred = np.clip(y_pred, epsilon, 1 - epsilon)
        return -np.mean(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))

    def compute_accuracy(self, y_true: np.ndarray, y_pred: np.ndarray) -> float:
        """Compute classification accuracy"""
        predictions = (y_pred > 0.5).astype(int)
        return np.mean(predictions == y_true)

    def plot_history(self) -> None:
        """Plot training history"""
        plt.figure(figsize=(12, 4))

        plt.subplot(1, 2, 1)
        plt.plot(self.history["loss"])
        plt.title("Training Loss")
        plt.xlabel("Epoch")
        plt.ylabel("Loss")

        plt.subplot(1, 2, 2)
        plt.plot(self.history["accuracy"])
        plt.title("Training Accuracy")
        plt.xlabel("Epoch")
        plt.ylabel("Accuracy")

        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    # Generate synthetic data
    np.random.seed(42)
    X_train = np.random.rand(1000, 10)
    y_train = np.random.randint(2, size=(1000, 1))

    # Create and train model
    model = SimpleNeuralNetwork([10, 16, 1])
    model.fit(X_train, y_train, epochs=100)

    # Evaluate model
    predictions = model.predict(X_train)
    loss = model.compute_loss(y_train, predictions)
    accuracy = model.compute_accuracy(y_train, predictions)

    print(f"\nFinal Results:")
    print(f"Loss: {loss:.4f}")
    print(f"Accuracy: {accuracy:.4f}")

    # Plot training history
    model.plot_history()
