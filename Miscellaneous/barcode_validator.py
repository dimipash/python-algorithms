"""
Barcode Validator

Validates various barcode formats (UPC, EAN) by checking structure and
calculating checksums. Supports validation of:
- UPC-A (12 digits)
- EAN-13 (13 digits) 
- UPC-E (8 digits)

Time Complexity: O(n) where n is number of digits
Space Complexity: O(1) for fixed-size calculations
"""


def validate_upc(upc_code: str) -> bool:
    """
    Validate UPC-A barcode using standard checksum algorithm.

    Args:
        upc_code (str): 12-digit UPC code

    Returns:
        bool: True if valid UPC code

    Examples:
        >>> validate_upc("036000291452")
        True
        >>> validate_upc("036000291453")
        False
    """
    # Input validation
    if not upc_code.isdigit() or len(upc_code) != 12:
        return False

    # Calculate checksum
    odd_sum = sum(int(upc_code[i]) for i in range(0, 11, 2))
    even_sum = sum(int(upc_code[i]) for i in range(1, 11, 2))
    total = (odd_sum * 3) + even_sum

    # Verify check digit
    check_digit = (10 - (total % 10)) % 10
    return check_digit == int(upc_code[-1])


def validate_ean13(ean_code: str) -> bool:
    """
    Validate EAN-13 barcode.

    Args:
        ean_code (str): 13-digit EAN code

    Returns:
        bool: True if valid EAN-13 code
    """
    if not ean_code.isdigit() or len(ean_code) != 13:
        return False

    # EAN-13 uses alternating multipliers 1 and 3
    total = sum(int(d) * (3 if i % 2 else 1) for i, d in enumerate(ean_code[:-1]))
    check_digit = (10 - (total % 10)) % 10

    return check_digit == int(ean_code[-1])


def validate_upce(upce_code: str) -> bool:
    """
    Validate UPC-E (compressed 8-digit format).

    Args:
        upce_code (str): 8-digit UPC-E code

    Returns:
        bool: True if valid UPC-E code
    """
    if not upce_code.isdigit() or len(upce_code) != 8:
        return False

    # Convert to UPC-A for validation
    upca = expand_upce_to_upca(upce_code)
    return validate_upc(upca)


def expand_upce_to_upca(upce: str) -> str:
    """
    Convert UPC-E to UPC-A format.
    """
    # Expansion rules based on last digit
    manufacturer = ""
    product = ""
    last_digit = int(upce[6])

    if last_digit in [0, 1, 2]:
        manufacturer = upce[1:3] + str(last_digit) + "00"
        product = upce[3:6]
    elif last_digit == 3:
        manufacturer = upce[1:4]
        product = "00" + upce[4:6]
    elif last_digit == 4:
        manufacturer = upce[1:5]
        product = "0" + upce[5]
    else:
        manufacturer = upce[1:6]
        product = upce[6]

    return upce[0] + manufacturer + product + upce[7]


def main() -> None:
    """
    Demonstrate barcode validation with examples.
    """
    test_cases = {
        "UPC-A": ["036000291452", "036000291453"],
        "EAN-13": ["5901234123457", "5901234123458"],
        "UPC-E": ["01234565", "01234566"],
    }

    for format_name, codes in test_cases.items():
        print(f"\nTesting {format_name}:")
        for code in codes:
            if format_name == "UPC-A":
                result = validate_upc(code)
            elif format_name == "EAN-13":
                result = validate_ean13(code)
            else:
                result = validate_upce(code)
            print(f"{code}: {'Valid' if result else 'Invalid'}")


if __name__ == "__main__":
    main()
