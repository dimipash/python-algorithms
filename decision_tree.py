class DecisionTree:
    """
    Implementation of a Decision Tree classifier using recursive binary splitting.

    Time Complexity: O(n*d*log(n)) where n is number of samples and d is number of features
    Space Complexity: O(log(n)) for balanced tree

    Attributes:
        max_depth: Maximum depth of the tree
        min_samples_split: Minimum samples required to split a node

    Example:
        >>> X = np.array([
        ...     [1, 2], [2, 3], [3, 4], [4, 5], [5, 6],
        ...     [6, 7], [7, 8], [8, 9], [9, 10], [10, 11]
        ... ])
        >>> y = np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1])
        >>> tree = DecisionTree(max_depth=3)
        >>> tree.fit(X, y)
        >>> tree.predict(np.array([[3, 3], [7, 7]]))
        array([0, 1])
    """

    class Node:
        def __init__(self):
            self.feature = None
            self.threshold = None
            self.left = None
            self.right = None
            self.value = None

    def __init__(self, max_depth=5, min_samples_split=2):
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.root = None

    def fit(self, X: np.ndarray, y: np.ndarray):
        """Builds the decision tree by recursive splitting"""
        self.n_classes = len(np.unique(y))
        self.root = self._grow_tree(X, y)

    def _grow_tree(self, X: np.ndarray, y: np.ndarray, depth=0) -> Node:
        """Recursively grows the decision tree"""
        n_samples, n_features = X.shape
        node = self.Node()

        # Check stopping criteria
        if (
            depth >= self.max_depth
            or n_samples < self.min_samples_split
            or len(np.unique(y)) == 1
        ):
            node.value = self._most_common_label(y)
            return node

        # Find best split
        best_feature, best_threshold = self._best_split(X, y)

        if best_feature is None:
            node.value = self._most_common_label(y)
            return node

        # Split data
        left_mask = X[:, best_feature] <= best_threshold
        X_left, y_left = X[left_mask], y[left_mask]
        X_right, y_right = X[~left_mask], y[~left_mask]

        # Create child nodes
        node.feature = best_feature
        node.threshold = best_threshold
        node.left = self._grow_tree(X_left, y_left, depth + 1)
        node.right = self._grow_tree(X_right, y_right, depth + 1)

        return node

    def predict(self, X: np.ndarray) -> np.ndarray:
        """Makes predictions for samples in X"""
        return np.array([self._traverse_tree(x, self.root) for x in X])

    def _traverse_tree(self, x: np.ndarray, node: Node) -> int:
        """Traverses the tree to make a prediction"""
        if node.value is not None:
            return node.value

        if x[node.feature] <= node.threshold:
            return self._traverse_tree(x, node.left)
        return self._traverse_tree(x, node.right)

    def _best_split(self, X: np.ndarray, y: np.ndarray) -> tuple:
        """Finds the best split using Gini impurity"""
        best_gain = -1
        best_feature = None
        best_threshold = None

        for feature in range(X.shape[1]):
            thresholds = np.unique(X[:, feature])
            for threshold in thresholds:
                gain = self._information_gain(y, X[:, feature], threshold)
                if gain > best_gain:
                    best_gain = gain
                    best_feature = feature
                    best_threshold = threshold

        return best_feature, best_threshold

    def _most_common_label(self, y: np.ndarray) -> int:
        """Returns the most common class label"""
        return np.bincount(y).argmax()

    def _information_gain(
        self, y: np.ndarray, feature: np.ndarray, threshold: float
    ) -> float:
        """Calculates information gain for a split"""
        parent_gini = self._gini(y)

        left_mask = feature <= threshold
        left_y = y[left_mask]
        right_y = y[~left_mask]

        if len(left_y) == 0 or len(right_y) == 0:
            return 0

        n = len(y)
        n_l, n_r = len(left_y), len(right_y)
        gini_left = self._gini(left_y)
        gini_right = self._gini(right_y)

        child_gini = (n_l / n) * gini_left + (n_r / n) * gini_right
        return parent_gini - child_gini

    def _gini(self, y: np.ndarray) -> float:
        """Calculates Gini impurity"""
        _, counts = np.unique(y, return_counts=True)
        probabilities = counts / len(y)
        return 1 - np.sum(probabilities**2)


if __name__ == "__main__":
    # Sample data
    X = np.array(
        [
            [1, 2],
            [2, 3],
            [3, 4],
            [4, 5],
            [5, 6],
            [6, 7],
            [7, 8],
            [8, 9],
            [9, 10],
            [10, 11],
        ]
    )
    y = np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1])

    # Train model
    tree = DecisionTree(max_depth=3)
    tree.fit(X, y)

    # Make predictions
    X_test = np.array([[3, 3], [7, 7]])
    predictions = tree.predict(X_test)
    print(f"Predictions for test points: {predictions}")
