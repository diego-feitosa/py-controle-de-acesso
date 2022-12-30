from passlib.context import CryptContext


CRYPT = CryptContext(
    schemes=['bcrypt'], 
    deprecated='auto'
)

def crypt_verify(password: str, hash_password: str) -> bool:
    return CRYPT.verify(password, hash_password)

def crypt_hash(password: str) -> str:
    return CRYPT.hash(password)
