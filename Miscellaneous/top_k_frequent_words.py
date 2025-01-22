from collections import Counter


def top_k_frequent_words(words, k):
    """
    Finds the top K frequent words in a list of words.

    Parameters:
    words (list of str): The list of words to analyze.
    k (int): The number of top frequent words to return.

    Returns:
    list of str: A list containing the top K frequent words.

    Time Complexity: O(N log K), where N is the number of words.
    Space Complexity: O(N), where N is the number of words.
    """
    # Count the frequency of each word
    count = Counter(words)
    # Get the K most common words as list of tuples (word, frequency)
    most_common = count.most_common(k)
    # Extract and return only the words
    return [word for word, _ in most_common]


# Example usage
if __name__ == "__main__":
    words = ["the", "day", "is", "sunny", "the", "the", "day", "is", "is"]
    k = 2
    top_words = top_k_frequent_words(words, k)
    print("Top K Frequent Words:", top_words)
