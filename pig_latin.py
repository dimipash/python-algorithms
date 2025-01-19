def pig_latin_converter(sentence):
    """
    Converts English text to Pig Latin following these rules:
    - Words beginning with vowels: add 'way' to the end
    - Words beginning with consonants: move consonants before first vowel to end and add 'ay'
    - Words without vowels: add 'ay' to the end

    Time Complexity: O(n) where n is total length of sentence
    Space Complexity: O(n) for storing converted sentence

    Args:
        sentence (str): English text to convert

    Returns:
        str: Text converted to Pig Latin
    """

    def convert_word(word):
        vowels = "aeiouAEIOU"

        # Word starts with vowel
        if word[0] in vowels:
            return word + "way"

        # Word starts with consonant
        for index, letter in enumerate(word):
            if letter in vowels:
                return word[index:] + word[:index] + "ay"

        # Word has no vowels
        return word + "ay"

    # Convert each word and join back with spaces
    return " ".join(convert_word(word) for word in sentence.split())


# Example usage
if __name__ == "__main__":
    text = "I love programming in Python"
    pig_latin = pig_latin_converter(text)
    print(f"Original: {text}")
    print(f"Pig Latin: {pig_latin}")
