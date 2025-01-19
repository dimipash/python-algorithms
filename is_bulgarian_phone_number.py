"""
Bulgarian Phone Number Validator

Validates phone numbers according to Bulgarian standards:
- 10 digits for local format
- Starts with 0
- Mobile numbers start with 08 or 09
- Supports both mobile and landline formats

Time Complexity: O(1) - constant time string operations
Space Complexity: O(1) - constant space used
"""


def is_valid_bulgarian_phone_number(phone_number: str) -> bool:
    """
    Validate Bulgarian phone number format.

    Args:
        phone_number (str): Phone number to validate

    Returns:
        bool: True if valid Bulgarian phone number

    Examples:
        >>> is_valid_bulgarian_phone_number("0812345678")
        True
        >>> is_valid_bulgarian_phone_number("0712345678")
        False
    """
    # Remove spaces and dashes
    number = phone_number.replace(" ", "").replace("-", "")

    # Handle international format
    if number.startswith("+359"):
        number = "0" + number[4:]

    # Basic validations
    if len(number) != 10:
        return False

    if not (number.startswith("0") and number.isdigit()):
        return False

    # Check second digit for mobile numbers
    if number[1] not in ["8", "9"]:
        return False

    return True


def validate_phone_number_with_details(phone_number: str) -> tuple:
    """
    Validate phone number with detailed error reporting.

    Args:
        phone_number (str): Phone number to validate

    Returns:
        tuple: (is_valid, error_message)
    """
    # Remove formatting
    number = phone_number.replace(" ", "").replace("-", "")

    # Handle international format
    if number.startswith("+359"):
        number = "0" + number[4:]

    # Check length
    if len(number) != 10:
        return False, "Phone number must be 10 digits"

    # Check if numeric
    if not number.isdigit():
        return False, "Phone number must contain only digits"

    # Check prefix
    if not number.startswith("0"):
        return False, "Phone number must start with 0"

    # Check mobile prefix
    if number[1] not in ["8", "9"]:
        return False, "Second digit must be 8 or 9"

    return True, "Valid Bulgarian phone number"


def main() -> None:
    """
    Demonstrate phone number validation with examples.
    """
    test_cases = [
        "0812345678",  # Valid mobile number
        "0912345678",  # Valid mobile number
        "0712345678",  # Invalid (wrong second digit)
        "1234567890",  # Invalid (wrong prefix)
        "0812345ABC",  # Invalid (non-numeric)
        "+35988888888",  # Valid international format
    ]

    for number in test_cases:
        is_valid, message = validate_phone_number_with_details(number)
        print(f"\nNumber: {number}")
        print(f"Valid: {is_valid}")
        print(f"Message: {message}")


if __name__ == "__main__":
    main()
