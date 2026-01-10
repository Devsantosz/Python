#exceção é um objeto que representa um erro que ocorre durante a execução de um programa.

#Blocos try e except 

def div(k, j):
    return round(k / j, 2)

if __name__ == '__main__':
    while True:
        try:
            n1 = int(input('Digite um número: '))
            n2 = int(input('Digite outro número: '))
            break
        except ValueError:
            print('Ocorreu um erro ao ler o valor, tente novamente...')
    try:
        r = div(n1, n2)
    except ZeroDivisionError:
        print('Erro: Divisão por zero não é permitida.')
    except:
        print('Erro desconhecido....')
    else:
        print(f'O resultado:{r}')
    finally:
        print(f'\nFim do programa')
