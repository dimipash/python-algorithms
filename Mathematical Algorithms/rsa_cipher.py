from typing import Tuple, Optional
import time
from sympy import mod_inverse


class RSACipher:
    """
    Implements RSA (Rivest-Shamir-Adleman) public-key cryptosystem.

    RSA is an asymmetric cryptographic algorithm that uses a public key for encryption
    and a private key for decryption. It relies on the mathematical properties of large
    prime numbers and the difficulty of factoring their product.

    Time Complexity: O(log n) for encryption/decryption using square-and-multiply
    Space Complexity: O(1) for key storage
    """

    def __init__(self, p: int, q: int):
        """
        Initialize RSA cipher with two prime numbers.

        Time Complexity: O(log n) for modular inverse calculation
        Space Complexity: O(1)
        """
        self.public_key, self.private_key = self._generate_keys(p, q)

    def _generate_keys(self, p: int, q: int) -> Tuple[Tuple[int, int], Tuple[int, int]]:
        """
        Generates public and private key pairs.

        Args:
            p, q: Prime numbers

        Returns:
            Tuple of ((n,e), (n,d)) representing public and private keys
        """
        n = p * q
        phi = (p - 1) * (q - 1)
        e = 65537  # Common choice for public exponent
        d = mod_inverse(e, phi)
        return ((n, e), (n, d))

    def encrypt(self, plaintext: int) -> int:
        """
        Encrypts message using public key.

        Time Complexity: O(log n) using square-and-multiply
        Space Complexity: O(1)
        """
        n, e = self.public_key
        return pow(plaintext, e, n)

    def decrypt(self, ciphertext: int) -> int:
        """
        Decrypts message using private key.

        Time Complexity: O(log n) using square-and-multiply
        Space Complexity: O(1)
        """
        n, d = self.private_key
        return pow(ciphertext, d, n)


def benchmark_operations(cipher: RSACipher, message: int) -> None:
    """Measures performance of encryption and decryption."""
    # Test encryption
    start = time.perf_counter()
    encrypted = cipher.encrypt(message)
    encrypt_time = time.perf_counter() - start

    # Test decryption
    start = time.perf_counter()
    decrypted = cipher.decrypt(encrypted)
    decrypt_time = time.perf_counter() - start

    print(f"Encryption time: {encrypt_time:.6f} seconds")
    print(f"Decryption time: {decrypt_time:.6f} seconds")

    assert decrypted == message, "Encryption/decryption failed!"


def main():
    # Test cases
    test_cases = [
        (61, 53, 123),  # Small primes
        (61, 53, 456),  # Different message
        (61, 53, 1),  # Edge case
        (61, 53, 3000),  # Large message
    ]

    for p, q, message in test_cases:
        print(f"\nTest case: p={p}, q={q}, message={message}")

        # Initialize cipher
        cipher = RSACipher(p, q)

        # Show keys
        print(f"Public Key (n,e): {cipher.public_key}")
        print(f"Private Key (n,d): {cipher.private_key}")

        # Encrypt and decrypt
        encrypted = cipher.encrypt(message)
        decrypted = cipher.decrypt(encrypted)

        print(f"Original: {message}")
        print(f"Encrypted: {encrypted}")
        print(f"Decrypted: {decrypted}")

        # Benchmark
        benchmark_operations(cipher, message)


if __name__ == "__main__":
    main()
