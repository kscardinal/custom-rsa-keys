from icecream import ic
import secrets
import time
import os
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa


# Generate a random n-bit odd number
def random_n_bit_number(n_bits):
    return secrets.randbits(n_bits) | (1 << (n_bits - 1)) | 1


# Miller-Rabin primality test
def is_prime(n, k=40):
    # Check for small primes first
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False

    # Convert n-1 to d*2^r
    r, d = 0, n - 1
    while d % 2 == 0:
        d //= 2
        r += 1

    # Witness loop, repeat k times
    for _ in range(k):
        a = secrets.randbelow(n - 3) + 2 
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

# Generate a large prime number with n bits
def generate_large_prime(n_bits):
    while True:
        num = random_n_bit_number(n_bits)
        if is_prime(num):
            return num

# Compute gcd        
def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

# Choose public exponent e
def get_public_exponent(phi):
    # Default to 65537 if it's suitable
    e = 65537
    if gcd(e, phi) == 1:
        return e
    
    # Otherwise, find the smallest odd integer > 2 that is coprime with phi
    for e in range(3, phi, 2):
        if gcd(e, phi) == 1:
            return e
    
    # If all else fails, raise an error
    raise ValueError("Failed to find suitable public exponent")

# Extended Euclidean Algorithm
def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    # Base case
    if a == 0:
        return b, 0, 1
    # Recursive case
    gcd, x1, y1 = extended_gcd(b % a, a)
    #  Update x and y using results of recursive call
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

# Modular Inverse
def mod_inverse(e: int, phi: int) -> int:
    gcd, x, y = extended_gcd(e, phi)
    if gcd != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % phi

# Main function to generate RSA keys
def generate_keys(n_bits=1024):
    # Ensure n_bits is even
    if n_bits % 2 != 0:
        raise ValueError("Number of bits must be even")
    
    # Generate two distinct large primes p and q
    while True:
        p = generate_large_prime(n_bits // 2)
        q = generate_large_prime(n_bits // 2)
        
        # Ensure p and q are distinct
        while p == q:
            q = generate_large_prime(n_bits // 2)

        # Calculate n and φ(n)
        n = p * q
        phi = (p - 1) * (q - 1)

        # Choose public exponent e and check length of n
        e = 65537
        if gcd(e, phi) == 1 and n.bit_length() == n_bits:
            break

    d = mod_inverse(e, phi)

    return (e, n), (d, n), (p, q)

# Save keys to PEM files
def save_keys_to_pem(public_key, private_key, p, q):
    e, n = public_key
    d, _ = private_key

    # Calculate CRT parameters for efficiency
    dmp1 = d % (p - 1)
    dmq1 = d % (q - 1)
    iqmp = pow(q, -1, p)

    private_numbers = rsa.RSAPrivateNumbers(
        p=p,
        q=q,
        d=d,
        dmp1=dmp1,
        dmq1=dmq1,
        iqmp=iqmp,
        public_numbers=rsa.RSAPublicNumbers(e=e, n=n)
    )

    # Build private key object
    private_key_obj = private_numbers.private_key()

    # Export private key PEM
    with open("private_key.pem", "wb") as f:
        f.write(private_key_obj.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        ))

    # Export public key PEM
    public_key_obj = private_key_obj.public_key()
    with open("public_key.pem", "wb") as f:
        f.write(public_key_obj.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))


# Example usage
time_start = time.time()
public_key, private_key, (p, q) = generate_keys(1024)
time_end = time.time()
print(f"Key generation took {time_end - time_start:.2f} seconds")

# Save PEM files
save_keys_to_pem(public_key, private_key, p, q)
print("Keys saved to private_key.pem and public_key.pem")


