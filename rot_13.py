from typing import List, Tuple
import time


class ROT13:
    """
    Implements ROT13 cipher - a special case of Caesar cipher that rotates letters by 13 positions.

    ROT13 is a simple substitution cipher that replaces each letter with the letter 13 positions
    after it in the alphabet. Since the English alphabet has 26 letters, applying ROT13 twice
    returns the original text, making it a reciprocal cipher.

    Time Complexity: O(n) where n is text length
    Space Complexity: O(n) for output string
    """

    @staticmethod
    def encrypt(text: str) -> str:
        """
        Encrypts text using ROT13.

        Time Complexity: O(n) where n is text length
        Space Complexity: O(n) for result string
        """
        result = []
        for char in text:
            if "A" <= char <= "Z":
                # Rotate uppercase letters
                result.append(chr((ord(char) - ord("A") + 13) % 26 + ord("A")))
            elif "a" <= char <= "z":
                # Rotate lowercase letters
                result.append(chr((ord(char) - ord("a") + 13) % 26 + ord("a")))
            else:
                # Preserve non-alphabetic characters
                result.append(char)
        return "".join(result)

    @staticmethod
    def decrypt(text: str) -> str:
        """
        Decrypts ROT13 text (same as encrypt due to reciprocal property).
        """
        return ROT13.encrypt(text)

    @staticmethod
    def test_cases() -> List[Tuple[str, str, str]]:
        """Runs test cases and returns results."""
        tests = [
            "HELLO WORLD",
            "abcdefghijklmnopqrstuvwxyz",
            "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
            "12345!@#$%",
            "",
            "ROT13 test 123!",
        ]

        results = []
        for text in tests:
            encrypted = ROT13.encrypt(text)
            decrypted = ROT13.decrypt(encrypted)
            results.append((text, encrypted, decrypted))
        return results


def main():
    cipher = ROT13()

    # Run test cases
    print("Testing ROT13 cipher:")
    for original, encrypted, decrypted in cipher.test_cases():
        print(f"\nOriginal : {original}")

        # Time encryption
        start = time.perf_counter()
        test_encrypted = cipher.encrypt(original)
        encrypt_time = time.perf_counter() - start

        print(f"Encrypted: {encrypted}")
        print(f"Decrypted: {decrypted}")
        print(f"Encryption time: {encrypt_time:.6f} seconds")

        # Verify results
        assert encrypted == test_encrypted, "Encryption failed!"
        assert decrypted == original, "Decryption failed!"
        assert (
            cipher.encrypt(cipher.encrypt(original)) == original
        ), "Double encryption failed!"


if __name__ == "__main__":
    main()
