coordinates = (4, 10) # As tuplas são semelhantes às listas, mas são imutáveis, ou seja, seus elementos não podem ser alterados após a criação da tupla.
print(coordinates[1]) # Acessando o segundo elemento da tupla usando indexação.
print(coordinates[0])

 #coordinates[0] = 6 # Isso resultará em um erro, pois as tuplas são imutáveis e não permitem a alteração de seus elementos.

coordinates2 = [(1, 2), (3, 4), (5, 6), coordinates] # As tuplas podem conter outros tipos de dados, incluindo outras tuplas.
print(coordinates2) 


