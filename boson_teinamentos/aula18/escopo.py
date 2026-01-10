#Escopo Global e Local 
var_global = 'Curso de Python'

def escreve_texto():
    global var_global
    var_local = 'Aula de Escopo'
    var_global = 'Banco de dados com SQL'
    print(f'Variável Global: {var_global}')
    print(f'Variável Local: {var_local}')

if __name__ == '__main__':
    print(f'executar a função escreve_texto():')
    escreve_texto()

    print(f'tentar acessar as variaveis diretamente')
    print(f'Variável Global: {var_global}')
    # print(f'Variável Local: {var_local}')  # Isso causará um erro, pois var_local não está definida no escopo global