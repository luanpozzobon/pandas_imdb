import pandas as pd
import matplotlib.pyplot as plt

# Leitura do dataset
ds = pd.read_table("./data.tsv", sep="\t", encoding="UTF-8")

# Conversão de colunas para tipos numéricos
ds['runtimeMinutes'] = pd.to_numeric(ds['runtimeMinutes'], errors='coerce')
ds['isAdult'] = pd.to_numeric(ds['isAdult'], downcast='integer', errors='coerce')
ds['startYear'] = pd.to_numeric(ds['startYear'], downcast='integer', errors='coerce')
ds['endYear'] = pd.to_numeric(ds['endYear'], downcast='integer', errors='coerce')

# Divisão da coluna 'genres' em listas e expansão do DataFrame
ds_sep_gen = ds
ds_sep_gen['genres'] = ds_sep_gen['genres'].str.split(",")
ds_sep_gen = ds_sep_gen.explode('genres')



# Função para obter os gêneros e informações sobre os gêneros
def get_genres():
    genres = ds_sep_gen['genres'].value_counts().reset_index()
    genres['Duração Média'] = ds_sep_gen.dropna(subset=['runtimeMinutes']).groupby('genres')['runtimeMinutes'].mean().round(2).reset_index()['runtimeMinutes']
    genres.columns = ['Gênero', 'Nº de Filmes', 'Duração Média']
    
    return genres


# Função para obter filmes de um gênero específico
def get_movies(genero):
    movies = ds_sep_gen[ds_sep_gen['genres'] == genero]
    movies = movies.rename(columns={'primaryTitle' : 'Título'})
    return movies

# Função para obter filmes dentro de um período de anos
def get_movies_by_data(dataInicial, dataFinal):
    movies_return = ds[(ds['startYear'] >= dataInicial) & (ds['startYear'] <= dataFinal)].sort_values('startYear')
    movies_return = movies_return.rename(columns={'primaryTitle' : 'Título', 'startYear' : 'Ano'})
    return movies_return

# Função para obter as informações sobre um filme
def get_movie_info(filme):
    return ds[ds['primaryTitle'] == filme]
    

# Função para contar o número de filmes por ano
def contador_groupby(dataset):
    cont_groupby = dataset['Ano'].value_counts().reset_index()
    cont_groupby.columns = ['Ano', 'Nº de Filmes']
    return cont_groupby
    
# Função para plotar gráficos
def plot_graph(df, x_axis, y_axis, kind, name):
    df.plot(x=x_axis, y=y_axis, kind=kind, figsize=(10, 8))
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    plt.title(name)
    plt.savefig(name + '.png')


selecao = input("Deseja selecionar por período ou por genero?:")
if(selecao.lower().__contains__("gen")):
    genres = get_genres()
    print(genres)
    genero = input("Selecione um gênero: ")
    movies = get_movies(genero=genero)
    print(movies)
    
    filme = input("Selecione um filme: ")
    movie = get_movie_info(filme)
    print(movie)
    # Plotagem de gráficos relacionados a gêneros
    plot_graph(genres, 'Gênero', 'Nº de Filmes', 'bar', 'qtCont_genre')
    plot_graph(genres, 'Gênero', 'Duração Média', 'bar', 'medDur_genre')
elif(selecao.lower().__contains__("per")):
    dataInit = int(input("Digite um ano de inicio: "))
    dataFin = int(input("Digite data final: "))
    movies = get_movies_by_data(dataInicial=dataInit, dataFinal=dataFin)
    print(movies)

    filme = input("Selecione um filme: ")
    movie = get_movie_info(filme)
    print(movie)

    # Plotagem de gráficos relacionados a anos
    plot_graph(contador_groupby(movies), 'Ano', 'Nº de Filmes', 'bar', 'qtdFilme_ano')

# Criação de uma cópia do DataFrame original para análise de filmes adultos
temp = ds.copy()
temp['isAdult'] = ds['isAdult'].replace('\\N', pd.NA)
temp = temp.dropna(subset=['isAdult'])
temp = temp[temp['isAdult'] < 2]
counts = temp['isAdult'].value_counts()

# Plotagem de um gráfico de pizza para mostrar a distribuição de filmes adultos
plt.figure(figsize=(7,7))
counts.plot(y='isAdult', labels=['Não Adulto', 'Adulto'], kind='pie', autopct='%1.1f%%')
plt.title('Filmes Adultos')
plt.ylabel('')
plt.legend(loc="upper right")
plt.axis('equal')
plt.tight_layout()
plt.savefig('isAdult_filme.png')