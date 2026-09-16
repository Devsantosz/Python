
#lista de login e senha

login_user = {"nome": "",
              "senha": ""
              }

nome = input('Digite seu nome: ')
senha = input('Digite sua senha: ')

login_user["nome"] = nome
login_user["senha"] = senha

print('Login realizado com sucesso!')

if(login_user["nome"] == nome and login_user["senha"] == senha):
    print('Acesso permitido!')
else:
    print('Acesso negado!')

