import numpy as np
import pandas as pd
from typing import Tuple, List
import matplotlib.pyplot as plt


class LSTMPredictor:
    """
    LSTM implementation for time series prediction.

    Time Complexity: O(sequence_length * hidden_size)
    Space Complexity: O(hidden_size)

    Example:
        >>> predictor = LSTMPredictor(input_size=1, hidden_size=32)
        >>> X, y = predictor.prepare_sequences(data, seq_length=10)
        >>> predictions = predictor.predict(X)
    """

    def __init__(self, input_size: int, hidden_size: int):
        """
        Initialize LSTM cell parameters

        Args:
            input_size: Number of input features
            hidden_size: Number of hidden units
        """
        self.hidden_size = hidden_size

        # Initialize weights
        self.Wf = np.random.randn(hidden_size, input_size + hidden_size) * 0.01
        self.Wi = np.random.randn(hidden_size, input_size + hidden_size) * 0.01
        self.Wc = np.random.randn(hidden_size, input_size + hidden_size) * 0.01
        self.Wo = np.random.randn(hidden_size, input_size + hidden_size) * 0.01

        # Initialize biases
        self.bf = np.zeros((hidden_size, 1))
        self.bi = np.zeros((hidden_size, 1))
        self.bc = np.zeros((hidden_size, 1))
        self.bo = np.zeros((hidden_size, 1))

    def sigmoid(self, x: np.ndarray) -> np.ndarray:
        """Compute sigmoid activation"""
        return 1 / (1 + np.exp(-x))

    def tanh(self, x: np.ndarray) -> np.ndarray:
        """Compute tanh activation"""
        return np.tanh(x)

    def forward(
        self, x: np.ndarray, h_prev: np.ndarray, c_prev: np.ndarray
    ) -> Tuple[np.ndarray, np.ndarray]:
        """
        Forward pass through LSTM cell

        Args:
            x: Input at current timestep
            h_prev: Previous hidden state
            c_prev: Previous cell state

        Returns:
            Tuple of (hidden state, cell state)
        """
        # Concatenate input and previous hidden state
        combined = np.vstack((h_prev, x))

        # Compute gates
        f = self.sigmoid(self.Wf @ combined + self.bf)
        i = self.sigmoid(self.Wi @ combined + self.bi)
        c_tilde = self.tanh(self.Wc @ combined + self.bc)
        o = self.sigmoid(self.Wo @ combined + self.bo)

        # Update states
        c = f * c_prev + i * c_tilde
        h = o * self.tanh(c)

        return h, c

    def prepare_sequences(
        self, data: np.ndarray, seq_length: int
    ) -> Tuple[np.ndarray, np.ndarray]:
        """Prepare sequences for training/prediction"""
        sequences = []
        targets = []

        for i in range(len(data) - seq_length):
            sequences.append(data[i : i + seq_length])
            targets.append(data[i + seq_length])

        return np.array(sequences), np.array(targets)

    def predict(self, X: np.ndarray) -> np.ndarray:
        """Make predictions for input sequences"""
        predictions = []
        batch_size, seq_length = X.shape

        for i in range(batch_size):
            # Initialize states
            h = np.zeros((self.hidden_size, 1))
            c = np.zeros((self.hidden_size, 1))

            # Process sequence
            sequence = X[i]
            for t in range(seq_length):
                x = sequence[t].reshape(1, 1)
                h, c = self.forward(x, h, c)

            predictions.append(h[0, 0])

        return np.array(predictions)


def generate_time_series(seq_length: int, frequency: float = 0.1) -> np.ndarray:
    """Generate synthetic time series data"""
    t = np.linspace(0, seq_length * frequency, seq_length)
    series = np.sin(t) + 0.1 * np.random.randn(seq_length)
    return series


def plot_predictions(
    actual: np.ndarray, predicted: np.ndarray, title: str = "LSTM Predictions"
) -> None:
    """Plot actual vs predicted values"""
    plt.figure(figsize=(12, 6))
    plt.plot(actual, label="Actual", alpha=0.7)
    plt.plot(predicted, label="Predicted", alpha=0.7)
    plt.title(title)
    plt.xlabel("Time")
    plt.ylabel("Value")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    # Generate data
    data = generate_time_series(1000)

    # Create sequences
    seq_length = 20
    predictor = LSTMPredictor(input_size=1, hidden_size=32)
    X, y = predictor.prepare_sequences(data, seq_length)

    # Make predictions
    predictions = predictor.predict(X)

    # Plot results
    plot_predictions(y[:100], predictions[:100])
