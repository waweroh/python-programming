import random
import hangman_pic
# generate chosen word from list randomly
word_list =['apple', 'orange','cabbage']
lives = 7
chosen_word = random.choice(word_list)
print(chosen_word)

# generate empty dashes for each letter of the chosen word
display = []
for i in range(len(chosen_word)):
  display += '_'
print(display)

game_over = False
while not game_over:
  #guess letter and check if the letter is in the word chosen
  guessed_letter = input("Guess a letter:")
    # every letter has to be compared
  for position in range(len(chosen_word)): #apple #01234 indexed
    letter = chosen_word[position] #a=0, p=1
    if letter == guessed_letter: #a
      display[position] = guessed_letter #display letter at the particular position
  print(display)

  # this is executed for every wrong guess as opposed to one guess being iterated over  if 
  # the if statement was inside the for loop
  if guessed_letter not in chosen_word:
    lives -= 1 
    if lives == 0:
      game_over = True
      print('You Lose ')

  # if you fill all the blanks and find the word
  if '_' not in display:
    game_over = True
    print('You win')

  print(hangman_pic.stages[lives])

  