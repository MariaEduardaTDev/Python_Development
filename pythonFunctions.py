def say_hi(name, age):
    #print("Hii, " + name + "!") ou:
    print(f"Hii, {name}! Are you {age} years old?") # Usando f-string para formatar a string de maneira mais legível.

say_hi("Duda", 18) # Chamando a função say_hi para executar o código dentro dela.
say_hi("João", 32) # Chamando a função say_hi novamente com diferentes argumentos para mostrar como a função pode ser reutilizada.


def cube(num):
    return num ** 3 # A função retorna o resultado do número elevado ao cubo.

print(cube(3)) # Chamando a função cube para calcular o cubo de 3 e imprimir o resultado.