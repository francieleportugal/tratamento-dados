import numpy as np

def getDadoNumerico(dado1, dado2):

    # Ambos estão vazios
    if (np.isnan(dado1) and np.isnan(dado2)):
        msgErro = 'Ambos os dados estão vazios.'
        return msgErro
    
    # Ambos não estão vazios
    if ((not np.isnan(dado1)) and (not np.isnan(dado2))):
        msgErro = 'Ambos os dados não estão vazios.'
        return msgErro
    
    # Dado 1 possui o valor
    if (not np.isnan(dado1)):
        return dado1
    
    # Dado 1 possui o valor
    if (not np.isnan(dado2)):
        return dado2

def teste():
    print ('Teste getDadoNumerico\n')
    
    print ('Teste ambos os valores NaN\n')
    resultado = getDadoNumerico(np.nan, np.nan)
    print ('___Result:', resultado, '\n')

    print ('Teste ambos os valores não NaN\n')
    resultado = getDadoNumerico(1, 2)
    print ('___Result:', resultado, '\n')

    print ('Teste somente dado1 NaN\n')
    resultado = getDadoNumerico(np.nan, 1)
    print ('___Result:', resultado, '\n')

    print ('Teste somente dado2 NaN\n')
    resultado = getDadoNumerico(1.1, np.nan)
    print ('___Result:', resultado, '\n')

if __name__== "__main__":
    teste()