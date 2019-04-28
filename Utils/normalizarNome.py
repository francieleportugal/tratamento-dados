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
    novoNome = remover_caracteres(nome)
    novoNome = novoNome.upper()
    return novoNome