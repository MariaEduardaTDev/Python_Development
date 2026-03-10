
'''
secret_word = "python"
guess = ""
guess_count = 0
guess_limit = 3



print("You have 3 chances to guess the secret word. LET'S START THE GAME!")

while guess != secret_word and guess_count < guess_limit:
        guess = input("\nEnter your guess about the secret word: ")
        guess_count += 1
        if guess == secret_word:
            print("\n=============== You win! ===============")
    
print("\nThe game is over!")
'''



# Another version:


secret_word = "code"
guess = ""
guess_count = 0
out_of_guesses = False

print("\nYou have 3 chances to guess the secret word. LET'S START THE GAME!")
while guess != secret_word and not(out_of_guesses):
    if guess != secret_word:
        guess = input("\nEnter your guess about the secret word: ")
    else:
        print("\n=============== You win! ===============")

