import math
import random
from icecream import ic

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Bounding the range for prime number generation
prime_lower_bound = 50000
prime_upper_bound = 1500000

# Generate a list of prime numbers within the specified range
primes = [n for n in range(prime_lower_bound, prime_upper_bound) if is_prime(n)]

# Randomly select two distinct prime numbers
p = random.choice(primes)
primes.remove(p)
q = random.choice(primes)

# Calculate n and φ(n)
n = p * q
phi = (p - 1) * (q - 1)


def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

def e(phi: int) -> int:
    if phi > 65357:
        e = 65537
    elif phi > 257:
        e = 257
    while e < phi:
        if gcd(e, phi) == 1:
            return e
        e += 2
    print("Failed to find e")

e_value = e(phi)

def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def mod_inverse(e: int, phi: int) -> int:
    gcd, x, y = extended_gcd(e, phi)
    if gcd != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % phi

d = mod_inverse(e_value, phi)
ic(p, q, n, phi, e_value, d)

public_key = (e_value, n)
private_key = (d, n)
ic(public_key, private_key)

def convert_to_int(message: str) -> int:
    return int.from_bytes(message.encode('utf-8'), 'big')

def convert_to_str(message_int: int) -> str:
    byte_length = (message_int.bit_length() + 7) // 8
    return message_int.to_bytes(byte_length, 'big').decode('utf-8', errors='ignore')

def encrypt(message: str, public_key: tuple[int, int]) -> int:
    e, n = public_key
    message_int = convert_to_int(message)
    if message_int >= n:
        raise ValueError("Message is too long for the key size.")
    cipher_int = pow(message_int, e, n)
    return cipher_int

def decrypt(cipher_int: int, private_key: tuple[int, int]) -> str:
    d, n = private_key
    message_int = pow(cipher_int, d, n)
    message = convert_to_str(message_int)
    return message

# Example usage
message = "12345"
ic(message)
ic(convert_to_int(message))
ciphertext = encrypt(message, public_key)
ic(ciphertext)
decrypted_message = decrypt(ciphertext, private_key)
ic(decrypted_message)
