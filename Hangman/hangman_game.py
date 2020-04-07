import random  # random choices
from words import word_list  # import list of words


def get_word():  # return a word for our game
   word = random.choice(word_list)
   return word.upper()  # converts all inputs to upper case

# For the interactive gameplay,define play() .
# Lets create unguessed letters as underscore


def play(word):
   # same length as the chosen one initially it will be underscores only for word_completion
   word_completion = '_' * len(word)
   guessed = False
   guessed_letters = []  # holds the letter user guesses
   guessed_words = []  # holds the words user guesses
   # no of tries.. the number of body parts left to be drawn on the hangman before the user looses.
   tries = 6

   # Printing some initial output to help guide the user when the game starts
   print("Let's play Hangman")
   print(display_hangman(tries))  # Initial state of hangman games
   print(word_completion)  # Initial stage of word with all underscores
   print("\n")
   while not guessed and tries > 0:         # Run until the word is guessed or the user runs out of tries
         guess = input("Please guess a letter or word : ").upper()

      # iNSIDE THE LOOP ...THERE ARE...3 POSSIBLE CONDITIONS
      # 1 : WHEN THE USER ENTERS A LETTER
      # 2:WHEN THE USER ENTERS A WORD
      # 3: WHEN THE USER ENTERS SOMETHING ELSE OTHER THAN A SINGLE LETTER OR WORD OF CORRECT LENGTH

      # Guessing a letter

         if len(guess) == 1 and guess.isalpha():
            # Need another conditional block to check whether the letter is already been guessed or Not in the word or Is in the word
               if guess in guessed_letters:  # already the user guessed the word and  repeatition remainder
                  print("You already guessed the letter ", guess)
               elif guess not in word:
                  print(guess, " is not in the word.")
                  # The user did an incorrect guess and hence looses one of his try.
                  tries -= 1
                  # Now store that guessed letter to the list --->  guessed_letters
                  guessed_letters.append(guess)
               # Now the only remaining possibility is that: The user guessed the right word.
               else:
                  print("Good Job ", guess, " is the word !! ")
                  # We need this letter to append on our guessed letters list
                  guessed_letters.append(guess)

                  # Now we have to update our variable --> word_completion to reveal to the user all occcurences of guess
                  # We convert the word_completion from a string to a list
                  # now we are able to index into it.
                  word_as_list = list(word_completion)
                  # Now we need to find all the indices where guess occurs in  the required word
                  # Lets use a list comprehension for that
                  # Here we call ---enumerate--- onward for getting both index and letter for each iteration
                  # We append index to this list if its corresponding letter equals guess
                  indices = [indx for indx, letter in enumerate(
                        word) if letter == guess]
                  # Now we need a for loop to ----replace--- each underscore at index with guess
                  for index in indices:
                        word_as_list[index] = guess
                  # Update word completion with the new changes
                  # Here, the value of --word_completion-- is replaced by the value inside word_as_list  but it is a list , we need it as  a string ---so the .join() function will join those words into a string .
                  # converted back to a string
                  word_completion = "".join(word_as_list)
                  # Also a possibility that the guess has now completed the required word
                  # Lets include an if statement to check this
                  if "_" not in word_completion:
                        guessed = True

      # Condition for Guessing a word
      # We need another conditional block inside the elif statement
      # Condition for checking if whether that already guessed OR if the word is correct OR  incorrect
         elif len(guess) == len(word) and guess.isalpha():
               # Condition if the Guessed word is already guessed by the user
               if guess in guessed_words:
                  print("You already guessed the word", guess)
               elif guess != word:  # incorrect guess
                  print(guess, "is not in the word.")
                  tries -= 1
                  guessed_words.append(guess)
               else: #correct guess
                  guessed = True
                  word_completion=word

         else:
               print("Not a valid guess")
               # After each guess is handled ,we have to print the current state of the hangman
         print(display_hangman(tries))
         #  And also the word
         print(word_completion)
         # New line
         print("\n ")
         #while loop is completed
   if guessed:
      print("Congrats, you guessed the word. You win!")
   else:
      print("Sorry,you ran out of tries. The word was "+ word +" . Don't loose hope.Try Again" )

def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]

#Main Function
def main():
   word = get_word()
   play(word)
   while input("Do you want to play again ? (Y/N)").upper() == "Y":
      word = get_word()
      play(word)

#Now this code is used for running our script on the command prompt
if __name__ == "__main__":
   main()


