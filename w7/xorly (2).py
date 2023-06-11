def encrypt(plaintext, key):
    ciphertext = []
    for i in range(0, len(plaintext)):
        ciphertext.append(ord(plaintext[i]) ^ ord(key[i%len(key)])) 

    return ''.join(map(chr, ciphertext))

decrypt = encrypt

def hex_to_str(s):
    return ''.join(chr(int(s[i:i+2], 16)) for i in range(0, len(s), 2))

def str_to_hex(s):
    return ''.join(format(ord(c), '02x') for c in s)

plaintext = "Here is a sample. Pay close attention!"
ciphertext_hex = "2e0c010d46000048074900090b191f0d484923091f491004091a1648071d070d081d1a070848"
ciphertext = hex_to_str(ciphertext_hex)

key = encrypt(plaintext, ciphertext)

print("Key: {}".format(str_to_hex(key)))

flag_hex = "0005120f1d111c1a3900003712011637080c0437070c0015"
flag = hex_to_str(flag_hex)

decrypted_flag = decrypt(flag, key)

print("Decrypted Flag: {}".format(decrypted_flag))
