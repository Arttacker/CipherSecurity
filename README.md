
# CipherSecurity Framework

**CipherSecurity Framework** is a comprehensive assistant designed to help you solve cryptography challenges any CTF platform. It also serves as a library containing various implementations of cryptographic and mathematical algorithms.

## Features

- **Classic Encryption**: Implementations of Caesar cipher, Vigenère cipher, Hill cipher, Playfair cipher and more.
- **Modern Encryption**: DES, RSA, Deffie-Hellman key exchange, Elgamal encryption and other modern cryptographic algorithms.
- **Hashing**: MD5, SHA-1, SHA-256, and other hashing functions.
- **Encoding**: Base64, Hex, etc.
- **Digital Signatures**: RSA, DSA, Elgmal Digital Signature implementations.
- **Mathematical Algorithms**: Prime number generation, modular arithmetic, GCD, and more.
- **Tests**: Comprehensive tests for all implemented algorithms to ensure their correctness.

## Getting Started

### Prerequisites

Make sure you have Python 3.7+ installed on your system.

### Installation

Clone the repository:

```bash
git clone https://github.com/Arttacker/CipherSecurity.git
cd CryptoHack-Framework
```

Install the required packages:

```bash
pip install -r requirements.txt
```

### Usage

You can use the framework to solve cryptographic challenges or as a library in your own projects.

Example usage for a few different algorithms:
#### Classic Encryption Example: Caesar Cipher
```python
from encryption.classic import caesar

# Encrypt a message using Caesar Cipher
message = "HELLO WORLD"
shift = 3
encrypted_message = caesar.encrypt(message, shift)
print(f"Encrypted Message: {encrypted_message}")

# Decrypt a message using Caesar Cipher
decrypted_message = caesar.decrypt(encrypted_message, shift)
print(f"Decrypted Message: {decrypted_message}")

```

#### Mathematical Algorithm Example: Modular Inverse

```python
from math_algorithms.euclidean import mod_inv

# Calculate the modular inverse
a = 23
m = 26
mod_inv = mod_inv(a, m)
print(f"Modular Inverse of {a} mod {m} is {mod_inv}")

```


### Running Tests

To run the tests, use the following command:

```bash
pytest
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries, please reach out to [artacker404@gmail.com](mailto:artacker404@gmail.com).

---

Happy Hacking 😈!
