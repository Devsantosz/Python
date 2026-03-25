import pandas as pd

disciplisnas = { 'Curso' : ['Estatística','Economia','Cálculo','Geometria'],
                'Créditos': [90,60,90,40],
                'Requisito' : [True, False, True, False]}

data = pd.DataFrame(disciplisnas)
print(data)