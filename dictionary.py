
monthConversions = {
    1: "January", # Chaves que estão relacionadas à palavras
    2: "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June", 
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(monthConversions["Apr"])
#print(monthConversions["Luv"]) -> Retornna um erro
print(monthConversions.get("Dec")) # O método get() é utilizado para acessar o valor associado a uma chave em um dicionário, e retorna None se a chave não existir, ao invés de gerar um erro.
print(monthConversions.get("Luv")) # Retorna None já que "Luv" não é uma chave presenta no dicionário monthConversions. 
print(monthConversions.get("Hello", "Not a valid key!")) # a função get() pde receber um segundo argumento que é o valor a ser retornado caso a chave não exista no dicionário, evitando assim o retorno de None.
print(monthConversions.get(1)) # Retorna o valor relacionado à chave 1, que é "January".
print(monthConversions.get(2)) # Retorna o valor relacionado à chave 2, que é "February".


