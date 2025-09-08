import pytest
from custom_rsa import generate_keys

def test_key_generation():
    public_key, private_key, (p, q) = generate_keys(1024)
    assert public_key is not None
    assert private_key is not None
    assert p != q  # p and q should be distinct primes
    assert public_key[1] == private_key[1]  # n should be the same in both keys
    assert public_key[0] == 65537  # e should be 65537
    assert private_key[0] > 0  # d should be positive
    assert p > 1 and q > 1  # p and q should be greater than 1
    assert (p - 1) * (q - 1) % public_key[0] != 0  # e and φ(n) should be coprime
    assert public_key[1].bit_length() == 1024  # n should be 1024 bits
    assert private_key[1].bit_length() == 1024  # n should be 1024 bits


test_key_generation()
