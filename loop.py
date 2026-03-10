
for letter in "Maria\n":
    print (letter) # Irá imprimir cada letra da palavra "Maria" em uma linha diferente
    

friends = ["John", "Marta", "Maria\n"]
for friend in friends: # a função "for" chamada "friend" irá percorrer cada item da lista "friends"
   print(friend) # Irá imprimir cada nome da lista "friends" em uma linha diferente 
   
# OU:

friends2 = ["Luiz", "Ana", "Carlos\n"]
for index in range (len(friends2)): # a função "for" chamada "index" que recebe a quantidade de elementos no array "friends2" irá percorrer cada índice da lista 
    print(friends2[index]) # Irá imprimir cada nome da lista "friends2" em uma linha diferente, utilizando o índice para acessar cada elemento da lista


for index2 in range (2, 10): # imrpime todos ps números entre 2 e 9, o número 10 não é incluído
    print(index2)
    

for index3 in range(1, 11) : # Imprime os números de 1 a 10, o número 11 não é incluído
    if index3 % 2 == 0: # Se o indíce for par, ou seja, o resto da divisão por 2 for igual a 0, ele irá imprimir o número
        print(f"\n{index3} é par!!")
    else:
        print(f"\n{index3} é ímpar :(") # Se o índice for ímpar, ou seja, o resto da divisão por 2 for diferente de 0, ele irá imprimir a mensagem dizendo que o número é ímpar