# Name:Wijekumara Kavindu Akash  
# Student Number:10687621  

# This file is provided to you as a starting point for the "guess_game.py" program of Assignment 1
# of CSP2151 in Semester 1, 2026.  It mainly provides you with a suitable list of words.
# Please use this file as the basis for your assignment work.  You are not required to reference it.


# Import the random module to allow us to select the word list and password at random.
import random



# The following function receives two words as parameters should return the number of matching letters between them.
# See the assignment brief for details of this function's requirements.
def compareWords(word1, word2):
    # pass The "pass" command tells Python to do nothing.  It is simply a placeholder for your code.
    count = 0
    for i in range(min(len(word1), len(word2))):
        if word1[i] == word2[i]:
            count += 1
    return count
        
# Function to select 8 unique random words from the candidate list       
def selectRandomWords(candidateWords):
    game_words = []  # Initialize empty list for game words
    while len(game_words) < 8:  # Keep adding until we have 8 words
        word = random.choice(candidateWords)  # Pick a random word
        if word not in game_words:  # Ensure no duplicates
            game_words.append(word)
    return game_words

# Function to select one word as the password
def selectPassword(game_words):
    return random.choice(game_words)  # Pick and return a random word

# Function to get user input
def getUserInput(prompt):
    user_input = input(prompt).upper()  # Convert to uppercase to match word list
    return user_input

# Add your user-defined functions here


# Main program
def main():
# IMPLEMENT YOUR PROGRAM HERE AND CALL OTHERS FUNCTIONS AND PASS PARAMETERS TO FUNCTIONS, WHEN NEEDED.   

    print("Welcome to the Guess-The-Word Game.")# This code line display the welcome of the program. 

    # Create a list of 100 words that are similar enough to work well for this game.
    candidateWords = ['AETHER', 'BADGED', 'BALDER', 'BANDED', 'BANTER', 'BARBER', 'BASHER', 'BATHED', 'BATHER', 'BEAMED', 'BEANED', 'BEAVER', 'BECKET', 'BEDDER', 'BEDELL', 'BEDRID', 'BEEPER', 'BEGGAR', 'BEGGED', 'BELIES', 'BELLES', 'BENDED', 'BENDEE', 'BETTER', 'BLAMER', 'BLOWER', 'BOBBER', 'BOLDER', 'BOLTER', 'BOMBER', 'BOOKER', 'BOPPER', 'BORDER', 'BOSKER', 'BOTHER', 'BOWYER', 'BRACER', 'BUDGER', 'BUMPER', 'BUSHER', 'BUSIER', 'CEILER', 'DEADEN', 'DEAFER', 'DEARER', 'DELVER', 'DENSER', 'DEXTER', 'EVADER', 'GELDED', 'GELDER', 'HEARER', 'HEIFER', 'HERDER', 'HIDDEN', 'JESTER', 'JUDDER', 'KIDDED', 'KIDDER', 'LEANER', 'LEAPER', 'LEASER', 'LEVIED', 'LEVIER', 'LEVIES', 'LIDDED', 'MADDER', 'MEANER', 'MENDER', 'MINDER', 'NEATER', 'NEEDED', 'NESTER', 'PENNER', 'PERTER', 'PEWTER', 'PODDED', 'PONDER', 'RADDED', 'REALER', 'REAVER', 'REEDED', 'REIVER', 'RELIER', 'RENDER', 'SEARER', 'SEDGES', 'SEEDED', 'SEISER', 'SETTER', 'SIDDUR', 'TEENER', 'TEMPER', 'TENDER', 'TERMER', 'VENDER', 'WEDDED', 'WEEDED', 'WELDED', 'YONDER']
    
    # The rest is up to you...
    # See the assignment brief for details of the program requirements.
    # All code inside a Python function must be indented.  


    wordList = random.sample(candidateWords, 8) # Select 8 random words from candidate words
    password = random.choice(wordList)          # Select one of the 8 words as Password
    won = False                                 # Boolean to track if the game has been won
    guessesRemaining = 4                        # Maximum guesses allowed is 4

    while guessesRemaining > 0 and not won:

        print("\nPassword is one of these words:")

        # Print the words with numbers (0-7)
        for i, word in enumerate(wordList):
            print(str(i) + ")", word)

        # Show remaining guesses
        print("\nGuesses remaining:", guessesRemaining)

        # Ask user to enter a number
        try:
         guess_index = int(input("Guess (enter 0-7): "))
        except ValueError:                                        # Extra: Validate input to ensure user enters a valid index (0-7) this prevents the program crashing.
         print("Invalid input! Please enter a number between 0 and 7.")
         continue  # skip this iteration and ask again

        # Reduce attempts immediately after the guess
        guessesRemaining -= 1

        # Get the guessed word using the number
        guess_word = wordList[guess_index]

        # Print the chosen word
        print("\n" + guess_word)

        # Check if correct
        if guess_word == password:
            print("Password correct.")
            won = True
            break

        else:
            # Compare letters using the function
            correct_letters = compareWords(password, guess_word)

            print("Password incorrect.")
            print(str(correct_letters) + "/6 correct.")

            # Display Reduce attempts
            print("Attempts left:", guessesRemaining)

    # If attempts finished or password guessed, show final message
    if won:
      print("\nCongratulations. You win!")
    else:
      print("\nYou lose! The password was:", password)

#Call to main function above. Do not modify or remove this.
main()