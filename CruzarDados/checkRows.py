def check (rowDadosMeteo, rowDadosNotifDengue):
    
    codigoErro = -1
    msgErro = 'Erro não tratado.'

    rowDadosMeteoVazio = rowDadosMeteo.shape[0] == 0
    rowDadosNotifDengueVazio = rowDadosNotifDengue.shape[0] == 0
    
    ambosVazios = rowDadosMeteoVazio and rowDadosNotifDengueVazio
    
    if (ambosVazios):
        codigoErro = 0
        msgErro = 'Não existe dados para esse municipio e data em ambas as bases de dados.'
    
    if (not ambosVazios):
        
        if (rowDadosMeteoVazio):    
            codigoErro = 1
            msgErro = 'Não existe dados para esse municipio e data na base de dados meteorologicos.'
        
        elif (rowDadosNotifDengueVazio):   
            codigoErro = 2
            msgErro = 'Não existe dados para esse municipio e data na base de dados de notificacoes de dengue.'

        else:
            
            codigoErro = 3

            qtdRowDadosMeteo = rowDadosMeteo.shape[0]
            qtdRowDadosNotifDengue = rowDadosNotifDengue.shape[0]
            
            msgErro = 'Para esse municipio e data '
            msgErro = msgErro + 'há' + str(qtdRowDadosMeteo) + 'registros na base de dados meteorologicos '
            msgErro = msgErro + 'e há' + str(qtdRowDadosNotifDengue) + 'registros na base de dados de notificacoes de dengue.' 

    return codigoErro, msgErro
            