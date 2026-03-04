import math

character_name = "Maria Eduarda"
character_age = 18.00

print("\nA nova funcionária " + character_name + " é extremamente capacitada como desenvolvedora de automações, e olha que ela só tem " + str(character_age) + " anos!!\n") 
# A variável de idade foi tranformada de um número para uma string, para que o código funcione, pois não é possível concatenar um número com uma string. 


phrase = "oláaa, tudo bem? "
print(phrase.lower()) # O método lower() é utilizado para converter todas as letras de uma string para minúsculas.
print(phrase.upper()) # O método upper() é utilizado para converter todas as letras de uma string para maiúsculas.
print(phrase.isupper()) # O método isupper() é utilizado para verificar se todas as letras de uma string estão em maiúsculas. Ele retorna True se todas as letras estiverem em maiúsculas e False caso contrário.
print(phrase.islower()) # O método islower() é utilizado para verificar se todas as letras de uma string estão em minúsculas. Ele retorna True se todas as letras estiverem em minúsculas e False caso contrário.
print(phrase.replace("oláaa, tudo bem?", "hello, how ur doing??\n"))


name = "Jane"
print(name[0], name.index("J")) 
print(name[1], name.index ("a"))
print(name[2], name.index("n"))
print(name[3], name.index("e"))
 # O método index() é utilizado para encontrar a posição de um caractere específico em uma string. Ele retorna o índice de cada caractere solicitado.
# Esse método retorna o caractere correspondente à posição do índice especificado.


num = -5
print(abs(num)) # O método abs() é utilizado para obter o valor absoluto de um número, ou seja, a distância do número em relação a zero.
print(pow(num, 2)) # O método pow() é utilizado para calcular a potência de um número. Ele recebe dois argumentos: o número base e o expoente.
print(max(num, 10, 0.1, 20, 615557445)) # O método max() é utilizado para encontrar o maior valor entre dois ou mais números.
print(min(num, 10, -11, 20, 615557445)) # O método min() é utilizado para encontrar o menor valor entre dois ou mais números.
print(round(31.621651484615616514684165616)) # O método round() é utilizado para arredondar um número para o inteiro mais próximo. Se o número tiver uma parte decimal de 0.5 ou mais, ele arredonda para cima; caso contrário, arredonda para baixo.


name2 = input("\n Digite o seu nome: ")
age2 = input("Digite a sua idade: ") # A idade será recebida como string
curso = input("Digite o curso que está fazendo ou pretende fazer: ")
print("Olá " + name2 + ", seja muito bem-vindo(a)!\n")
if(int(age2) >= 18 and int(age2) <=25): # Para comparar com números é necessário a conversão para o tipo inteiro
    print("Muito feliz de saber que um jovem como você de " + age2 + " anos está se dedicando tão cedo para aprender " + curso + "!!\n")
elif(int(age2)< 18):
    print("Que legal que você tem apenas " + age2 + " anos e já está se interessando por " + curso + "!!\n")
else:
    print("Parabéns pela sua dedicação e que independente da idade, o importanto é nunca deixar de fazermos o que queremos!!\n")
    


color = input("Dgite uma cor (no plural): ")
color2 = input("\nDigite uma segunda cor (no plural)): ")
nome3 = input("\nDigite o seu nome:")
print("Agora vamos para o nosso poema!!\n\n")
print("Violetas são " + color)
print("\nRosas são " + color2)
print("\nSe você se chama " + nome3 + " então vai tomar banho!!\n")


humanBody = ["Hair", "shoulders", "knees", " and toes", "knees", " and toes"]
for i in range(len(humanBody)):
    print(humanBody[i])
print(humanBody[1:4]) # O código acima imprime os elementos do índice 1 ao 3 da lista humanBody


humanBody2 = ["And eyes", "and ears", "and mouth", "and nose"]
humanBody.extend(humanBody2) # O método extend() é utilizado para adicionar os elementos de uma lista a outra lista.
print(humanBody)


humanBody.remove(" and toes") # O método remove() é utilizado para remover a primeira ocorrência de um elemento específico em uma lista.

humanBody.pop(1) # O método pop() é utilizado para remover um elemento de uma lista com base em seu índice. 
print(humanBody)

print(humanBody.index("knees")) # O método index() é utilizado para encontrar a posição de um elemento específico em uma lista. 
#print(humanBody.index("hi"))  -> Retorno: ValueError: "list.index(x): x not in list"
print(humanBody.count("knees") ) # O método count() é utilizado para contar o número de vezes que um elemento específico aparece em uma lista.

humanBody.clear() # O método clear() é utilizado para remover todos os elementos de uma lista, deixando-a vazia.

humanBody.append("But i'm a creep!") # O método append() é utilizado para adicionar um elemento ao final de uma lista.
print(humanBody)

random = [1, 2, 5, 7, 10, -2, 0, 3, 4, 6, 8, 9]
random.sort() # O método sort() é utilizado para ordenar os elementos de uma lista em ordem crescente.
print(random)

random.reverse() # O método reverse() é utilizado para inverter a ordem dos elementos de uma lista. 
print(random)

random2 = random.copy() # O método copy() é utilizado para criar uma cópia de uma lista. 
print(random2)





































































