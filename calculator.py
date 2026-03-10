num1 = float(input("Enter the first number: ")) # Recebe o primeiro número no formato de string e convert para tipo float
op = input("Enter the operator: ") # Recebe o operador para a realização do cálculo
num2 = float(input("Enter the second number: ")) # Recebe o segundo número no formato de string e convert para tipo float

if op == "+":
    print(num1 + num2) # Realiza a soma dos dois números e imprime o resultado
elif op == "-":
    print(num1 - num2) # Realiza a subtração dos dois números e imprime o resultado
elif op == "*":
    print(num1 * num2) # Realiza a multiplicação dos dois números e imprime o resultado
elif op == "/" :
    print(num1 / num2) # Realiza a divisão dos dois números e imprime o resultado
else:
    print("Invalid operator!") # Imprime uma mensagem de erro caso o operador seja inválido