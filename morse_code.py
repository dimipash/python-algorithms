from typing import Dict, Optional
import time


class MorseCode:
    """
    Implements Morse Code encoding and decoding.

    Morse Code is a method of encoding text characters using dots (.) and dashes (-).
    Developed in the 1830s-1840s by Samuel Morse and Alfred Vail for telegraph communication.
    Each letter and number is represented by a unique sequence of dots and dashes.

    Time Complexity: O(n) for encoding and decoding
    Space Complexity: O(1) for dictionaries, O(n) for message storage
    """

    def __init__(self):
        # Space: O(1) - fixed size dictionary
        self.morse_dict = {
            "A": ".-",
            "B": "-...",
            "C": "-.-.",
            "D": "-..",
            "E": ".",
            "F": "..-.",
            "G": "--.",
            "H": "....",
            "I": "..",
            "J": ".---",
            "K": "-.-",
            "L": ".-..",
            "M": "--",
            "N": "-.",
            "O": "---",
            "P": ".--.",
            "Q": "--.-",
            "R": ".-.",
            "S": "...",
            "T": "-",
            "U": "..-",
            "V": "...-",
            "W": ".--",
            "X": "-..-",
            "Y": "-.--",
            "Z": "--..",
            "1": ".----",
            "2": "..---",
            "3": "...--",
            "4": "....-",
            "5": ".....",
            "6": "-....",
            "7": "--...",
            "8": "---..",
            "9": "----.",
            "0": "-----",
            " ": " ",
        }
        # Create reverse mapping for decoding
        self.reverse_dict = {v: k for k, v in self.morse_dict.items()}

    def encode(self, message: str) -> str:
        """
        Encodes text to Morse code.

        Time Complexity: O(n) where n is message length
        Space Complexity: O(n) for result string
        """
        if not message:
            return ""

        return " ".join(self.morse_dict.get(char.upper(), "") for char in message)

    def decode(self, morse_code: str) -> str:
        """
        Decodes Morse code to text.

        Time Complexity: O(n) where n is code length
        Space Complexity: O(n) for result string
        """
        if not morse_code:
            return ""

        return "".join(self.reverse_dict.get(code, "") for code in morse_code.split())

    @staticmethod
    def validate_morse(code: str) -> bool:
        """
        Validates if string contains only valid Morse code characters.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        return all(c in (".", "-", " ") for c in code)


def benchmark_encoding(morse: MorseCode, message: str, iterations: int = 1000) -> float:
    """Measures average encoding time over multiple iterations."""
    start = time.perf_counter()
    for _ in range(iterations):
        morse.encode(message)
    return (time.perf_counter() - start) / iterations


def main():
    morse = MorseCode()

    # Test cases
    test_messages = [
        "HELLO WORLD",
        "SOS",
        "12345",
        "MORSE CODE IS AWESOME",
        "",  # Empty string
    ]

    for message in test_messages:
        print(f"\nOriginal message: {message}")

        # Encode
        encoded = morse.encode(message)
        print(f"Encoded: {encoded}")

        # Validate Morse code
        if encoded:
            is_valid = MorseCode.validate_morse(encoded)
            print(f"Valid Morse code: {is_valid}")

        # Decode
        decoded = morse.decode(encoded)
        print(f"Decoded: {decoded}")

        # Performance benchmark
        avg_time = benchmark_encoding(morse, message)
        print(f"Average encoding time: {avg_time:.8f} seconds")

        # Verify
        assert message == decoded, "Encoding/decoding failed!"


if __name__ == "__main__":
    main()
