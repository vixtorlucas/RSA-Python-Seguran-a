# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import rsa

def generateKeys():
    (publicKey, privateKey) = rsa.newkeys(512)
    with open('keys/publicKey.pem', 'wb') as p:
        p.write(publicKey.save_pkcs1('PEM'))
    with open('keys/privateKey.pem', 'wb') as p:
        p.write(privateKey.save_pkcs1('PEM'))

def loadKeys():
    with open('keys/publicKey.pem', 'rb') as p:
        publicKey = rsa.PublicKey.load_pkcs1(p.read())
        print(publicKey)
    with open('keys/privateKey.pem', 'rb') as p:
        privateKey = rsa.PrivateKey.load_pkcs1(p.read())
        print(privateKey)
    return privateKey, publicKey

def encrypt(message, key):
    return rsa.encrypt(message.encode('ascii'), key)

def decrypt(ciphertext, key):
    try:
        return rsa.decrypt(ciphertext, key).decode('ascii')
    except:
        return False

def sign(message, key):
    return rsa.sign(message.encode(), key, 'SHA-1')

def verify(message, signature, key):
    try:
        return rsa.verify(message.encode('ascii'), signature, key,) == 'SHA-1'
    except:
        return False


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Use at least 2048 bit keys nowadays, see e.g. https://www.keylength.com/en/4/
    publicKey, privateKey = rsa.newkeys(2048)

    # Export public key in PKCS#1 format, PEM encoded
    publicKeyPkcs1PEM = publicKey.save_pkcs1().decode('utf8')
    print(publicKeyPkcs1PEM)
    # Export private key in PKCS#1 format, PEM encoded
    privateKeyPkcs1PEM = privateKey.save_pkcs1().decode('utf8')
    print(privateKeyPkcs1PEM)

    # Save and load the PEM encoded keys as you like

    # Import public key in PKCS#1 format, PEM encoded
    publicKeyReloaded = rsa.PublicKey.load_pkcs1(publicKeyPkcs1PEM.encode('utf8'))
    # Import private key in PKCS#1 format, PEM encoded
    privateKeyReloaded = rsa.PrivateKey.load_pkcs1(privateKeyPkcs1PEM.encode('utf8'))

    plaintext = "vinay kumar shukla".encode('utf8')
    print("Plaintext: ", plaintext)

    ciphertext = rsa.encrypt(plaintext, publicKeyReloaded)
    print("Ciphertext: ", ciphertext)

    decryptedMessage = rsa.decrypt(ciphertext, privateKeyReloaded)
    print("Decrypted message: ", decryptedMessage)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
