def getDateSplit(data):
    split = data.split('/')
    dia = split[0]
    mes = split[1]    
    ano = split[2]
    return dia, mes, ano
