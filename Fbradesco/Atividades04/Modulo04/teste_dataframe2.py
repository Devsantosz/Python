import pandas as pd

nome_cidade = pd.Series(['Maringá','itabira','uberlândia'])
populancao = pd.Series([403.063,120.904,699.097])

pd.DataFrame({"Cidade": nome_cidade, "populção": populancao})