import numpy as np
from typing import Tuple, List
import matplotlib.pyplot as plt


class ConvLayer:
    """
    Convolutional layer implementation.

    Time Complexity: O(n_filters * input_depth * kernel_size^2 * output_size^2)
    Space Complexity: O(output_size^2 * n_filters)
    """

    def __init__(
        self,
        n_filters: int,
        kernel_size: int,
        input_shape: Tuple[int, int, int],
        stride: int = 1,
        padding: str = "valid",
    ):
        self.n_filters = n_filters
        self.kernel_size = kernel_size
        self.input_shape = input_shape
        self.stride = stride
        self.padding = padding

        # Initialize filters and biases
        self.filters = (
            np.random.randn(n_filters, input_shape[2], kernel_size, kernel_size) * 0.1
        )
        self.biases = np.zeros(n_filters)

    def forward(self, input_data: np.ndarray) -> np.ndarray:
        """Forward pass of convolution operation"""
        self.input = input_data
        batch_size, h, w, channels = input_data.shape

        # Calculate output dimensions
        h_out = (h - self.kernel_size) // self.stride + 1
        w_out = (w - self.kernel_size) // self.stride + 1

        output = np.zeros((batch_size, h_out, w_out, self.n_filters))

        # Perform convolution
        for i in range(h_out):
            for j in range(w_out):
                h_start = i * self.stride
                h_end = h_start + self.kernel_size
                w_start = j * self.stride
                w_end = w_start + self.kernel_size

                receptive_field = input_data[:, h_start:h_end, w_start:w_end, :]

                for k in range(self.n_filters):
                    output[:, i, j, k] = (
                        np.sum(receptive_field * self.filters[k], axis=(1, 2, 3))
                        + self.biases[k]
                    )

        return output


class MaxPoolLayer:
    """
    Max pooling layer implementation.

    Time Complexity: O(input_size^2)
    Space Complexity: O(output_size^2)
    """

    def __init__(self, pool_size: int = 2, stride: int = 2):
        self.pool_size = pool_size
        self.stride = stride

    def forward(self, input_data: np.ndarray) -> np.ndarray:
        """Forward pass of max pooling operation"""
        batch_size, h, w, channels = input_data.shape

        h_out = (h - self.pool_size) // self.stride + 1
        w_out = (w - self.pool_size) // self.stride + 1

        output = np.zeros((batch_size, h_out, w_out, channels))

        for i in range(h_out):
            for j in range(w_out):
                h_start = i * self.stride
                h_end = h_start + self.pool_size
                w_start = j * self.stride
                w_end = w_start + self.pool_size

                output[:, i, j, :] = np.max(
                    input_data[:, h_start:h_end, w_start:w_end, :], axis=(1, 2)
                )

        return output


class CNN:
    """
    Convolutional Neural Network implementation.
    """

    def __init__(self, input_shape: Tuple[int, int, int], num_classes: int):
        self.input_shape = input_shape
        self.num_classes = num_classes

        # Define network architecture
        self.layers = []
        self._build_network()

    def _build_network(self):
        """Build the CNN architecture"""
        # First convolutional block
        self.layers.append(ConvLayer(32, 3, self.input_shape))
        self.layers.append(MaxPoolLayer())

        # Second convolutional block
        self.layers.append(ConvLayer(64, 3, (32, 32, 32)))
        self.layers.append(MaxPoolLayer())

        # Third convolutional block
        self.layers.append(ConvLayer(64, 3, (16, 16, 64)))

    def forward(self, x: np.ndarray) -> np.ndarray:
        """Forward pass through the network"""
        for layer in self.layers:
            x = layer.forward(x)
        return x

    def summary(self):
        """Print model summary"""
        print("\nCNN Architecture Summary:")
        print("-" * 80)
        print(f"{'Layer Type':<20} {'Output Shape':<20} {'Parameters':<20}")
        print("-" * 80)

        current_shape = (None,) + self.input_shape
        total_params = 0

        for i, layer in enumerate(self.layers):
            if isinstance(layer, ConvLayer):
                params = (
                    layer.kernel_size * layer.kernel_size * current_shape[-1] + 1
                ) * layer.n_filters
                output_shape = (
                    None,
                    (current_shape[1] - layer.kernel_size) // layer.stride + 1,
                    (current_shape[2] - layer.kernel_size) // layer.stride + 1,
                    layer.n_filters,
                )
                layer_type = "Conv2D"

            elif isinstance(layer, MaxPoolLayer):
                params = 0
                output_shape = (
                    None,
                    (current_shape[1] - layer.pool_size) // layer.stride + 1,
                    (current_shape[2] - layer.pool_size) // layer.stride + 1,
                    current_shape[-1],
                )
                layer_type = "MaxPooling2D"

            current_shape = output_shape
            total_params += params

            print(f"{layer_type:<20} {str(output_shape):<20} {params:<20}")

        print("-" * 80)
        print(f"Total parameters: {total_params:,}")


if __name__ == "__main__":
    # Example usage
    input_shape = (64, 64, 3)
    num_classes = 10

    # Create model
    model = CNN(input_shape, num_classes)

    # Print model summary
    model.summary()

    # Example forward pass
    batch_size = 4
    sample_input = np.random.randn(batch_size, *input_shape)
    output = model.forward(sample_input)
    print(f"\nOutput shape: {output.shape}")
