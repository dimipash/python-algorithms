def apriori(transactions: list[set], min_support: float) -> list[set]:
    """
    Implements the Apriori algorithm to find frequent itemsets in transaction data.

    Time Complexity: O(2^n * m) where n is number of unique items and m is number of transactions
    Space Complexity: O(2^n) to store all possible itemsets

    Args:
        transactions: List of transactions where each transaction is a set of items
        min_support: Minimum support threshold (0 to 1)

    Returns:
        List of sets containing frequent itemsets at each level k

    Example:
        >>> transactions = [
        ...     {'milk', 'bread', 'diapers'},
        ...     {'bread', 'butter'},
        ...     {'milk', 'diapers', 'bread', 'butter'},
        ...     {'milk', 'bread'},
        ...     {'diapers', 'bread'}
        ... ]
        >>> apriori(transactions, 0.4)
        [{'bread'}, {'milk', 'diapers'}, {'bread', 'milk'}, {'bread', 'diapers'}]
    """
    # Count frequency of individual items
    item_counts = defaultdict(int)
    n_transactions = len(transactions)

    for transaction in transactions:
        for item in transaction:
            item_counts[frozenset([item])] += 1

    # Find frequent 1-itemsets that meet min_support
    frequent_items = {
        item
        for item, count in item_counts.items()
        if count / n_transactions >= min_support
    }

    k = 2  # Start with 2-itemsets
    frequent_itemsets = [frequent_items]

    while frequent_items:
        # Generate candidate k-itemsets
        candidates = set()
        for item1 in frequent_items:
            for item2 in frequent_items:
                union = item1.union(item2)
                if len(union) == k:
                    candidates.add(union)

        # Count support for candidates
        item_counts = defaultdict(int)
        for transaction in transactions:
            for candidate in candidates:
                if candidate.issubset(transaction):
                    item_counts[candidate] += 1

        # Filter by min_support
        frequent_items = {
            itemset
            for itemset, count in item_counts.items()
            if count / n_transactions >= min_support
        }

        if frequent_items:
            frequent_itemsets.append(frequent_items)
        k += 1

    return frequent_itemsets
