
#lista de login e senha

login_user = {"nome": "",
              "senha": ""
              }

#Pergunta se deseja realizar o login
tem_login = str(input('Deseja realizar o login? [S/N] ')).upper().strip()


if (tem_login == 'S'):
    nome = input('Digite seu nome: ')
    senha = input('Digite sua senha: ')
    print('Login realizado com sucesso!')
    if(login_user["nome"] == nome and login_user["senha"] == senha):
        print('Acesso permitido!')
    else:
        print('Acesso negado!')
else:
    print('Login não realizado!')




