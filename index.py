# import sys
# sys.path.insert(0, '/Utils')
from Utils import levenshtein
from Utils import normalizarNome

print ('Teste algoritmo de semellhança entre nomes\n')

# Teste algoritmo de semellhança entre nomes para nomes completamente iguais
print ('___(\'Franciele\', \'Franciele\')')
result = levenshtein.levenshtein('Franciele', 'Franciele')
print ('___Result:', result, '\n') # O resultado deve ser igual a 0, indicando nomes completamente iguais

# Teste algoritmo de semellhança entre nomes para nomes com pouca diferença
print ('___(\'Franciele\', \'franciele\')')
result = levenshtein.levenshtein('Franciele', 'franciele')
print ('___Result:', result, '\n')

# Teste algoritmo de semellhança entre nomes diferentes mas um pouco semelhantes
print ('___(\'Franciele\', \'Francine\')')
result = levenshtein.levenshtein('Franciele', 'Francine')
print ('___Result:', result, '\n')

# Teste algoritmo de semellhança entre nomes diferentes
print ('___(\'Franciele\', \'Fernando\')')
result = levenshtein.levenshtein('Franciele', 'Fernando')
print ('___Result:', result, '\n')


print ('Teste normalização de nomes\n')

# Teste da função de remover os acentos
print ('___(\'áêãòÁÊÃÒ\'#\')')
result = normalizarNome.normalizar_nome('áêãòÁÊÃÒoo\'ii#')
print ('___Result:', result, '\n')