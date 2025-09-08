import pytest
from custom_rsa import load_public_key, load_private_key, encrypt_message, decrypt_message, generate_keys, save_keys_to_pem

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


def test_encryption_decryption():
    # Generate keys and save to PEM files
    public_key, private_key, (p, q) = generate_keys(1024)
    save_keys_to_pem(public_key, private_key, p, q)

    # Load key objects
    pub_key_obj = load_public_key("public_key.pem")
    priv_key_obj = load_private_key("private_key.pem")

    # Test message
    message = b"This is an encryption test."

    # Encrypt the message
    ciphertext = encrypt_message(message, pub_key_obj)
    assert ciphertext != message  # Ciphertext should differ from plaintext

    # Decrypt the message
    decrypted_message = decrypt_message(ciphertext, priv_key_obj)
    assert decrypted_message == message  # Decrypted message should match original

