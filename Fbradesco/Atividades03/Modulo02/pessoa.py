class Pessoa:
    "Isto é uma nova classe, chamada pessoa."

    idade = 15

    def saudacao(self):
        print("Olá, Pessoas!")

#Create new object of person class
matheus = Pessoa()

#Outpot: 15
print(matheus.idade)

#Outpot <Bound method person.greet of <__main__.person object>
print(matheus.saudacao)

#Chamando o metodo saudacao
#Outpot: "Olá, Pessoas!"
matheus.saudacao()