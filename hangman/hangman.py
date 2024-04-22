import random
from wordlists import words_list
chosen_word = random.choice(words_list)
word_length = len(chosen_word)
display = []
for _ in range(word_length):
    display += "_"

end_of_game = False
lives = 6
from hang_art import logo, stages
print(logo)
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You have already guessed {guess} letter. Try other letter.")
    if guess not in chosen_word:
        lives -= 1
        print(f"You choosed {guess}, that is not in the word. Now you will loose your fucking life.")
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win")
    if lives == 0:
        end_of_game = True
        print("You lose")
    from hang_art import stages
    print(stages[lives])




    
