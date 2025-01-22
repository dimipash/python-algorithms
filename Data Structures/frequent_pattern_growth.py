from collections import defaultdict
from typing import List, Dict, Set, Optional
import pandas as pd


class FPNode:
    """Node in FP-tree representing an item and its count"""

    def __init__(self, item: str, count: int = 1, parent: Optional["FPNode"] = None):
        self.item = item
        self.count = count
        self.parent = parent
        self.children: Dict[str, FPNode] = {}
        self.next = None  # Link to next node with same item


class FPGrowth:
    """
    Implementation of FP-Growth algorithm for mining frequent itemsets.

    Time Complexity: O(n), where n is number of transactions
    Space Complexity: O(m), where m is number of unique items

    Example:
        >>> transactions = [
        ...     ['A', 'B', 'D'],
        ...     ['B', 'C'],
        ...     ['A', 'B', 'C', 'E'],
        ...     ['B', 'E'],
        ...     ['A', 'B', 'C', 'D']
        ... ]
        >>> fp = FPGrowth(min_support=0.6)
        >>> patterns = fp.find_frequent_patterns(transactions)
        >>> print(patterns)
    """

    def __init__(self, min_support: float = 0.5):
        self.min_support = min_support
        self.header_table: Dict[str, FPNode] = {}

    def _build_tree(self, transactions: List[List[str]]) -> FPNode:
        """Builds FP-tree from transactions"""
        # Count item frequencies
        item_counts = defaultdict(int)
        for transaction in transactions:
            for item in transaction:
                item_counts[item] += 1

        # Filter items below minimum support
        n_transactions = len(transactions)
        min_count = self.min_support * n_transactions
        frequent_items = {k: v for k, v in item_counts.items() if v >= min_count}

        # Create root node
        root = FPNode("null", 0)

        # Insert transactions into tree
        for transaction in transactions:
            # Sort and filter transaction items by frequency
            items = [item for item in transaction if item in frequent_items]
            items.sort(key=lambda x: (-frequent_items[x], x))

            current = root
            for item in items:
                if item not in current.children:
                    # Create new node
                    new_node = FPNode(item, 1, current)
                    current.children[item] = new_node

                    # Update header table
                    if item not in self.header_table:
                        self.header_table[item] = new_node
                    else:
                        # Link to existing nodes
                        node = self.header_table[item]
                        while node.next:
                            node = node.next
                        node.next = new_node
                else:
                    current.children[item].count += 1
                current = current.children[item]

        return root

    def find_frequent_patterns(
        self, transactions: List[List[str]]
    ) -> Dict[frozenset, int]:
        """
        Mines frequent patterns from transactions using FP-Growth algorithm

        Args:
            transactions: List of transactions where each transaction is a list of items

        Returns:
            Dictionary mapping frequent itemsets to their support counts
        """
        self.header_table.clear()
        tree = self._build_tree(transactions)

        patterns = {}
        for item in self.header_table:
            pattern = frozenset([item])
            patterns[pattern] = sum(node.count for node in self._get_prefix_path(item))

        return patterns

    def _get_prefix_path(self, item: str) -> List[FPNode]:
        """Returns all prefix paths for an item"""
        paths = []
        node = self.header_table[item]
        while node:
            paths.append(node)
            node = node.next
        return paths


if __name__ == "__main__":
    # Example usage
    transactions = [
        ["A", "B", "D"],
        ["B", "C"],
        ["A", "B", "C", "E"],
        ["B", "E"],
        ["A", "B", "C", "D"],
    ]

    fp_growth = FPGrowth(min_support=0.6)
    patterns = fp_growth.find_frequent_patterns(transactions)

    print("Frequent patterns:")
    for pattern, support in patterns.items():
        print(f"{list(pattern)}: {support}")
