print("    ####### BEM-VINDO A CALC SIMPLES DO JUCI #######     ")
print("Escolha uma opção: "
                    "\n + para adição "
                    "\n - para subtração "
                    "\n x para multiplicação "
                    "\n / para divisão ")
resultado = input("Escolha qual operação deseja fazer: ")
n1 = float(input("Informe o primeiro número: "))
n2 = float(input("Informe o segundo número: "))
if resultado == "+":
    print("O resultado é: ", round(n1 + n2,2))
elif resultado == "-":
    print("O resultado é: ", round(n1 - n2,2))
elif resultado == "*":
    print("O resultado é: ", round(n1 * n2,2))
elif resultado == "/":
    print("O resultado é: ", round(n1 / n2,2))

print("######################## END ###############################")





