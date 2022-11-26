#Code by Ekta Kapase
import random
import hangman_words
import hangman_art
  
print(hangman_art.logo)

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
hang_pos = len(hangman_art.stages)
# print(f'The solution is {chosen_word}.')

display = []
for _ in range(word_length):
  display += "_"

over = "no"
guessed_letters = []
guess = ""

while over != "yes":
  guessed_letters += guess  
  guess = input("Guess a letter: ").lower()
  print("")
  for position in range(word_length):   
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter
      if "_" not in display:
        over = "yes"      
    
  if guess not in display:
    if guess in guessed_letters:
      print("You've aready guessed this letter. Guess another letter.")
    else:
      print(f"You guessed letter {guess}, that's not in the word. You lose a life. ")
      print(hangman_art.stages[hang_pos - 1])
      hang_pos -= 1
      if hang_pos == 0:
        over = "yes"
  else:
    print("Your guess is correct.\n")
  print(f"{' '.join(display)}\n")
  
if over == "yes":
  print(f"The word is {chosen_word}.")
  
if "_" not in display:
  print("You win!")
elif hang_pos == 0:
  print("You lose!")
