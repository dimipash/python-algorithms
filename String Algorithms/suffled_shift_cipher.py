from typing import List
import random
import time


class ShuffledShiftCipher:
    """
    Implements Shuffled Shift Cipher - a polyalphabetic substitution cipher
    that combines character shifting with key shuffling for added security.

    Time Complexity: O(n) for encryption/decryption where n is text length
    Space Complexity: O(n) for key generation and text storage
    """

    @staticmethod
    def shuffle_key(key: str) -> str:
        """
        Shuffles characters in the key randomly.

        Time Complexity: O(n) where n is key length
        Space Complexity: O(n) for key list
        """
        key_list = list(key)
        random.shuffle(key_list)
        return "".join(key_list)

    @staticmethod
    def generate_key(plaintext: str, key: str) -> str:
        """
        Generates a key of same length as plaintext by repeating if necessary.

        Time Complexity: O(n) where n is plaintext length
        Space Complexity: O(n) for generated key
        """
        key = key.replace(" ", "").upper()
        if len(key) < len(plaintext):
            multiplier = len(plaintext) // len(key)
            remainder = len(plaintext) % len(key)
            key = key * multiplier + key[:remainder]
        return key[: len(plaintext)]

    def encrypt(self, plaintext: str, key: str) -> str:
        """
        Encrypts plaintext using shuffled shift cipher.

        Time Complexity: O(n) where n is plaintext length
        Space Complexity: O(n) for ciphertext
        """
        plaintext = plaintext.replace(" ", "").upper()
        key = self.generate_key(plaintext, key)
        ciphertext = []

        for i in range(len(plaintext)):
            shifted_key = self.shuffle_key(key)
            shift = (ord(plaintext[i]) - ord("A") + ord(shifted_key[i]) - ord("A")) % 26
            ciphertext.append(chr(shift + ord("A")))

        return "".join(ciphertext)

    def decrypt(self, ciphertext: str, key: str) -> str:
        """
        Decrypts ciphertext using shuffled shift cipher.

        Time Complexity: O(n) where n is ciphertext length
        Space Complexity: O(n) for plaintext
        """
        key = self.generate_key(ciphertext, key)
        plaintext = []

        for i in range(len(ciphertext)):
            shifted_key = self.shuffle_key(key)
            shift = (
                ord(ciphertext[i]) - ord("A") - (ord(shifted_key[i]) - ord("A")) + 26
            ) % 26
            plaintext.append(chr(shift + ord("A")))

        return "".join(plaintext)


def benchmark_cipher(cipher: ShuffledShiftCipher, text: str, key: str) -> None:
    """Measures encryption and decryption performance."""
    # Test encryption
    start = time.perf_counter()
    encrypted = cipher.encrypt(text, key)
    encrypt_time = time.perf_counter() - start

    # Test decryption
    start = time.perf_counter()
    decrypted = cipher.decrypt(encrypted, key)
    decrypt_time = time.perf_counter() - start

    print(f"Encryption time: {encrypt_time:.6f} seconds")
    print(f"Decryption time: {decrypt_time:.6f} seconds")


def main():
    cipher = ShuffledShiftCipher()

    test_cases = [
        ("MEET AT DAWN", "SECRETKEY", "Basic case"),
        ("HELLO WORLD", "KEY", "Short key"),
        ("ABC", "LONGKEY", "Short text"),
        ("", "KEY", "Empty text"),
        ("THISISALONGMESSAGE", "K", "Single char key"),
    ]

    for text, key, case_type in test_cases:
        print(f"\nTest case: {case_type}")
        print(f"Original text: {text}")
        print(f"Key: {key}")

        if text:
            encrypted = cipher.encrypt(text, key)
            decrypted = cipher.decrypt(encrypted, key)

            print(f"Encrypted: {encrypted}")
            print(f"Decrypted: {decrypted}")

            benchmark_cipher(cipher, text, key)


if __name__ == "__main__":
    main()
