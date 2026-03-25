import pandas as pd

cidades = ['Maringá','itabira','Uberlândia','Salvador','Fortaleza']
populancao = [403.063,120.904,699.097,2.886698,2.686612]

populacao_cidades = dict(zip(cidades,populancao))
populacao_cidades['Vitoria'] = 365.855
print(populacao_cidades)