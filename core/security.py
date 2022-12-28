from passlib.context import CryptContext


CRYPT = CryptContext(
    schemes=['bcrypt'], 
    deprecated='auto'
)

def crypt_verify(senha: str, hash_senha: str) -> bool:
    return CRYPT.verify(senha, hash_senha)

def crypt_hash(senha: str) -> str:
    return CRYPT.hash(senha)
