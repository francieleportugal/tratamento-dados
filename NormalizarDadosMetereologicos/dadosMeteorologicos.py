import pandas as pd

def normalizar():
    df = pd.read_excel('/home/franciele/Projetos/dados-dengue/Dados/dados_meteorologicos.xlsx', head=[0, 1, 2, 3, 4, 5, 6])
    df.columns = ['municipio', 'data', 'hora', 'precipitacao', 'temperatura_maxima',
     'temperatura_minima', 'temperatura_media', 'umidade_relativa_media']            

    """
    print('=========================================================================================')
    print('                                 RESUMO DAS INFORMAÇÕES                                  ')
    print(df.head())
    print(df.columns)
    print(df.dtypes)
    print(df.index)
    print(df.shape)
    print(df.count())
    """

    # Formatando a data
    df['data'] = df.data.dt.strftime('%d/%m/%Y') 
    # print(df.head())

    # Ordenando os dados
    df.sort_values(['municipio', 'data', 'hora'], ascending=[True, True, True])
    # print(df.head())

    # Lista única município
    lista_municipios = df.municipio.unique()
    """ print(lista_municipios)
    print(lista_municipios.size) """

    # Lista única data
    lista_datas = df.data.unique()
   """  print(lista_datas)
    print(lista_datas.size) """

    #

if __name__== "__main__":
    normalizar()