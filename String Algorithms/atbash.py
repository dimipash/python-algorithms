def atbash_cipher(text):
    """
    Encrypts or decrypts text using the Atbash cipher.

    Parameters:
    text (str): The input text to be transformed.

    Returns:
    str: The transformed text.
    """
    # Define the standard and reversed alphabets
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    reversed_alphabet = alphabet[::-1]  # Reverse the alphabet

    # Create a translation table for uppercase letters
    translation_table = str.maketrans(alphabet, reversed_alphabet)

    # Translate the input text using the translation table
    return text.translate(translation_table)


# Example usage
if __name__ == "__main__":
    plaintext = "HELLO"
    ciphertext = atbash_cipher(plaintext)  # SVOLL
    decrypted_text = atbash_cipher(ciphertext)  # HELLO
    print(f"Ciphertext: {ciphertext}")  # Ciphertext: SVOLL
    print(f"Decrypted: {decrypted_text}")  # Decrypted: HELLO
