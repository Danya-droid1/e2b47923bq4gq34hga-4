
from ripemd160 import ripemd160

def encrypt(data: str) -> str:
    return ripemd160(data.encode()).hex()
