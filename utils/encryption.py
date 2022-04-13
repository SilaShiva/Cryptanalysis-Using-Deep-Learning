import binascii
import string
import numpy as np
np.random.seed(30)

from pyDes import des, CBC, PAD_PKCS5
import pyaes
import pbkdf2
import unicodedata

def caesar_cipher(plainText):
    """
    Args:
    plainText(string): Text to be encrypted
    key(int): Shift value for Caesar Cipher
    """
    key = np.random.randint(low=1, high=26)
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    shifted_alphabet = alphabet[26-key:]+alphabet[0:(26-key)]
    shifted_number = numbers[10-key:]+numbers[0:(10-key)]
    cipher_text = ""

    for i in range(len(plainText)):
        char = plainText[i]
        if(char.isalpha()):
            idx = alphabet.find(char.upper())
            if idx == -1:
                cipher_text = cipher_text + char
            elif char.islower():
                cipher_text = cipher_text + shifted_alphabet[idx].lower()
            else:
                cipher_text = cipher_text + shifted_alphabet[idx]

        elif(char.isnumeric()):
            idx = numbers.find(char.upper())
            if idx == -1:
                cipher_text = cipher_text + char
            else:
                cipher_text = cipher_text + shifted_number[idx]

    return (cipher_text, key)

def aes_encrypt(text, seed):
  key = pbkdf2.PBKDF2(seed, '').read(32)
  aes = pyaes.AESModeOfOperationCTR(key)
  ciphertext = aes.encrypt(text)
  return (binascii.hexlify(ciphertext), seed)

def des_encrypt(text, seed):
    secret_seed = seed
    iv = secret_seed
    k = des(secret_seed, CBC, iv, pad=None, padmode=PAD_PKCS5)
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'replace')
    en = k.encrypt(text, padmode=PAD_PKCS5)
    return (binascii.b2a_hex(en).decode(), seed)


def vigenere_cipher(text, key):
    enc = 'abcdefghijklmnopqrstuvwxyz0123456789'
    ciph = ''
    key = key.lower()
    text = text.lower()
    j = 0
    for i in range(len(text)):
        try:
            if text[i].isalpha() or text[i].isnumeric():
                ciph += enc[(enc.index(text[i])+enc.index(key[j])) % len(enc)]
                j += 1
                j %= len(key)
            else:
                ciph += text[i]
        except:
            ciph += text[i]
    return (ciph, key)