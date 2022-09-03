from typing import List

print('Catálogo de Filmes')
print("-" * 19)

import pandas as pd

movies = []

movies.append(input('Filme: '))
movies.append(input('Diretor: '))
movies.append(input('Gênero: '))
movies.append(input('Quantidade de vezes assistida: '))

decision = input("Deseja adicionar mais filmes? S/N ")

while decision:
    if decision == 'S':
        movies.append(input('Filme: '))
        movies.append(input('Diretor: '))
        movies.append(input('Gênero: '))
        movies.append(input('Quantidade de vezes assistida: '))
        decision = input("Deseja adicionar mais filmes? S/N ")
    else:
        break

columns = ['FILME', 'DIRETOR', 'GÊNERO', 'ASSISTIDO']
catalog = pd.DataFrame(movies, columns)
catalogT = catalog.transpose()

print(catalogT)