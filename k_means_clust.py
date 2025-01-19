import numpy as np
from typing import Tuple, Optional
import matplotlib.pyplot as plt


class KMeansCluster:
    """
    Implementation of K-Means clustering algorithm.

    Time Complexity: O(n_samples * n_clusters * n_iterations)
    Space Complexity: O(n_samples + n_clusters)

    Example:
        >>> X = np.array([[1, 2], [1, 4], [1, 0], [4, 2], [4, 4], [4, 0]])
        >>> kmeans = KMeansCluster(n_clusters=2, max_iters=100)
        >>> labels, centroids = kmeans.fit(X)
        >>> print(f"Cluster assignments: {labels}")
    """

    def __init__(
        self,
        n_clusters: int = 2,
        max_iters: int = 100,
        random_state: Optional[int] = None,
    ):
        self.n_clusters = n_clusters
        self.max_iters = max_iters
        self.random_state = random_state

    def _init_centroids(self, X: np.ndarray) -> np.ndarray:
        """Initialize cluster centroids randomly"""
        if self.random_state:
            np.random.seed(self.random_state)
        idx = np.random.permutation(X.shape[0])[: self.n_clusters]
        return X[idx]

    def _assign_clusters(self, X: np.ndarray, centroids: np.ndarray) -> np.ndarray:
        """Assign each point to nearest centroid"""
        distances = np.sqrt(((X - centroids[:, np.newaxis]) ** 2).sum(axis=2))
        return np.argmin(distances, axis=0)

    def _update_centroids(self, X: np.ndarray, labels: np.ndarray) -> np.ndarray:
        """Update centroids based on mean of assigned points"""
        centroids = np.zeros((self.n_clusters, X.shape[1]))
        for k in range(self.n_clusters):
            if np.sum(labels == k) > 0:
                centroids[k] = np.mean(X[labels == k], axis=0)
        return centroids

    def fit(self, X: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        """
        Fit K-Means clustering to data.

        Args:
            X: Input data of shape (n_samples, n_features)

        Returns:
            Tuple containing:
                - labels: Cluster assignments for each point
                - centroids: Final cluster centroids
        """
        # Initialize centroids
        centroids = self._init_centroids(X)

        # Iterate until convergence
        for _ in range(self.max_iters):
            old_centroids = centroids.copy()

            # Assign clusters
            labels = self._assign_clusters(X, centroids)

            # Update centroids
            centroids = self._update_centroids(X, labels)

            # Check convergence
            if np.all(old_centroids == centroids):
                break

        return labels, centroids

    def plot_clusters(
        self, X: np.ndarray, labels: np.ndarray, centroids: np.ndarray
    ) -> None:
        """Plot clustered data points and centroids"""
        plt.figure(figsize=(8, 6))
        plt.scatter(X[:, 0], X[:, 1], c=labels, cmap="rainbow")
        plt.scatter(
            centroids[:, 0],
            centroids[:, 1],
            color="black",
            marker="x",
            s=200,
            linewidth=3,
        )
        plt.title("K-Means Clustering")
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.show()


if __name__ == "__main__":
    # Generate sample data
    X = np.array([[1, 2], [1, 4], [1, 0], [4, 2], [4, 4], [4, 0]])

    # Initialize and fit KMeans
    kmeans = KMeansCluster(n_clusters=2, random_state=42)
    labels, centroids = kmeans.fit(X)

    # Print results
    print("Cluster Labels:", labels)
    print("Centroids:\n", centroids)

    # Plot results
    kmeans.plot_clusters(X, labels, centroids)
