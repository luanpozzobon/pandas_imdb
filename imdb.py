import pandas as pd

ds = pd.read_table("./data.tsv", sep="\t", encoding="UTF-8")
ds['runtimeMinutes'] = pd.to_numeric(ds['runtimeMinutes'], errors='coerce')
ds['isAdult'] = pd.to_numeric(ds['isAdult'], errors='coerce')
ds_sep_gen = ds
ds_sep_gen['genres'] = ds_sep_gen['genres'].str.split(",")
ds_sep_gen = ds_sep_gen.explode('genres')


def get_genres():
    genres = ds_sep_gen['genres'].value_counts().reset_index()
    genres['Duração Média'] = ds_sep_gen.dropna(subset=['runtimeMinutes']).groupby('genres')['runtimeMinutes'].mean().reset_index()['runtimeMinutes']
    genres.columns = ['Gênero', 'Nº de Filmes', 'Duração Média']
    
    return genres

def get_movies(genero):
    movies = ds_sep_gen[ds_sep_gen['genres'] == genero]
    movies = movies.rename(columns={'primaryTitle' : 'Título'})
    return movies

def get_movie_info(filme):
    return ds[ds['primaryTitle'] == filme]

def plot_graph(df, x_axis, y_axis, kind, name):
    plot = df.plot(x=x_axis, y=y_axis, kind=kind)
    plot.set_xlabel(x_axis)
    plot.set_ylabel(y_axis)
    plot.set_title(name)
    plot.get_figure().savefig(name + '.png')


genres = get_genres()
print(genres)
genero = input("Selecione um gênero: ")
movies = get_movies(genero)

for index, row in movies.iterrows():
    print(f"{index}\t{row['Título']}")
    
filme = input("Selecione um filme: ")
movie = get_movie_info(filme)
print(movie)

plot_graph(genres, 'Gênero', 'Nº de Filmes', 'bar', 'qtCont_genre')
plot_graph(genres, 'Gênero', 'Duração Média', 'bar', 'medDur_genre')