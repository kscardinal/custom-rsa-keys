from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding

# ---------------------------
# Load keys once
# ---------------------------
def load_public_key(path="public_key.pem"):
    with open(path, "rb") as f:
        return serialization.load_pem_public_key(f.read())

def load_private_key(path="private_key.pem"):
    with open(path, "rb") as f:
        return serialization.load_pem_private_key(f.read(), password=None)

# ---------------------------
# Encryption / Decryption
# ---------------------------
def encrypt_message(message: bytes, public_key):
    """
    Encrypt a message (bytes) using the given public key.
    Returns ciphertext (bytes).
    """
    ciphertext = public_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return ciphertext

def decrypt_message(ciphertext: bytes, private_key):
    """
    Decrypt a ciphertext (bytes) using the given private key.
    Returns plaintext (bytes).
    """
    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return plaintext

# ---------------------------
# File helpers
# ---------------------------
def encrypt_file(input_path, output_path, public_key):
    with open(input_path, "rb") as f:
        message = f.read()
    ciphertext = encrypt_message(message, public_key)
    with open(output_path, "wb") as f:
        f.write(ciphertext)

def decrypt_file(input_path, output_path, private_key):
    with open(input_path, "rb") as f:
        ciphertext = f.read()
    plaintext = decrypt_message(ciphertext, private_key)
    with open(output_path, "wb") as f:
        f.write(plaintext)

# ---------------------------
# Example usage
# ---------------------------
if __name__ == "__main__":
    pub_key = load_public_key("public_key.pem")
    priv_key = load_private_key("private_key.pem")

    # Encrypt / decrypt strings
    message = b"This is an encryption test."
    ciphertext = encrypt_message(message, pub_key)
    print("Encrypted:", ciphertext)
    decrypted = decrypt_message(ciphertext, priv_key)
    print("Decrypted:", decrypted.decode())

    # Encrypt / decrypt files
    # encrypt_file("plain.txt", "encrypted.bin", pub_key)
    # decrypt_file("encrypted.bin", "decrypted.txt", priv_key)
