#Como usar: python Basic.py 10 10 -> isso seria passando o numero 10 duas vezes
import sys  #Biblioteca usada para utilizar parametros passados na linha de codigo
value1 = int(sys.argv[1])
value2 = int(sys.argv[2])

def calc (var1, var2):
    print("A soma fica:",var1+var2)
    print("A subtração fica:",var1-var2)
    print("A multiplicação fica:",var1*var2)
    print("A divisão fica:",var1/var2)
    print("A exponenciação fica:",var1**var2)

calc(value1,value2)