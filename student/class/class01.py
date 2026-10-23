from time import sleep

class carro:
    #Funcao de criar o objeto carro
    def __init__(self, marca, modelo): #Atributos do objeto
        self.marca = marca      #Atributo
        self.modelo = modelo    #Atributo
        self.ligado = False     #Atributo

    def apresentar(self): #Referencia a esse objeto
        print(f"Carro: {self.marca} {self.modelo}")

    def ligar(self):      #Carro ligado
        self.ligado = True  #Um unico atributo sera usado para dois estados true/false
        print("O carro esta ligado!")

    def desligar(self):   #carro desligado
        self.ligado = False
        print("O carro esta desligado!")

#Variavel recebera a instância da class carro
meu_carro = carro("Toyota", "Corolla")  #Atribui a marca e ao modelo

meu_carro.apresentar() #faz a chamada da funcao que ira apresentar a variavel
sleep(0.5)
meu_carro.ligar()

sleep(0.5)
print(meu_carro.ligado) #Mostra estado do carro

sleep(0.5)
meu_carro.desligar()

        