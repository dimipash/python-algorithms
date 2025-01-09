from typing import Dict, List
import string
import time


class CaesarCipher:
    """
    Implements the Caesar Cipher encryption and decryption.
    Space Complexity: O(1) - stores fixed-size mapping dictionaries
    """

    def __init__(self):
        # Space: O(1) - maximum 26 shifts possible
        self.upper_map: Dict[int, Dict[str, str]] = {}
        self.lower_map: Dict[int, Dict[str, str]] = {}

    def _create_shift_map(self, shift: int) -> None:
        """
        Creates mapping dictionaries for given shift if not already cached.
        Time Complexity: O(1) - operates on fixed alphabet size
        Space Complexity: O(1) - fixed size mappings
        """
        if shift not in self.upper_map:
            # Create uppercase mapping
            self.upper_map[shift] = str.maketrans(
                string.ascii_uppercase,
                string.ascii_uppercase[shift:] + string.ascii_uppercase[:shift],
            )

            # Create lowercase mapping
            self.lower_map[shift] = str.maketrans(
                string.ascii_lowercase,
                string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift],
            )

    def encrypt(self, plaintext: str, shift: int) -> str:
        """
        Encrypts text using Caesar cipher.

        Time Complexity: O(n) where n is length of plaintext
        Space Complexity: O(n) for result string

        Args:
            plaintext: Text to encrypt
            shift: Number of positions to shift

        Returns:
            Encrypted text
        """
        shift = shift % 26  # Normalize shift value
        self._create_shift_map(shift)

        result = []
        for char in plaintext:  # O(n) iteration
            if char.isupper():
                result.append(char.translate(self.upper_map[shift]))
            elif char.islower():
                result.append(char.translate(self.lower_map[shift]))
            else:
                result.append(char)

        return "".join(result)  # O(n) join operation

    def decrypt(self, ciphertext: str, shift: int) -> str:
        """
        Decrypts text by shifting in opposite direction.
        Time & Space Complexity: Same as encrypt()
        """
        return self.encrypt(ciphertext, -shift)

    def crack(self, ciphertext: str) -> List[tuple[int, str]]:
        """
        Attempts to crack cipher by trying all possible shifts.
        Time Complexity: O(26n) = O(n) where n is length of ciphertext
        Space Complexity: O(26n) = O(n) to store all possible solutions
        """
        return [(shift, self.decrypt(ciphertext, shift)) for shift in range(26)]


def analyze_frequency(text: str) -> Dict[str, float]:
    """
    Analyzes letter frequency in text.
    Time Complexity: O(n) where n is length of text
    Space Complexity: O(1) - fixed size alphabet
    """
    total = sum(c.isalpha() for c in text)  # O(n)
    if total == 0:
        return {}

    frequency = {}
    for char in text.upper():  # O(n)
        if char.isalpha():
            frequency[char] = frequency.get(char, 0) + 1

    return {char: count / total for char, count in frequency.items()}  # O(1)


def main():
    cipher = CaesarCipher()

    # Test cases
    test_cases = [
        ("HELLO, WORLD!", 3),
        ("The quick brown fox jumps over the lazy dog.", 7),
        ("CAESAR CIPHER", 13),
        ("123!@#", 5),  # Non-alphabetic characters
        ("", 1),  # Empty string
    ]

    for text, shift in test_cases:
        print(f"\nOriginal text: {text}")
        print(f"Shift: {shift}")

        # Measure encryption time
        start = time.perf_counter()
        encrypted = cipher.encrypt(text, shift)
        encrypt_time = time.perf_counter() - start

        print(f"Encrypted: {encrypted}")
        print(f"Encryption time: {encrypt_time:.6f} seconds")

        # Verify decryption
        decrypted = cipher.decrypt(encrypted, shift)
        print(f"Decrypted: {decrypted}")
        assert text == decrypted, "Decryption failed!"

        # Show frequency analysis for non-empty text
        if text:
            freq = analyze_frequency(encrypted)
            print("\nLetter frequencies in encrypted text:")
            for char, frequency in sorted(freq.items()):
                print(f"{char}: {frequency:.3f}")

        # Demonstrate cracking for short texts
        if len(text) <= 20:
            print("\nAttempting to crack:")
            possible_solutions = cipher.crack(encrypted)
            for shift, solution in possible_solutions[:5]:
                print(f"Shift {shift}: {solution}")


if __name__ == "__main__":
    main()
