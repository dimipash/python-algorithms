def gcd(a, b):
    """
    Compute the greatest common divisor of a and b using Euclidean algorithm.

    Time Complexity: O(log(min(a, b)))
    Space Complexity: O(1)
    """
    while b:
        a, b = b, a % b
    return a


def mod_inverse(a, m):
    """
    Find the modular inverse of a under modulo m using brute-force search.
    Returns None if the inverse does not exist.

    Time Complexity: O(m)
    Space Complexity: O(1)
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

    Time Complexity: O(n), where n is the length of plaintext
    Space Complexity: O(n)
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

    Time Complexity: O(n), where n is the length of ciphertext
    Space Complexity: O(n)
    """
    a_inv = mod_inverse(a, 26)
    if a_inv is None:
        return "Invalid 'a' value; must be coprime with 26."
    return "".join(
        chr(((a_inv * ((ord(char) - 65) - b)) % 26) + 65)
        for char in ciphertext.upper()
        if char.isalpha()
    )


def atbash_cipher(text):
    """
    Encrypts or decrypts text using the Atbash cipher.

    Parameters:
    text (str): The input text to be transformed.

    Time Complexity: O(n), where n is the length of text
    Space Complexity: O(n)
    """
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    reversed_alphabet = alphabet[::-1]
    translation_table = str.maketrans(alphabet, reversed_alphabet)
    return text.translate(translation_table)


def decimal_to_hexadecimal(n):
    """
    Converts a non-negative decimal integer to its hexadecimal representation.

    Parameters:
    n (int): The decimal number to convert.

    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    if not isinstance(n, int):
        return "Invalid input, please enter an integer."
    if n < 0:
        return "Invalid input, please enter a non-negative integer."
    return hex(n).replace("0x", "").upper()


def hexadecimal_to_decimal(hex_str):
    """
    Converts a hexadecimal string to its decimal representation.

    Parameters:
    hex_str (str): The hexadecimal string to convert.

    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    if not isinstance(hex_str, str):
        return "Invalid hexadecimal input."
    hex_str = hex_str.strip()
    if hex_str.lower().startswith("0x"):
        hex_str = hex_str[2:]
    try:
        return int(hex_str, 16)
    except ValueError:
        return "Invalid hexadecimal input."


if __name__ == "__main__":
    # Affine Cipher Example
    plaintext_affine = "HELLO"
    a, b = 5, 8  # 'a' must be coprime with 26
    ciphertext_affine = affine_encrypt(plaintext_affine, a, b)
    decrypted_text_affine = affine_decrypt(ciphertext_affine, a, b)
    print(f"Affine Ciphertext: {ciphertext_affine}")
    print(f"Affine Decrypted: {decrypted_text_affine}")

    # Atbash Cipher Example
    plaintext_atbash = "HELLO"
    ciphertext_atbash = atbash_cipher(plaintext_atbash)
    decrypted_text_atbash = atbash_cipher(ciphertext_atbash)
    print(f"Atbash Ciphertext: {ciphertext_atbash}")
    print(f"Atbash Decrypted: {decrypted_text_atbash}")

    # Base16 Conversion Example
    decimal_number = 419
    hexadecimal_number = "1A3"

    # Convert decimal to hexadecimal
    hex_result = decimal_to_hexadecimal(decimal_number)
    print(f"Decimal {decimal_number} to Hexadecimal: {hex_result}")

    # Convert hexadecimal to decimal
    dec_result = hexadecimal_to_decimal(hexadecimal_number)
    print(f"Hexadecimal {hexadecimal_number} to Decimal: {dec_result}")
