print('Catálogo de Filmes')
print("-" * 19)

import pandas as pd

movies = []

def options():
    movie = input('Filme: ')
    director = input('Diretor: ')
    genre = input('Gênero: ')
    time = int(input('Quantidade de vezes assistido: '))
    movies.append({'FILME': movie, 'DIRETOR': director, 'GÊNERO': genre, 'X ASSISTIDO': time})


options()
decision = input("Deseja adicionar mais filmes? S/N ")

while decision:
    if decision == 'S':
        options()
        decision = input("Deseja adicionar mais filmes? S/N ")
    else:
        break

catalog = pd.DataFrame(movies)

print(catalog)