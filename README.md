## Repositorio de Estudo de PYTHON

> Base de estudos da linguagem de programacao **python**.

## Informacoes
- Uso de IDE De trabalho *Pycharm*/*VScode*.
- Estudo base do curso online - Curso em video.
- Desenvolvimento fora e dentro do curso.
```
msg = 'Ola, Mundo!'
print(msg)
```
<p>Uso de variaveis e seus tipos(int, float, bool), com conceitos basicos de uso.</p>

1 - Entrada e saida de dados:
```
n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))

media = (n1 + n2) / 2

print('A media do aluno e {}'.format(media))
```
<p>Entrada de dados pelo usuario e seu tratamento e ultilizacao, desde a soliciatacao, tratamento, formatacao e uso.</p>

2 - Calculos matematicos e formatacao de valores(variaveis):
```
d = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))

km_value = 0.15
d_value = 60

orc = (d * d_value) + (km * km_value)

print('O total a pagar e R${:.2f}'.format(orc))
```
<p>Calculos matematicos e seus operadores, com formatacao de casas numericas.</p>

3 - Uso de bibliotecas:
```
import random 
from time import sleep #biblioteca de tempo

numero_aleatorio = random.randint(0,5)

num_select = int(input('Digite um numero de 0 a 5: '))
print("Processando resposta...")
sleep(2) # Faz o computador "dormir por () determinado."
if (num_select == numero_aleatorio):
    print('Voce ganho, parabens!')
else:
    print('Voce erro!')
    print(f'O numero era {numero_aleatorio}.')
```
<p>Uso de bibliotecas naturais da linguigem entre outras que estao disponiveis.</p>

4 - Estruturas de decisao com if, elfi else:
```
num1 = int(input("Digite um numero inteiro: "))
num2 = int(input("Digite outro numero inteiro: "))

#Operador logico de comparacao, verifica se num1 e maior que num2.
if num1 > num2:
    print(f"O numero {num1} e maior que o numero {num2}")
elif num1 < num2:
    print(f"O numero {num2} e maior que o numero {num1}")
#Operador logico de comparacao, verifica se ambos os numeros sao igual.
#elif num1 == num2:
else:
    print(f"O numero {num1} e igual a {num2}")
```
<p>Estruturas de decisoes e suas condicoes, para tomada de caminhos.</p>

5 - Estrutura de repeticao For(Ate o momento):
```
from time import sleep

fogos = int(input("Quantos fogos de artificios estouraram?"))

for c in range(10, -1, -1):
    sleep(0.5)
    print(c)
    if c == 0:
        for c in range(1,fogos+1):
            sleep(0.3)
            print("POOOW!")
print(f"Foram {fogos} fogos.")
```

<p>Estrutura de repeticao que tem um valor certo de repeticao.</p>

### Repositorio focado em documentar o aprendizado da linguagem python, a cada passo concluido e utilizado.
