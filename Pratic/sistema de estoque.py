class Roupa:
    def __init__(self, nome, quant):
        self.nome = nome
        self.quant = quant
    
    def comprar(self):
        if self.quant > 0:
            self.quant -= 1
            print("Você comprou!")
        else:
            print(f"{self.nome} fora de estoque!")
    
    def abastecer(self, qtd):
        self.quant += qtd
        print(f"{self.nome} Unidades reabastecida!")

    def ver_estoque(self):
        print(f"{self.nome}: {self.quant}")

if __name__ == '__main__':

    qtd_blusa = int(input("Quantas blusas tem no estoque?"))
    qtd_short = int(input("Quantas short tem no estoque?"))
    qtd_calca = int(input("Quantas calca tem no estoque?"))

    blusa = Roupa("Blusa", qtd_blusa)
    short = Roupa("Short", qtd_blusa)
    calca = Roupa("Calça", qtd_blusa)

    

    blusa.comprar()
    blusa.ver_estoque()

    short.abastecer(10)
    short.ver_estoque()