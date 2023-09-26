<h1 align="center">Pandas IMDb</h1>
<p align="center">Análise da base de dados do IMDb</p>

## Alunos
<table>
    <tr>
        <td align="center">
            <a href="https://github.com/GabrielFerreira-Dev">
                <img src="https://avatars.githubusercontent.com/u/107369374?v=4" width="100px;" alt="Foto de Gabriel Ferreira no GitHub"/><br>
                <sub>
                    <b>Gabriel Ferreira</b>
                </sub>
            </a>
        </td>
        <td align="center">
            <a href="https://github.com/Guiiima">
                <img src="https://avatars.githubusercontent.com/u/101485588?v=4" width="100px;" alt="Foto de Guilherme Henrique no GitHub"/><br>
                <sub>
                    <b>Guilherme Henrique</b>
                </sub>
            </a>
        </td>
        <td align="center">
            <a href="http://github.com/luanpozzobon">
                <img src="https://avatars.githubusercontent.com/u/108753073?v=4" width="100px;" alt="Foto de Luan Pozzobon no GitHub"/><br>
                <sub>
                    <b>Luan Pozzobon</b>
                </sub>
            </a>
        </td>
    </tr>
</table>
<hr>

## Pré-Requisitos
Antes de executar o projeto, é necessário <a href="https://datasets.imdbws.com/title.basics.tsv.gz">baixar o dataset</a>.<br>
Também é necessário instalar as dependências:
```
pip install -r requirements.txt
```

## Exemplos  de Uso
Após o carregamento do dataset, o usuário será perguntado a analisar a base por gênero ou período de lançamentos.<br>
Ao final será gerado um gráfico mostrando a proporção entre filmes adultos e não-adultos.
### Gênero
Ao selecionar a opção gênero será mostrado ao usuário uma lista com todos os gêneros, a quantidade de títulos e a média de tempo para cada gênero. O usuário deve selecionar um gênero, e então será mostrado a ele, os títulos daquele gênero. Ao selecionar o título, ele poderá visualizar mais informações sobre aquele título.<br>
Ao final serão gerados os gráficos quanto a quantidade de títulos lançados para cada gênero, e à média de duração para cada gênero.
### Período
O usuário pode selecionar a opção período, e então, entrar com o ano inicial e ano final, será então mostrado ao usuário uma lista de títulos que foram lançados entre aqueles anos. O usuário pode também, selecionar um título para obter mais informações.<br>
Ao final será gerado um gráfico, mostrando a quantidade de títulos lançados por ano