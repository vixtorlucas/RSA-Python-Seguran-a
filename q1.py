import rsa

##1 - Implemente um sistema que simula uma troca de mensagens entre duas partes
# cifradas através do RSA. Não é necessário pedir o input do usuário, bastando
# que o sistema exercite a geração de pares
# de chaves públicas e privadas aleatórias, seguido da cifragem
# e decifragem de mensagens de forma correta.


publicKey, privateKey = rsa.newkeys(2048)

publicKeySaved = publicKey.save_pkcs1('PEM').decode('utf8')
print(publicKeySaved)
# Export private key in PKCS#1 format, PEM encoded
privateKeySaved = privateKey.save_pkcs1('PEM').decode('utf8')
print(privateKeySaved)

with open('keys/publicKey.pem', 'wb') as p:
    p.write(publicKey.save_pkcs1('PEM'))
with open('keys/privateKey.pem', 'wb') as p:
    p.write(privateKey.save_pkcs1('PEM'))


plaintext = "Mensagem de texto para q1".encode('utf8')
print("Plaintext: ", plaintext)

with open('keys/publicKey.pem', 'rb') as p:
    publicKeyReloaded = rsa.PublicKey.load_pkcs1(p.read())
    ciphertext = rsa.encrypt(plaintext, publicKeyReloaded)
    print("Ciphertext: ", ciphertext)
with open('keys/privateKey.pem', 'rb') as p:
    privateKeyReloaded = rsa.PrivateKey.load_pkcs1(p.read())
    decryptedMessage = rsa.decrypt(ciphertext, privateKeyReloaded)
    print("Mensagem decriptada: ", decryptedMessage)




