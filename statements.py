is_tall = False
is_male = True

if is_tall and is_male:
    print("Wow, you're a really tall men!")
elif is_male and not(is_tall):
    print("Wow, you're a really short men!")
elif is_tall and not(is_male):
    print("You aren't male but are tall! Who are you?!")
else:
    print("You are neither tall nor male! Who are you?!")
    

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3: # "!=" diferente / "==" igual / ">=" maior ou igual / "<=" menor ou igual
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
    

print(max_num(12, 2, -5)) # Chamando a função max_num para encontrar o maior número entre 12, 2 e -5, e imprimir o resultado.
