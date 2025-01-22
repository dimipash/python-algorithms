"""
Credit Card Validator

Implements the Luhn algorithm to validate credit card numbers.
Supports major card types (Visa, Mastercard, Amex, Discover) and
performs both format and checksum validation.

Time Complexity: O(n) where n is number of digits
Space Complexity: O(n) for digit storage
"""

from typing import Dict, List


class CreditCardValidator:
    """Credit card validation using Luhn algorithm."""

    # Card type patterns
    CARD_PATTERNS: Dict[str, List[str]] = {
        "Visa": ["4"],
        "Mastercard": ["51", "52", "53", "54", "55"],
        "Amex": ["34", "37"],
        "Discover": ["6011"],
    }

    @staticmethod
    def luhn_check(card_number: str) -> bool:
        """
        Validate card number using Luhn algorithm.

        Args:
            card_number (str): Credit card number

        Returns:
            bool: True if valid according to Luhn algorithm
        """
        if not card_number.isdigit():
            return False

        # Convert to integers and reverse
        digits = [int(d) for d in card_number][::-1]

        # Double every second digit
        for i in range(1, len(digits), 2):
            digits[i] *= 2
            if digits[i] > 9:
                digits[i] -= 9

        # Check if sum is divisible by 10
        return sum(digits) % 10 == 0

    @classmethod
    def identify_card_type(cls, card_number: str) -> str:
        """
        Identify the credit card type based on prefix.

        Args:
            card_number (str): Credit card number

        Returns:
            str: Card type or 'Unknown'
        """
        for card_type, prefixes in cls.CARD_PATTERNS.items():
            if any(card_number.startswith(prefix) for prefix in prefixes):
                return card_type
        return "Unknown"

    @classmethod
    def validate_card(cls, card_number: str) -> tuple:
        """
        Perform complete card validation.

        Args:
            card_number (str): Credit card number

        Returns:
            tuple: (is_valid, card_type, error_message)
        """
        # Remove spaces and dashes
        card_number = card_number.replace(" ", "").replace("-", "")

        # Basic format check
        if not card_number.isdigit():
            return False, "Unknown", "Card number must contain only digits"

        # Length check
        if not (13 <= len(card_number) <= 19):
            return False, "Unknown", "Invalid card number length"

        # Identify card type
        card_type = cls.identify_card_type(card_number)

        # Luhn algorithm check
        if not cls.luhn_check(card_number):
            return False, card_type, "Failed Luhn check"

        return True, card_type, "Valid card number"


def main() -> None:
    """
    Demonstrate credit card validation with examples.
    """
    test_cards = [
        "4532015112830366",  # Valid Visa
        "6011514433546200",  # Valid Discover
        "4485680044297115",  # Valid Visa
        "1234567812345670",  # Invalid
        "378282246310005",  # Valid Amex
    ]

    validator = CreditCardValidator()

    for card in test_cards:
        is_valid, card_type, message = validator.validate_card(card)
        print(f"\nCard Number: {card}")
        print(f"Type: {card_type}")
        print(f"Valid: {is_valid}")
        print(f"Message: {message}")


if __name__ == "__main__":
    main()
