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


path = input("Caminho do arquivo: ")
pathKey = input("Caminho da chave privada: ")

with open(path) as f:
    file = f.read()
    print(file)
    with open(pathKey, 'rb') as p:
        publicKeyReloaded = rsa.PrivateKey.load_pkcs1(p.read())
        signature = sign(file, publicKeyReloaded)

        print(signature.decode('latin-1'))
        pathValue = Path(path)

        newfileValue = str(pathValue.parent) + '/' + str(pathValue.name) + '_assinado.txt'
        with open(newfileValue, 'xb') as new:
            new.write(file.encode())
            new.write(signature)
            new.close()
            
        p.close()
        f.close()
