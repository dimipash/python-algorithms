def gcd(a, b):
    """
    Compute the greatest common divisor of a and b using Euclidean algorithm.
    """
    while b:
        a, b = b, a % b
    return a


def mod_inverse(a, m):
    """
    Find the modular inverse of a under modulo m using brute-force search.
    Returns None if the inverse does not exist.
    """
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None


def affine_encrypt(plaintext, a, b):
    """
    Encrypt plaintext using the Affine cipher.

    Parameters:
        plaintext (str): The input text to encrypt.
        a (int): The multiplicative key, must be coprime with 26.
        b (int): The additive key.

    Returns:
        str: The encrypted ciphertext.
    """
    return "".join(
        chr(((a * (ord(char) - 65) + b) % 26) + 65)
        for char in plaintext.upper()
        if char.isalpha()
    )


def affine_decrypt(ciphertext, a, b):
    """
    Decrypt ciphertext using the Affine cipher.

    Parameters:
        ciphertext (str): The encrypted text to decrypt.
        a (int): The multiplicative key, must be coprime with 26.
        b (int): The additive key.

    Returns:
        str: The decrypted plaintext or an error message if 'a' is invalid.
    """
    a_inv = mod_inverse(a, 26)
    if a_inv is None:
        return "Invalid 'a' value; must be coprime with 26."
    return "".join(
        chr(((a_inv * ((ord(char) - 65) - b)) % 26) + 65)
        for char in ciphertext.upper()
        if char.isalpha()
    )


# Example usage
if __name__ == "__main__":
    plaintext = "HELLO"
    a, b = 5, 8  # 'a' must be coprime with 26
    ciphertext = affine_encrypt(plaintext, a, b)
    decrypted_text = affine_decrypt(ciphertext, a, b)
    print(f"Ciphertext: {ciphertext}")
    print(f"Decrypted: {decrypted_text}")
