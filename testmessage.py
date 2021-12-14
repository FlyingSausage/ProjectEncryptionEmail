import cipherDecryption, cipherEncryption
s = 'abcdefghijklmnopqrstuvwxyz123456789'

s1 = cipherEncryption.encryption(s)
s2 = cipherDecryption.decryption(s1)

print(s1)
print(s2)


