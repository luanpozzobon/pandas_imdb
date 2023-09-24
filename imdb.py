import pandas as pd

ds = pd.read_table("./data_reduced.tsv", sep="\t", encoding="UTF-8")
ds['genres'] = ds['genres'].str.split(",")
ds = ds.explode('genres')

def get_genres():
    genres = ds['genres'].value_counts().reset_index()
    genres.columns = ['Gênero', 'Nº de Filmes']
    return genres

def get_movies(genero):
    movies = ds[ds['genres'] == genero]
    movies = movies.rename(columns={'primaryTitle' : 'Título'})
    return movies


def plot_graph(df, x_axis, y_axis, kind, name):
    plot = df.plot(x=x_axis, y=y_axis, kind=kind)
    plot.set_xlabel(x_axis)
    plot.set_ylabel(y_axis)
    plot.set_title(name)
    plot.get_figure().savefig(name + '.png')

genres = get_genres()
plot_graph(genres, 'Gênero', 'Nº de Filmes', 'bar', 'qtCont_genre')
print(genres)
genero = input("Selecione um gênero: ")
movies = get_movies(genero)

for index, row in movies.iterrows():
    print(row['Título'])
    
filme = input("Selecione um filme: ")
