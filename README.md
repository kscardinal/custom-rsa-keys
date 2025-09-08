# 🔒 Custom RSA Keys
`custom-rsa-keys` is a python utility providing custom RSA key generation used for encrypting and decrypting secure data.


![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Version](https://img.shields.io/badge/Version-1.0.0-green)
![GitHub commit activity](https://img.shields.io/github/commit-activity/t/kscardinal/custom-rsa-keys)
![GitHub last commit](https://img.shields.io/github/last-commit/kscardinal/custom-rsa-keys)
![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/kscardinal/custom-rsa-keys/python-tests.yml?label=Encryption%2FDecryption%20Testing)


---

## Table of Contents  
- [Overview](#Overview)
- [Features](#features)
- [Tech Stack](#Tech-Stack)
- [Project Structure](#project-structure)
- [Setup](#setup)
- [Usage](#usage)
- [Security Features](#security-features)
- [License](#License)

---

## Overview  

`custom-rsa-keys` is a project enables users to generate custom RSA key pairs and perform encryption and decryption operations using those keys. It includes scripts for creating secure private and public keys, as well as utilities for encrypting and decrypting data with RSA. 

---

## Features  

- Custom RSA key length selection for enhanced security
- Data encryption and decryption using generated RSA keys
- Generation of secure private and public key files
- Easy-to-use Python scripts for key management and cryptographic operations
- Example usage and demonstration module for quick integration
- Support for standard cryptographic libraries to ensure reliability and compatibility

---

## Tech Stack  

- **Frontend**: Python 
- **Backend**: Python
- **Database**: N/A
- **Other Tools**: secrets, cryptography  

---

## Project Structure

- custom-rsa-keys/
- ├── src/
- ├ ‎ ├── custom_rsa/
- ├ ‎ ‎ ‎ ‎ ├── [`__init__.py`](__init__.py)
- ├ ‎ ‎ ‎ ‎ ├── [`rsa_encryption.py`](rsa_encryption.py)
- ├ ‎ ‎ ‎ ‎ ├── [`rsa_generation.py`](rsa_generation.py)
- ├── tests/
- ├‎ ‎ ├── [`encryption_test.py`](encryption_test.py)
- └‎ ‎ ├── [`generation_test.py`](generation_test.py)


---

## Setup

1. **Install uv**
	Download and install [uv](https://github.com/astral-sh/uv) from the official repository or use:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
uv self update
uv python install 3.13
```

2. **Create a virtual environment**
```bash
uv venv
```

3. **Install dependencies**
```bash
uv pip install -e .
```

---

## Usage

1. Start the server:
```python
python rsa-generation.py
```
2. Double check key creation
3. Encrypt / Decrypt Messages
```python
python rsa-encryption.py
```
4. Example Usage (Encrypt / Decrypt Files):
```python
encrypt_file("{plain.txt}", "{encrypted.bin}", {public_key})
decrypt_file("{encrypted.bin}", "{decrypted.txt}", {private_key})
```

---

## Security Features

- Uses strong RSA encryption for data confidentiality
- Employs OAEP padding with SHA-256 for secure encryption and decryption
- Separates private and public key files to prevent unauthorized access
- Loads keys from files, supporting secure key storage practices
- Utilizes standard cryptographic libraries to avoid custom, error-prone implementations
- Supports custom key lengths for adjustable security levels

---

## License

This project is licensed under the MIT License, which means you are free to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the software, as long as you include the original copyright and license notice in any copy of the software. The software is provided "as is," without warranty of any kind.


