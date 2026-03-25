import pandas as pd

Autor = ['Sun Tzu', 'Fernando Pessoa', 'Thomas Mann', 'João Guimarães Rosa']
Livro = ['A Arte da Guerra', 'Poesias Selecionadas', 'A montanha mágica', 'Primeiras Estórias']
Ano = [2000, 2004, 2015, 2017]

dados = {
    'Auto':Autor,
    'Livro':Livro,
    'Autor':Autor
}

autores = pd.DataFrame(dados)
df = pd.DataFrame(autores)
print(df)

df.to_csv("autores.csv")

autores.info()