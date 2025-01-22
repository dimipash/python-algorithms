import numpy as np
from typing import List, Tuple
import matplotlib.pyplot as plt


class TwoLayerNeuralNetwork:
    """
    Neural network implementation with two hidden layers.

    Time Complexity: O(n_samples * (n1 * n2 + n2 * n3)) per epoch
    Space Complexity: O(n1 * n2 + n2 * n3) for weights

    Example:
        >>> model = TwoLayerNeuralNetwork([10, 16, 8, 1])
        >>> model.fit(X_train, y_train, epochs=100)
        >>> predictions = model.predict(X_test)
    """

    def __init__(self, layer_sizes: List[int], learning_rate: float = 0.01):
        """
        Args:
            layer_sizes: List containing [input_size, hidden1_size, hidden2_size, output_size]
            learning_rate: Learning rate for gradient descent
        """
        self.layer_sizes = layer_sizes
        self.learning_rate = learning_rate
        self.history = {"loss": [], "accuracy": []}

        # Initialize weights and biases
        self.weights = [
            np.random.randn(layer_sizes[0], layer_sizes[1])
            * np.sqrt(2 / layer_sizes[0]),  # He initialization
            np.random.randn(layer_sizes[1], layer_sizes[2])
            * np.sqrt(2 / layer_sizes[1]),
            np.random.randn(layer_sizes[2], layer_sizes[3])
            * np.sqrt(2 / layer_sizes[2]),
        ]

        self.biases = [
            np.zeros((1, layer_sizes[1])),
            np.zeros((1, layer_sizes[2])),
            np.zeros((1, layer_sizes[3])),
        ]

    def relu(self, x: np.ndarray) -> np.ndarray:
        """ReLU activation function"""
        return np.maximum(0, x)

    def relu_derivative(self, x: np.ndarray) -> np.ndarray:
        """Derivative of ReLU function"""
        return (x > 0).astype(float)

    def sigmoid(self, x: np.ndarray) -> np.ndarray:
        """Sigmoid activation function"""
        return 1 / (1 + np.exp(-np.clip(x, -500, 500)))

    def forward(self, X: np.ndarray) -> Tuple[List[np.ndarray], List[np.ndarray]]:
        """
        Forward pass through the network

        Returns:
            Tuple of (activations, weighted_sums)
        """
        activations = [X]
        weighted_sums = []

        # First hidden layer (ReLU)
        z1 = np.dot(X, self.weights[0]) + self.biases[0]
        a1 = self.relu(z1)
        weighted_sums.append(z1)
        activations.append(a1)

        # Second hidden layer (ReLU)
        z2 = np.dot(a1, self.weights[1]) + self.biases[1]
        a2 = self.relu(z2)
        weighted_sums.append(z2)
        activations.append(a2)

        # Output layer (Sigmoid)
        z3 = np.dot(a2, self.weights[2]) + self.biases[2]
        a3 = self.sigmoid(z3)
        weighted_sums.append(z3)
        activations.append(a3)

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

        # Output layer error
        delta3 = activations[-1] - y

        # Second hidden layer error
        delta2 = np.dot(delta3, self.weights[2].T) * self.relu_derivative(
            weighted_sums[1]
        )

        # First hidden layer error
        delta1 = np.dot(delta2, self.weights[1].T) * self.relu_derivative(
            weighted_sums[0]
        )

        # Compute gradients
        weight_grads = [
            np.dot(X.T, delta1) / m,
            np.dot(activations[1].T, delta2) / m,
            np.dot(activations[2].T, delta3) / m,
        ]

        bias_grads = [
            np.sum(delta1, axis=0, keepdims=True) / m,
            np.sum(delta2, axis=0, keepdims=True) / m,
            np.sum(delta3, axis=0, keepdims=True) / m,
        ]

        return weight_grads, bias_grads

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

                # Forward and backward passes
                activations, weighted_sums = self.forward(batch_X)
                weight_grads, bias_grads = self.backward(
                    batch_X, batch_y, activations, weighted_sums
                )

                # Update parameters
                for j in range(len(self.weights)):
                    self.weights[j] -= self.learning_rate * weight_grads[j]
                    self.biases[j] -= self.learning_rate * bias_grads[j]

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
    model = TwoLayerNeuralNetwork([10, 16, 8, 1])
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
