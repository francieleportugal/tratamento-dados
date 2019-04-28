import numpy as np

def levenshtein(seq1, seq2):  
    size_x = len(seq1) + 1
    size_y = len(seq2) + 1
    matrix = np.zeros ((size_x, size_y))
    
    for x in range(size_x):
        matrix [x, 0] = x

    for y in range(size_y):
        matrix [0, y] = y

    for x in range(1, size_x):
        for y in range(1, size_y):
            if seq1[x-1] == seq2[y-1]:
                matrix [x,y] = min(
                    matrix[x-1, y] + 1,
                    matrix[x-1, y-1],
                    matrix[x, y-1] + 1
                )
            else:
                matrix [x,y] = min(
                    matrix[x-1,y] + 1,
                    matrix[x-1,y-1] + 1,
                    matrix[x,y-1] + 1
                )
    # print (matrix)
    return (matrix[size_x - 1, size_y - 1])

def teste():
    print ('Teste algoritmo de semellhança entre nomes\n')

    # Teste algoritmo de semellhança entre nomes para nomes completamente iguais
    print ('___(\'Franciele\', \'Franciele\')')
    result = levenshtein('Franciele', 'Franciele')
    print ('___Result:', result, '\n') # O resultado deve ser igual a 0, indicando nomes completamente iguais

    # Teste algoritmo de semellhança entre nomes para nomes com pouca diferença
    print ('___(\'Franciele\', \'franciele\')')
    result = levenshtein('Franciele', 'franciele')
    print ('___Result:', result, '\n')

    # Teste algoritmo de semellhança entre nomes diferentes mas um pouco semelhantes
    print ('___(\'Franciele\', \'Francine\')')
    result = levenshtein('Franciele', 'Francine')
    print ('___Result:', result, '\n')

    # Teste algoritmo de semellhança entre nomes diferentes
    print ('___(\'Franciele\', \'Fernando\')')
    result = levenshtein('Franciele', 'Fernando')
    print ('___Result:', result, '\n')

if __name__== "__main__":
    teste()