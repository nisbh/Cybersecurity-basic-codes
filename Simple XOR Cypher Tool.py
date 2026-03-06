# -*- coding: utf-8 -*-
"""
Created on Sun Sep 28 21:11:09 2025

@author: nisar
"""


# xor_tool.py
def xor_bytes(data: bytes, key: bytes) -> bytes:
    return bytes(b ^ key[i % len(key)] for i, b in enumerate(data))

if __name__ == "__main__":
    import sys
    mode = sys.argv[1] if len(sys.argv) > 1 else "enc"
    key = b"secret"
    if mode == "enc":
        plain = input("plaintext: ").encode()
        cipher = xor_bytes(plain, key)
        print(cipher.hex())
    else:
        hexs = input("hex: ")
        cipher = bytes.fromhex(hexs)
        plain = xor_bytes(cipher, key)
        print(plain.decode(errors="replace"))
