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
    pass # The "pass" command tells Python to do nothing.  It is simply a placeholder for your code.



# Add your user-defined functions here





def main():
# IMPLEMENT YOUR PROGRAM HERE AND CALL OTHERS FUNCTIONS AND PASS PARAMETERS TO FUNCTIONS, WHEN NEEDED.   

    print("Welcome to the Gues The Word Game")# This code line display the welcome of the program. 

    # Create a list of 100 words that are similar enough to work well for this game.
    candidateWords = ['AETHER', 'BADGED', 'BALDER', 'BANDED', 'BANTER', 'BARBER', 'BASHER', 'BATHED', 'BATHER', 'BEAMED', 'BEANED', 'BEAVER', 'BECKET', 'BEDDER', 'BEDELL', 'BEDRID', 'BEEPER', 'BEGGAR', 'BEGGED', 'BELIES', 'BELLES', 'BENDED', 'BENDEE', 'BETTER', 'BLAMER', 'BLOWER', 'BOBBER', 'BOLDER', 'BOLTER', 'BOMBER', 'BOOKER', 'BOPPER', 'BORDER', 'BOSKER', 'BOTHER', 'BOWYER', 'BRACER', 'BUDGER', 'BUMPER', 'BUSHER', 'BUSIER', 'CEILER', 'DEADEN', 'DEAFER', 'DEARER', 'DELVER', 'DENSER', 'DEXTER', 'EVADER', 'GELDED', 'GELDER', 'HEARER', 'HEIFER', 'HERDER', 'HIDDEN', 'JESTER', 'JUDDER', 'KIDDED', 'KIDDER', 'LEANER', 'LEAPER', 'LEASER', 'LEVIED', 'LEVIER', 'LEVIES', 'LIDDED', 'MADDER', 'MEANER', 'MENDER', 'MINDER', 'NEATER', 'NEEDED', 'NESTER', 'PENNER', 'PERTER', 'PEWTER', 'PODDED', 'PONDER', 'RADDED', 'REALER', 'REAVER', 'REEDED', 'REIVER', 'RELIER', 'RENDER', 'SEARER', 'SEDGES', 'SEEDED', 'SEISER', 'SETTER', 'SIDDUR', 'TEENER', 'TEMPER', 'TENDER', 'TERMER', 'VENDER', 'WEDDED', 'WEEDED', 'WELDED', 'YONDER']
    
    # The rest is up to you...
    # See the assignment brief for details of the program requirements.
    # All code inside a Python function must be indented.  

    words =random.sample(candidateWords,8) #Select 8 ramdom words from candidate words
    password =random.choice(words) #Select one of the 8 words as Password

    attempts =4 #maximum attempts allowed is 4

    while attempts >0:
        print("\nAvailable Words")
        for word in words:
            print(word)

         #Ask user to guess
        guess =input("\n Enter your guess:")

         # Check if the guess is correct
        if guess == password:
          print("Correct! You guessed the password.")
          break  # Stop the game

    else:
        # Count how many letters match in the same position
        correct_letters = 0
        for i in range(len(password)):
            if i < len(guess) and guess[i] == password[i]:
                correct_letters += 1

        # Show number of correct letters
        print("Correct letters in the correct position:", correct_letters)

        # Reduce attempts
        attempts -= 1
        print("Attempts left:", attempts)

# If attempts finished and password not guessed
    if attempts == 0:
     print("\nGame Over. The password was:", password)


#Call to main function above. Do not modify or remove this.
main()




  