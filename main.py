from funcoesdacalculadora import *

a = input("Digite uma hora válida: ")
b = input("Digite outra hora válida: ")
operacao = input("Digite o sinal da operação: ")
if operacao == "+" and a is not None and b is not None:
    resultado = somadehoras(a, b)
elif operacao == "-" and a is not None and b is not None:
    resultado = subtracaodehoras(a, b)
else:
    resultado = "Operação inválida."
print(resultado)
