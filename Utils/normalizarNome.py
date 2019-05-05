from unicodedata import normalize

def remover_acentos(nome):
    return normalize('NFKD', nome).encode('ASCII', 'ignore').decode('ASCII')

def remover_caracteres(nome):
    caracteresIndesejados = '\''
    for i in range(0,len(caracteresIndesejados)):
        nome = nome.replace(caracteresIndesejados[i],'')
    return nome

def normalizar_nome(nome):
    novoNome = remover_acentos(nome)
    novoNome = remover_caracteres(novoNome)
    novoNome = novoNome.upper()
    return novoNome

def teste():
    print ('Teste normalização de nomes\n')

    # Teste da função de remover os acentos
    print ('___(\'áêãòÁÊÃÒ\'#\')')
    result = normalizar_nome('áêãòÁÊÃÒoo\'ii#')
    print ('___Result:', result, '\n')

if __name__== "__main__":
    teste()