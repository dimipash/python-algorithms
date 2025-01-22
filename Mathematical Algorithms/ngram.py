def generate_ngrams(text, n):
    """
    Generates n-grams from input text by creating sequences of n consecutive words.

    Time Complexity: O(m) where m is number of words in text
    Space Complexity: O(m-n+1) for storing n-grams

    Args:
        text (str): Input text to generate n-grams from
        n (int): Size of each n-gram sequence

    Returns:
        list: List of tuples containing n-gram sequences
    """
    # Split text into words
    tokens = text.split()
    ngrams = []

    # Generate n-grams by sliding window of size n
    for i in range(len(tokens) - n + 1):
        # Create tuple of n consecutive tokens
        ngram = tuple(tokens[i : i + n])
        ngrams.append(ngram)

    return ngrams


# Example usage
if __name__ == "__main__":
    text = "I love natural language processing"

    # Generate bigrams (n=2)
    bigrams = generate_ngrams(text, 2)
    print(f"Bigrams: {bigrams}")

    # Generate trigrams (n=3)
    trigrams = generate_ngrams(text, 3)
    print(f"Trigrams: {trigrams}")
