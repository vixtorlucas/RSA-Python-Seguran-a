##2 - Pesquise por ferramentas que possam ser utilizadas pela linha de comando para gerar pares de chaves assimétricas.
# Enumere os comandos necessários para criar um par de chaves, explicando como o comando deve ser executado.


## Resposta: Para Criação de chaves assimetricas por meio da linha de comando pode-se utilizar da ferramenta
# conhecida como OpenSSL.
# O comando para iniciar a chave privada é:
# openssl genrsa nomeDaChave.key 2048, onde o primeiro nome é a ferramenta utlizada a segunda o gerador da chave,
# o proximo parametro o nome da chave, e o ultimo o seu tamanho
# Para criar o Certificado de assinatura se utiliza o comando
# openssl req -key nomeDaChave.key -new -out nomeDaCert.csr
# onde se passa o nome da chave em nomeDaChave.key e o nome do certificado gerado em nomeDaCert.csr
# esses são os principais para a geração de chaves assimetricas
# #