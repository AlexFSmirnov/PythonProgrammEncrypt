def encrypt(arr, key):
    encrypted = [None] * len(arr)
    for i in range(len(arr)):
        encrypted[i] = arr[i] ^ ord(key[i % len(key)])
    return encrypted


template = '''def decrypt(arr, key):
    decrypted = ""
    for i in range(len(arr)):
        decrypted += chr(arr[i] ^ ord(key[i % len(key)]))
    return decrypted


key = input("Enter the key: ")
exec(decrypt({}, key))'''

filename = input("Enter the file to encrypt: ")
key = input("Enter the key: ")
with open(filename, 'rb') as fin:
    encrypted = encrypt(list(fin.read()), key)
    fin.close()

encrypted_programm = template.format(encrypted)
with open(filename[:-3] + "-encrypted" + ".py", 'w') as fout:
    fout.write(encrypted_programm)
    fout.close()