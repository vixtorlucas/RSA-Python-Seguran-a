import rsa
from pathlib import Path
import base64

def sign(message, key):
    return rsa.sign(message.encode('ascii'), key, 'SHA-1')

def verify(message, signature, key):
    try:
        return rsa.verify(message.encode('ascii'), signature, key,) == 'SHA-1'
    except:
        return False

path = input("Caminho do arquivo assinado: ")
pathKey = input("Caminho da chave publica: ")

with open(path, 'rb') as f:
    file = f.read()
    print(file)
    with open(pathKey, 'rb') as p:
        pubkey = rsa.PublicKey.load_pkcs1(p.read())
        valida = False
        for element in range(0, len(file.decode('latin-1'))):
            try:
                response = rsa.verify(file[0:element], file[element:len(file)], pubkey)
                valida = True
                print('Arquivo Valido')
            except:
                continue

        if not valida:
            print('Documento invalido')
        p.close()
        f.close()

