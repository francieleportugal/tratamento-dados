def save_log(arquivoCodigo, arquivoDados, msgErro, municipio, data, campo):
    arquivo = open('log.txt','a')
    arquivo.write('Arquivo do código: ' + arquivoCodigo + '\n')
    arquivo.write('Arquivo de dados: ' + arquivoDados + '\n')
    arquivo.write('Mensagem erro: ' + msgErro + '\n')
    if (municipio != ''):
        arquivo.write('Município: ' + municipio + '\n')
    if (data != ''):
        arquivo.write('Data: ' + data + '\n')
    if (campo != ''):
        arquivo.write('Campo: ' + campo + '\n')
    arquivo.write('============================================================================================\n')
    arquivo.close()

def test():
    erro = 'MUNICIPIO'
    arquivoCodigo = 'testeNormalizacao.ipynb'
    arquivoDados = 'dados_meteorologicos.xlsx'
    msgErro = 'Não há dados para o municipio ' + lista_municipios[i] + '.'
    municipio = ''
    data = ''
    campo = ''
    save_log(arquivoCodigo, arquivoDados, msgErro, municipio, data, campo)

if __name__== "__main__":
    test()