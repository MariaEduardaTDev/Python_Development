
def raise_to_power (base_num, pow_num):
    result = 1 # A variável "result" é inicializada com o valor 1, que será usada para armazenar o resultado da operação de potência.
    for index in range(pow_num):
        result = result * base_num # A cada iteração do loop, o valor de "result" é multiplicado pelo "base_num", acumulando o resultado da potência.
    return result
    
#print(raise_to_power(3, 3)) 
print("\n\n =======================POWER FUNCTION =======================\n")
print(raise_to_power(int(input("Base: ")), int(input("Expoente: ")))) # O usuário é solicitado a inserir o número base e o expoente, que são convertidos para inteiros e passados como argumentos para a função "raise_to_power". O resultado é então impresso na tela.