import random
# generate chosen word from list randomly
word_list =['apple', 'orange','cabbage']
chosen_word = random.choice(word_list)
print(chosen_word)

# generate empty dashes for each letter of the chosen word
display = []
for i in range(len(chosen_word)):
  display += '_'
print(display)

#guess letter and check if the letter is in the word chosen
guessed_letter = input("Guess a letter:")
  # every letter has to be compared
for letter in chosen_word: #apple
  if letter == guessed_letter: #a
    print ("match")
  else:
    print('No match')