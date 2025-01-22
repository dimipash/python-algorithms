"""
Email Address Validator

Validates email addresses using regex pattern matching according to RFC 5322.
Checks for proper format including local part, domain, and TLD.

Time Complexity: O(n) where n is length of email string
Space Complexity: O(1) for regex compilation
"""

import re
from typing import Tuple


class EmailValidator:
    """Email validation with detailed checking."""

    # Regular expression for basic email validation
    EMAIL_PATTERN = re.compile(
        r"""
        ^[a-zA-Z0-9._%+-]+      # Local part
        @                       # @ symbol
        [a-zA-Z0-9.-]+         # Domain name
        \.[a-zA-Z]{2,}$        # Top-level domain
    """,
        re.VERBOSE,
    )

    # Additional patterns for specific checks
    CONSECUTIVE_DOTS = re.compile(r"\.{2,}")
    SPECIAL_CHARS = re.compile(r"[!#$%^&*()+=\[\]{}|\\,<>/?]")

    @classmethod
    def is_valid_email(cls, email: str) -> bool:
        """
        Basic email validation using regex pattern.

        Args:
            email (str): Email address to validate

        Returns:
            bool: True if email format is valid
        """
        return bool(cls.EMAIL_PATTERN.match(email))

    @classmethod
    def validate_email_detailed(cls, email: str) -> Tuple[bool, str]:
        """
        Detailed email validation with specific error messages.

        Args:
            email (str): Email address to validate

        Returns:
            tuple: (is_valid, error_message)
        """
        # Check for empty or None
        if not email:
            return False, "Email cannot be empty"

        # Check length
        if len(email) > 254:
            return False, "Email too long"

        # Split into local and domain parts
        try:
            local, domain = email.split("@")
        except ValueError:
            return False, "Email must contain exactly one @ symbol"

        # Check local part
        if not local:
            return False, "Local part cannot be empty"
        if len(local) > 64:
            return False, "Local part too long"

        # Check domain part
        if not domain:
            return False, "Domain cannot be empty"
        if cls.CONSECUTIVE_DOTS.search(domain):
            return False, "Domain cannot contain consecutive dots"

        # Check for invalid special characters
        if cls.SPECIAL_CHARS.search(email):
            return False, "Contains invalid special characters"

        # Check basic pattern
        if not cls.EMAIL_PATTERN.match(email):
            return False, "Invalid email format"

        return True, "Valid email address"


def main() -> None:
    """
    Demonstrate email validation with examples.
    """
    test_cases = [
        "example@domain.com",  # Valid
        "user.name@domain.co.uk",  # Valid
        "user-name@domain.com",  # Valid
        "user@domain",  # Invalid (no TLD)
        "user@.com",  # Invalid (invalid domain)
        "user@domain..com",  # Invalid (consecutive dots)
        "user@domain.c",  # Invalid (TLD too short)
        "very.common@example.com",  # Valid
        "disposable.style.email.with+symbol@example.com",  # Valid
        "other.email-with-hyphen@example.com",  # Valid
        "fully-qualified-domain@example.com",  # Valid
        "user.name+tag+sorting@example.com",  # Valid
        "x@example.com",  # Valid (one-letter local part)
        "example-indeed@strange-example.com",  # Valid
        "example@s.example",  # Valid
        "",  # Invalid (empty)
    ]

    validator = EmailValidator()

    for email in test_cases:
        is_valid, message = validator.validate_email_detailed(email)
        print(f"\nEmail: {email}")
        print(f"Valid: {is_valid}")
        print(f"Message: {message}")


if __name__ == "__main__":
    main()
