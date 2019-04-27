# import sys
# sys.path.insert(0, '/Utils')
from Utils import levenshtein

print ('Teste algoritmo de semellhança entre nomes\n')

# Teste algoritmo de semellhança entre nomes para nomes completamente iguais
print ('(\'Franciele\', \'Franciele\')')
result = levenshtein.levenshtein('Franciele', 'Franciele')
print ('Result:', result, '\n') # O resultado deve ser igual a 0, indicando nomes completamente iguais

# Teste algoritmo de semellhança entre nomes para nomes com pouca diferença
print ('(\'Franciele\', \'franciele\')')
result = levenshtein.levenshtein('Franciele', 'franciele')
print ('Result:', result, '\n')

# Teste algoritmo de semellhança entre nomes diferentes mas um pouco semelhantes
print ('(\'Franciele\', \'Francine\')')
result = levenshtein.levenshtein('Franciele', 'Francine')
print ('Result:', result, '\n')

# Teste algoritmo de semellhança entre nomes diferentes
print ('(\'Franciele\', \'Fernando\')')
result = levenshtein.levenshtein('Franciele', 'Fernando')
print ('Result:', result, '\n')
