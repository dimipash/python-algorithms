from typing import Tuple
import random
from sympy import isprime, mod_inverse


class RSAKeyGenerator:
    """
    Implements secure RSA key generation using large prime numbers.

    RSA security relies on the computational difficulty of factoring the product
    of two large prime numbers. This implementation generates keys using random
    prime numbers of specified bit length.

    Time Complexity: O(k^4) for k-bit prime generation
    Space Complexity: O(k) for k-bit numbers
    """

    @staticmethod
    def generate_prime_candidate(length: int) -> int:
        """
        Generates an odd number of specified bit length.

        Time Complexity: O(1)
        Space Complexity: O(k) for k-bit number
        """
        # Generate random bits
        p = random.getrandbits(length)
        # Set MSB and LSB to 1 to ensure odd number of correct length
        p |= (1 << length - 1) | 1
        return p

    @staticmethod
    def generate_prime_number(length: int) -> int:
        """
        Generates a prime number of specified bit length.

        Time Complexity: O(k^4) for k-bit prime
        Space Complexity: O(k)
        """
        p = 4  # Start with non-prime
        while not isprime(p):
            p = RSAKeyGenerator.generate_prime_candidate(length)
        return p

    @classmethod
    def generate_keys(cls, bits: int) -> Tuple[Tuple[int, int], Tuple[int, int]]:
        """
        Generates RSA public and private key pairs.

        Args:
            bits: Bit length for prime numbers (recommended >= 2048)

        Returns:
            Tuple of ((n,e), (n,d)) for public and private keys

        Time Complexity: O(k^4) for k-bit keys
        Space Complexity: O(k)
        """
        # Generate distinct primes
        p = cls.generate_prime_number(bits)
        q = cls.generate_prime_number(bits)
        while p == q:
            q = cls.generate_prime_number(bits)

        # Calculate key components
        n = p * q
        phi = (p - 1) * (q - 1)
        e = 65537  # Commonly used public exponent
        d = mod_inverse(e, phi)

        return ((n, e), (n, d))


def main():
    # Use at least 2048 bits for security in production
    bit_lengths = [512, 1024]  # Example bit lengths

    for bits in bit_lengths:
        print(f"\nGenerating {bits}-bit RSA keys:")

        # Time the key generation
        import time

        start = time.perf_counter()

        try:
            public_key, private_key = RSAKeyGenerator.generate_keys(bits)
            duration = time.perf_counter() - start

            print(f"Time taken: {duration:.2f} seconds")
            print(f"Public Key (n,e):")
            print(f"n = {public_key[0]}")
            print(f"e = {public_key[1]}")
            print(f"Private Key (n,d):")
            print(f"n = {private_key[0]}")
            print(f"d = {private_key[1]}")

        except Exception as e:
            print(f"Error generating keys: {e}")


if __name__ == "__main__":
    main()
