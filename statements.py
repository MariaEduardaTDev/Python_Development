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
    

