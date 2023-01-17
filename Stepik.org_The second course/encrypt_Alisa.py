import simplecrypt


with open("encrypted.bin", "rb") as encrypt:
    encrypted = encrypt.read()
with open("passwords.txt", "r") as inp:
    passw = inp.read().split('\n')
    passw.pop()

for p in passw:
    try:
        secret = simplecrypt.decrypt(p, encrypted).strip()
    except simplecrypt.DecryptionException:
        print('Error')
        continue
    print(secret)
    break


