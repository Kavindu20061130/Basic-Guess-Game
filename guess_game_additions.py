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
    user_input = input(prompt)  # Get input from user
    return user_input


# Main program
def main():

    print("Welcome to the Guess-The-Word Game.")# This code line display the welcome of the program. 

    # Create a list of 100 words that are similar enough to work well for this game.
    candidateWords = ['AETHER', 'BADGED', 'BALDER', 'BANDED', 'BANTER', 'BARBER', 'BASHER', 'BATHED', 'BATHER', 'BEAMED', 'BEANED', 'BEAVER', 'BECKET', 'BEDDER', 'BEDELL', 'BEDRID', 'BEEPER', 'BEGGAR', 'BEGGED', 'BELIES', 'BELLES', 'BENDED', 'BENDEE', 'BETTER', 'BLAMER', 'BLOWER', 'BOBBER', 'BOLDER', 'BOLTER', 'BOMBER', 'BOOKER', 'BOPPER', 'BORDER', 'BOSKER', 'BOTHER', 'BOWYER', 'BRACER', 'BUDGER', 'BUMPER', 'BUSHER', 'BUSIER', 'CEILER', 'DEADEN', 'DEAFER', 'DEARER', 'DELVER', 'DENSER', 'DEXTER', 'EVADER', 'GELDED', 'GELDER', 'HEARER', 'HEIFER', 'HERDER', 'HIDDEN', 'JESTER', 'JUDDER', 'KIDDED', 'KIDDER', 'LEANER', 'LEAPER', 'LEASER', 'LEVIED', 'LEVIER', 'LEVIES', 'LIDDED', 'MADDER', 'MEANER', 'MENDER', 'MINDER', 'NEATER', 'NEEDED', 'NESTER', 'PENNER', 'PERTER', 'PEWTER', 'PODDED', 'PONDER', 'RADDED', 'REALER', 'REAVER', 'REEDED', 'REIVER', 'RELIER', 'RENDER', 'SEARER', 'SEDGES', 'SEEDED', 'SEISER', 'SETTER', 'SIDDUR', 'TEENER', 'TEMPER', 'TENDER', 'TERMER', 'VENDER', 'WEDDED', 'WEEDED', 'WELDED', 'YONDER']

    playAgain = True  #  loop control so game can repeat

    while playAgain:

        # Ask difficulty level
        while True:
          difficulty = input("Select difficulty (Easy/Medium/Hard): ").lower()

          if difficulty == "easy":
             guessesRemaining = 5
             break
          elif difficulty == "medium":
             guessesRemaining = 4
             break
          elif difficulty == "hard":
            guessesRemaining = 3
            break
          else:
            print("Invalid difficulty. Please enter Easy, Medium, or Hard.")


        wordList = selectRandomWords(candidateWords) # Select 8 random words from candidate words
        password = selectPassword(wordList)          # Select one of the 8 words as Password
        won = False                                  # Boolean to track if the game has been won

        guessedWords = {}  # Dictionary to store guessed word index and result

        while guessesRemaining > 0 and not won:

            print("\nPassword is one of these words:")

            # Print the words with numbers (1-8 instead of 0-7)
            for i, word in enumerate(wordList):

                # If word was guessed show result
                if i in guessedWords:
                    print(f"{i+1}) {word} [{guessedWords[i]}/6 correct]")
                else:
                    print(f"{i+1}) {word}")

            print("\nGuesses remaining:", guessesRemaining)

            # Input validation to prevent crashing
            try:
                user_input = getUserInput("Guess (enter 1-8): ")
                guess_index = int(user_input) - 1   # Convert to list index

                if guess_index < 0 or guess_index > 7:
                    print("Invalid input. Enter number between 1 and 8.")
                    continue

            except:
                print("Invalid input. Please enter a number.")
                continue

            # Check if already guessed
            if guess_index in guessedWords:
                print("You already guessed that word.")
                continue

            guess_word = wordList[guess_index]

            print("\n" + guess_word)

            guessesRemaining -= 1

            if guess_word == password:
                print("Password correct.")
                won = True
                break

            else:
                correct_letters = compareWords(password, guess_word)

                guessedWords[guess_index] = correct_letters  # Store result

                print("Password incorrect.")
                print(str(correct_letters) + "/6 correct.")

        if won:
            print("\nCongratulations. You win!")
        else:
            print("\nYou lose! The password was:", password)

        # Ask to play again
        again = input("Do you want to play again? (y/n): ").lower()
        if again != "y":
            playAgain = False


#Call to main function above. Do not modify or remove this.
main()