print('Catálogo de Filmes')
print("-" * 19)

import pandas as pd

filmes = []
data = []
qtd =[]

filmes.append(input('Filme: '))
data.append(input('Última Vez que Assistiu: '))
qtd.append(input('Quantas Vezes Assistiu: '))

dados = {"Filme":filmes, "Data":data, "Qtd":qtd}
catalogo = pd.DataFrame(dados)

print(catalogo)