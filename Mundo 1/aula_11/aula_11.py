# tipo de fonte: 0 = none; 1 = bold; 4 = underline; 7 = negative
# cores da fonte: de 30 a 37, cada número simboliza uma cor
# background: de 40 a 47, cada número simboliza uma cor

print('\033[0;33;44mRoi, Letícia né?\033[0;33;44m') # font normal, cor amarela e background azul
print('\033[0;30;41m') # font normal, cor branca e background vermelho
print('\033[4;33;46m') # font sublinhada, cor amarela e background ciano
print('\033[1;35;43m') # font bold, cor rosa e background amarelo
print('\033[0;30;42m') # font normal, cor branca e background verde
print('\033[m') # font normal, cor amarela e background azul
print('\033[7;30m') # font negativa, cor branca -> preta

cores = {
    'limpa': '\033[m',
    'azul': '\033[34m',
    'amarelo': '\033[33m',
    'pretoebranco': '\033[7;30m'
}

print('Olá, {}mundo{}!'.format(cores['azul'], cores['limpa']))