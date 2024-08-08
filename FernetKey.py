# from cryptography.fernet import Fernet
# from cryptography.fernet import Fernet

import os
import base64
from cryptography.hazmat.primitives import hashes
# from the hazardous materials module of the crypto library we have imported the hashes module
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
# again from that same package we have imported the  password based key derivation class the  the passw based key
# derivation hashed based message authentication function
from cryptography.hazmat.backends import default_backend


# the above default backend will be used as a parameter in the pass based key derivation function

# password=b'Oedipus'
# now we will form the salt
# it is a random 16 byte data
# the class below will generate the key from the given password in the constructor and return the URL-safe base64 encoded key
class KeyGenerator:
    def __init__(self, password):
        self.password = password

    def keygenerator(self):
        # salt = os.urandom(16)
        # print(salt)
        # key derivation function - cryptographic hash function
        # password based Key derivation function 2 hash-based message authentication
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=b"\x145\\b\xce\xad\xcdkwT:\x92\xd9\x90'\x1b",
            iterations=1000000,
            backend=default_backend()
        )
        # we can use this above instance of the kdf only once in the program
        # this function will derive the key from the given password as the parameter
        # key=kdf.derive(password)

        key = base64.urlsafe_b64encode(kdf.derive(self.password.encode()))
        return key


# fkey=KeyGenerator('Oedipus')
# key=fkey.keygenerator()
# print(key)

