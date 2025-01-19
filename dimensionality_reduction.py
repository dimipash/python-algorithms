from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd


def reduce_dimensionality(data: pd.DataFrame, n_components: int) -> np.ndarray:
    """
    Perform dimensionality reduction using PCA on input data.

    Args:
        data (pd.DataFrame): Input dataset with features as columns
        n_components (int): Number of components to reduce to

    Returns:
        np.ndarray: Transformed data with reduced dimensions

    Time Complexity: O(min(n_samples^2 * n_features, n_samples * n_features^2))
    Space Complexity: O(n_samples * n_components)

    Example:
        >>> df = pd.DataFrame({
        ...     'Feature1': [2.5, 3.5, 1.5, 4.5],
        ...     'Feature2': [2.5, 0.5, 2.0, 1.0],
        ...     'Feature3': [1.0, 2.0, 3.0, 4.0]
        ... })
        >>> reduced = reduce_dimensionality(df, 2)
        >>> print(reduced.shape)
        (4, 2)
    """
    # Standardize features to zero mean and unit variance
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)

    # Initialize and apply PCA
    pca = PCA(n_components=n_components)
    reduced_data = pca.fit_transform(scaled_data)

    return reduced_data


if __name__ == "__main__":
    # Example usage
    df = pd.DataFrame(
        {
            "Feature1": [2.5, 3.5, 1.5, 4.5],
            "Feature2": [2.5, 0.5, 2.0, 1.0],
            "Feature3": [1.0, 2.0, 3.0, 4.0],
        }
    )

    reduced_data = reduce_dimensionality(df, 2)
    print("Original shape:", df.shape)
    print("Reduced shape:", reduced_data.shape)
