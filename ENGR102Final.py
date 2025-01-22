# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name:       Jacob Jones
# Section:    575
# Assignment: Final Project
# Date:       12/05/2022

# Main Menu ####################################################################################################################################################

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("Howdy! Welcome to Jacob's ENGR 102 final project!")

username = input("Enter your name or preferred username: ")

strOptions = ["1", "2", "3", "4"]
intOptions = [1, 2, 3, 4]

print("\n\n\n\n\n\n\n\n\n\n")

while True:
    print("\n\n\n\nWelcome to the Main Menu!")
    print("""\nThere are three games to play:
      
          
☆ Option 1 is MyWordle™ ☆

General Concept of MyWordle™: MyWordle™ is a word guessing game where you have 12 attempts to guess the secret 
word. Hints will be given based on if the correct letter is in the correct slot, if the correct letter is in the
word, or if the letter is in the word at all. (More specific instructions will be given once the game is selected.)
        
☆ Option 2 is Rock Paper Scissors (vs. AI or another player) ☆

General Concept of Rock Paper Scissors: This game is the same as normal old fashioned Rock Paper Scissors. 
You can play against a friend by selecting human as an opponent,or you can play against an AI by selecting computer as an opponent.
Rock beats scissors, scissors beats paper, and paper beats rock. (More specific instructions will be given once the game is selected.)
        
☆ Option 3 is Aggie Trivia ☆

General Concept of Aggie Trivia: This game is like any other trivia game but with a focus on Texas A&M. 
There will be multiple choice questions displayed that are Aggie related. Get 100 % (12/12) of the questions
right and win a special prize. (More specific instructions will be given once the game is selected.)

☆ Option 4 is The Exit ☆

This is the designated exit main menu option. Selecting this option will exit the entire program.

☆ Attention ☆

All game results will be displayed after the user has quit or completed the game. The main menu will appear
immediately after the game is finished/quit. To see the results, either scroll up in the console, or make the 
console window longer vertically. Thanks and have fun!
    """)
    
    option = input("\nWhich game do you want to play right now? (Enter option number 1, 2, 3, or 4 to quit): ")
    
    while option not in strOptions and option not in intOptions: # Checks the inputted item, if not in list, user is prompted to change input.
        print("\n   Enter only option numbers 1, 2, 3, or 4 to quit)")
        option = input("\nWhich game do you want to play right now? (Enter option number 1, 2, 3, or 4 to quit): ")
        
    option = int(option)
        
    while True: # Uses a try except statement to check if the inputted guess is composed of only letters.
        try:    
            option = int(option) 
            break
        except:
            print("\n   Enter only option numbers 1, 2, 3, or 4 to quit)")
            option = input("\nWhich game do you want to play right now? (Enter option number 1, 2, 3, or 4 to quit): ")
        
    while option not in strOptions and option not in intOptions: # Checks the inputted item, if not in list, user is prompted to change input.
        print("\n   Enter only option numbers 1, 2, 3, or 4 to quit)")
        option = int(input("\nWhich game do you want to play right now? (Enter option number 1, 2, 3, or 4 to quit): "))
        
    option = int(option)
    
    if option == 1: # Wordle Game (Done)

# Wordle Instructions ##########################################################################################################################################

        print("""\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nHowdy again! This game is called MyWordle™ because I made it. 
It is basically the same as New York Times' Wordle, but in this game, there is a guess limit of 12, for the 12th man of course.
    


☆ How to play ☆
Guess any 5 letter word and press the 'Enter' key and the console will output the result of your guess.
The word bank is the same as the one New York Times uses in their game Wordle.



☆ Tip ☆
None of the words in the word bank have more than one of the same letter. This should make the game easier.
  

  
☆ Key ☆
If there is a '🟥' in a letter slot that means the letter you entered is not in the word at all. 
If there is a '🟨' that means the letter is in the word, just not in that slot. 
Finally, if the letter you inputted is in the correct slot, the letter will appear in the correct slot in the hint output.
 

   
☆ How to Exit Game ☆
Feel free to enter the word 'quit' at any time to exit the game. 
Using either of these commands will take you back to the main menu screen. Have fun!


              """)

################################################################################################################################################################
        
        import random # Imports random module. #!!! New Thing!
        
        wordfile = open("wordbank.txt", "r+") # Opens the word bank for MyWordle.
        wordbank = wordfile.readlines()       # Creates a list of all the words from the word bank.
        words = []                            # Creates a python list of the word. (This is for the requirements in case the one above doesn't satisfy.)

        for word in range(len(wordbank)):
            words.append(wordbank[word])
            
        secret = random.choice(words)         # Picks a random word from the word bank. 
        secret = secret.upper()               # Turns the secret word to all upper cases for aesthetics.
        numGuesses = 0                        # Initializes the number of guesses to 0.
        correct = False                       # Initializes correct as False.
        
        def checkGuesses(secretWord, inputtedGuess):
            """This function checks the inputted guess with the chosen word."""
            slot = 0
            hint = ""
            for letter in inputtedGuess: # This loop scans the inputted word and gives the correct hint based on the guess.
                if letter == secretWord[slot]:
                    hint += letter
                elif letter in secretWord:
                    hint += "🟨" # Yellows is a wrong guess for the slot, but right for the word.
                else:
                    hint += "🟥" # Red is a completely wrong guess.
                slot += 1
            print(hint)
            return hint == f"{secret[0]}{secret[1]}{secret[2]}{secret[3]}{secret[4]}" 
        
        while numGuesses < 12 and not correct:
            guess = input("\nInput a 5 letter word and press enter (input quit to exit): ").upper()
            
            if guess == 'QUIT': # Quit message
                print(f"\nHey {username}, try harder next time you stinkin' quitter. The correct word was: {secret}")
                wordfile.close()
                break

            while len(guess) != 5: # Checks the inputted guess length and gives according messages to the user.
                if len(guess) > 5:
                    print("\n   Use a shorter word.")
                elif len(guess) < 5:
                    print("\n   Use a longer word.")
                guess = input("\nInput a 5 letter word and press enter: ").upper()
                
            while True: # Uses a try except statement to check if the inputted guess is composed of only letters.
                try:    # This try except is designed to only work when the exception is met.
                    guess = int(guess) 
                    print("\n   Use only letters, no numbers allowed.")
                    guess = input("\nInput a 5 letter word and press enter: ").upper()
                except:
                    break
                
            while len(guess) != 5: # Checks the inputted guess length and gives according messages to the user.
                if len(guess) > 5: # This is to ensure the user has a letter guess that is also the correct length.
                    print("\n   Use a shorter word.")
                elif len(guess) < 5:
                    print("\n   Use a longer word.")
                guess = input("\nInput a 5 letter word and press enter: ").upper()
                
            print("\n   You guessed:", guess,"\n")
            numGuesses += 1
            print("\nHint: ")
            correct = checkGuesses(secret, guess) # Checks if guess is right or wrong and produces the hint.
            
        if correct: # Outputs the victory message.
            print("\n☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
            print(f"\n   The word was: {secret}                             ")
            print(f"   Great job {username}! You did it! You guessed the word in {numGuesses} tries!\n")
            print("☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
            wordfile.close()
            
        elif not correct: # Outputs the losing message.
            print("\n☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
            print(f"\n   Nice try {username}! You tried your best it! The word was: {secret}\n")
            print("☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
            wordfile.close()

    elif option == 2: # Rock Paper Scissors Game (Done)

# Rock Paper Scissors (Human/AI) Instructions ##################################################################################################################

        print("""\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nHowdy again! This game is called Rock Paper Scissors (vs. AI or another player). 
It is basically the same as a normal game Rock Paper Scissors except you can play against a friend (human) or a computer (AI). 
There is also a match length option where you can choose the match set (Best of 3, Best of 7, or Unlimited).



☆ How to play ☆
Enter Rock, Paper, Scissors, or quit (to quit), then the opponent (Human or AI) will choose their input and the winner will be evaluated
through a few functions. The result will be outputted to the console along with the current score. After you are don playing, input
quit to exit the game. Depending on the most commonly used item (Rock/Paper/Scissors) a picture will be displayed.
    


☆ Attention ☆
Open the "Plots" window in the console to view the post game analysis! 
Must have one of each item (Rock/Paper/Scissors) to earn post game analysis output!



☆ How to Exit Game ☆
Feel free to enter the word 'quit' at any time to exit the game. 
Using this command will take you back to the main menu screen. Have fun!


              """)

################################################################################################################################################################      
       
        oppTypes = ["HUMAN", "AI"]
        
        opponentType = input("\nDo you want to play against another human or an AI? (Enter HUMAN or AI): ").upper()
        
        while opponentType not in oppTypes: # Checks the inputted item, if not in list, user is prompted to change input.
            print("\n   Enter only AI or Human.")
            opponentType = input("\nDo you want to play against another human or an AI? (Enter HUMAN or AI): ").upper()
            
        while True: # Uses a try except statement to check if the inputted guess is composed of only letters.
            try:    # This try except is designed to only work when the exception is met.
                opponentType = int(opponentType) 
                print("\n   Enter only AI or Human.")
                opponentType = input("\nDo you want to play against another human or an AI? (Enter HUMAN or AI): ").upper()
            except:
                break
            
        while opponentType not in oppTypes: # Checks the inputted item, if not in list, user is prompted to change input.
            print("\n   Enter only AI or Human.")
            opponentType = input("\nDo you want to play against another human or an AI? (Enter HUMAN or AI): ").upper()
            
        intMatchLengths = [3, 7, 0]
        strMatchLengths = ["3", "7", "0"]
        
        matchLen = input("\nEnter the length of match you want to play (3 for Best of 3, 7 for Best of 7, or 0 for unlimited): ")
        
        while matchLen not in strMatchLengths and matchLen not in intMatchLengths: # Checks the inputted item, if not in list, user is prompted to change input.
            print("\n   Enter only numbers 3, 7, or 0.")
            matchLen = input("\nEnter the length of match you want to play (3 for Best of 3, 7 for Best of 7, or 0 for unlimited): ")  
            
        matchLen = int(matchLen)
            
        while True: # Uses a try except statement to check if the inputted guess is composed of only letters.
            try:    
                matchLen = int(matchLen) 
                break
            except:
                print("\n   Enter only numbers 3, 7, or 0.")
                matchLen = input("\nEnter the length of match you want to play (3 for Best of 3, 7 for Best of 7, or 0 for unlimited): ")  
            
        while matchLen not in strMatchLengths and matchLen not in intMatchLengths: # Checks the inputted item, if not in list, user is prompted to change input.
            print("\n   Enter only numbers 3, 7, or 0.")
            matchLen = input("\nEnter the length of match you want to play (3 for Best of 3, 7 for Best of 7, or 0 for unlimited): ")
            
        matchLen = int(matchLen)
            
        if matchLen == 0:
            matchLen = 999
        
        import random       # Imports random module.
        import pandas as pd # Imports pandas module. #!!! New Thing!
        import matplotlib.pyplot as plt # Imports matplotlib.
        colors = ({"Rock": "hotpink", "Paper": "yellow", "Scissors": "turquoise"})
        itemList = ["ROCK", "PAPER", "SCISSORS"]
        userScore = 0 # User score.
        oppScore = 0  # Opponent score.
        winner = 0    # -1 == Opp win, 0 == Tie, 1 == User win.
        rockNum = 0
        paperNum = 0
        scissorsNum = 0

        def whoWon(userItem, oppItem):
            winner = 0
            rockNum = 0
            paperNum = 0
            scissorsNum = 0
            """This function decides who won the round."""
            if userItem == "ROCK" and oppItem == "SCISSORS":
                rockNum += 1
                scissorsNum += 1
                winner = 1
            elif userItem == "PAPER" and oppItem == "ROCK":
                paperNum += 1
                rockNum += 1
                winner = 1
            elif userItem == "SCISSORS" and oppItem == "PAPER":
                scissorsNum += 1
                paperNum += 1
                winner = 1
            elif userItem == "ROCK" and oppItem == "PAPER":
                rockNum += 1
                paperNum += 1
                winner = -1
            elif userItem == "PAPER" and oppItem == "SCISSORS":
                paperNum += 1
                scissorsNum += 1
                winner = -1
            elif userItem == "SCISSORS" and oppItem == "ROCK":
                scissorsNum += 1
                rockNum += 1
                winner = -1
            elif userItem == oppItem:
                if userItem == "ROCK":
                    rockNum += 2
                    winner = 0
                elif userItem == "PAPER":
                    paperNum += 2
                    winner = 0
                elif userItem == "SCISSORS":
                    scissorsNum += 2
                    winner = 0
            return winner, rockNum, paperNum, scissorsNum
        
        if opponentType == "HUMAN" and matchLen == 3:
            
            while True:
                
                userItem = input("\n\nPlayer 1 enter an item (Rock/Paper/Scissors or quit to exit): ").upper()
                
                if userItem == "QUIT":
                     if userScore > oppScore:
                         print("\n\n\nThe results are in...")
                         print()
                         print("\n☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
                         print(f"\n   Player 1 Won! Great job! The final score was {userScore} - {oppScore}!\n")
                         print("☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
                         if rockNum != 0 or scissorsNum != 0 or paperNum != 0:
                             # Created dataframe using pandas module.
                             plt.title("Post Game Analysis")
                             df = pd.DataFrame({"Items": ["Rock", "Paper", "Scissors"],"Frequency": [rockNum, paperNum, scissorsNum]})
                             # Plots a pie chart using matplotlib module.
                             plt.pie(df["Frequency"], labels = df["Items"], colors = colors.values())
                             plt.show()
                             break
                         break
                     elif userScore < oppScore:
                         print("\n\n\nThe results are in...")
                         print()
                         print("\n☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
                         print(f"\n   Player 2 won! Great job! The final score was {userScore} - {oppScore}!\n")
                         print("☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
                         if rockNum != 0 or scissorsNum != 0 or paperNum != 0:
                             # Created dataframe using pandas module.
                             plt.title("Post Game Analysis")
                             df = pd.DataFrame({"Items": ["Rock", "Paper", "Scissors"],"Frequency": [rockNum, paperNum, scissorsNum]})
                             # Plots a pie chart using matplotlib module.
                             plt.pie(df["Frequency"], labels = df["Items"], colors = colors.values())
                             plt.show()
                             break
                         break
                     elif userScore == oppScore:
                         print("\n\n\nThe results are in...")
                         print()
                         print("\n☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
                         print(f"\n   It was a tie! Nice try! The final score was {userScore} - {oppScore}!\n")
                         print("☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
                         if rockNum != 0 or scissorsNum != 0 or paperNum != 0:
                             # Created dataframe using pandas module.
                             plt.title("Post Game Analysis")
                             df = pd.DataFrame({"Items": ["Rock", "Paper", "Scissors"],"Frequency": [rockNum, paperNum, scissorsNum]})
                             # Plots a pie chart using matplotlib module.
                             plt.pie(df["Frequency"], labels = df["Items"], colors = colors.values())
                             plt.show()
                             break
                         break
                
                while userItem not in itemList: # Checks the inputted item, if not in list, user is prompted to change input.
                    print("\n   Enter only rock, paper, or scissors.")
                    userItem = input("\nPlayer 1 enter an item (Rock/Paper/Scissors): ").upper()
                   
                while True: # Uses a try except statement to check if the inputted guess is composed of only letters.
                    try:    # This try except is designed to only work when the exception is met.
                        userItem = int(userItem) 
                        print("\n   Enter only rock, paper, or scissors.")
                        userItem = input("\nPlayer 1 enter an item (Rock/Paper/Scissors): ").upper()
                    except:
                        break
                    
                while userItem not in itemList: # Checks the inputted item, if not in list, user is prompted to change input.
                    print("\n   Enter only rock, paper, or scissors.")
                    userItem = input("\nPlayer 1 enter an item (Rock/Paper/Scissors): ").upper()
                    
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                
                oppItem = input("Player 2 enter an item (Rock/Paper/Scissors or quit to exit): ").upper()
                
                if oppItem == "QUIT":
                     if userScore > oppScore:
                         print("\n\n\nThe results are in...")
                         print()
                         print("\n☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
                         print(f"\n   Player 1 Won! Great job! The final score was {userScore} - {oppScore}!\n")
                         print("☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
                         if rockNum != 0 or scissorsNum != 0 or paperNum != 0:
                             # Created dataframe using pandas module.
                             plt.title("Post Game Analysis")
                             df = pd.DataFrame({"Items": ["Rock", "Paper", "Scissors"],"Frequency": [rockNum, paperNum, scissorsNum]})
                             # Plots a pie chart using matplotlib module.
                             plt.pie(df["Frequency"], labels = df["Items"], colors = colors.values())
                             plt.show()
                             break
                         break
                     elif userScore < oppScore:
                         print("\n\n\nThe results are in...")
                         print()
                         print("\n☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
                         print(f"\n   Player 2 won! Great job! The final score was {userScore} - {oppScore}!\n")
                         print("☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
                         if rockNum != 0 or scissorsNum != 0 or paperNum != 0:
                             # Created dataframe using pandas module.
                             plt.title("Post Game Analysis")
                             df = pd.DataFrame({"Items": ["Rock", "Paper", "Scissors"],"Frequency": [rockNum, paperNum, scissorsNum]})
                             # Plots a pie chart using matplotlib module.
                             plt.pie(df["Frequency"], labels = df["Items"], colors = colors.values())
                             plt.show()
                             break
                         break
                     elif userScore == oppScore:
                         print("\n\n\nThe results are in...")
                         print()
                         print("\n☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
                         print(f"\n   It was a tie! Nice try! The final score was {userScore} - {oppScore}!\n")
                         print("☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
                         if rockNum != 0 or scissorsNum != 0 or paperNum != 0:
                             # Created dataframe using pandas module.
                             plt.title("Post Game Analysis")
                             df = pd.DataFrame({"Items": ["Rock", "Paper", "Scissors"],"Frequency": [rockNum, paperNum, scissorsNum]})
                             # Plots a pie chart using matplotlib module.
                             plt.pie(df["Frequency"], labels = df["Items"], colors = colors.values())
                             plt.show()
                             break
                         break
                
                while oppItem not in itemList: # Checks the inputted item, if not in list, user is prompted to change input.
                    print("\n   Enter only rock, paper, or scissors.")
                    oppItem = input("\nPlayer 2 enter an item (Rock/Paper/Scissors): ").upper()
                   
                while True: # Uses a try except statement to check if the inputted guess is composed of only letters.
                    try:    # This try except is designed to only work when the exception is met.
                        oppItem = int(userItem) 
                        print("\n   Enter only rock, paper, or scissors.")
                        oppItem = input("\nPlayer 2 enter an item (Rock/Paper/Scissors): ").upper()
                    except:
                        break
                    
                while oppItem not in itemList: # Checks the inputted item, if not in list, user is prompted to change input.
                    print("\n   Enter only rock, paper, or scissors.")
                    oppItem = input("\nPlayer 2 enter an item (Rock/Paper/Scissors): ").upper()
                
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    
                winner = whoWon(userItem, oppItem)[0]
                rockNum += whoWon(userItem, oppItem)[1]
                paperNum += whoWon(userItem, oppItem)[2]
                scissorsNum += whoWon(userItem, oppItem)[3]
                
                if winner == -1:   # If opponent wins.
                    print(f"\n   Player 1 lost this round. Player 2 chose {oppItem} and Player 1 chose {userItem}.")
                    oppScore += 1
                    if userScore > oppScore and userScore != 2 and oppScore != 2:
                        print(f"\n   The current score is {userScore} - {oppScore}. Player 1 is in the lead.")
                    elif userScore < oppScore and userScore != 2 and oppScore != 2:
                        print(f"\n   The current score is {userScore} - {oppScore}. Player 2 is in the lead.")
                    elif userScore == oppScore and userScore != 2 and oppScore != 2:
                        print(f"\n   The current score is {userScore} - {oppScore}. It's a tie game.")
                elif winner == 1:  # If user wins.
                    print(f"\n   Player 1 won this round. Player 2 chose {oppItem} and Player 1 chose {userItem}.")
                    userScore += 1
                    if userScore > oppScore and userScore != 2 and oppScore != 2:
                        print(f"\n   The current score is {userScore} - {oppScore}.  Player 1 is in the lead.")
                    elif userScore < oppScore and userScore != 2 and oppScore != 2:
                        print(f"\n   The current score is {userScore} - {oppScore}. Player 2 is in the lead.")
                    elif userScore == oppScore and userScore != 2 and oppScore != 2:
                        print(f"\n   The current score is {userScore} - {oppScore}. It's a tie game.")
                elif winner == 0:  # If a draw, do nothing.
                    print(f"\n   This round was a draw. Player 2 chose {oppItem} and Player 1 chose {userItem}.")
                    if userScore > oppScore and userScore != 2 and oppScore != 2:
                        print(f"\n   The current score is {userScore} - {oppScore}.  Player 1 is in the lead.")
                    elif userScore < oppScore and userScore != 2 and oppScore != 2:
                        print(f"\n   The current score is {userScore} - {oppScore}. Player 2 is in the lead.")
                    elif userScore == oppScore and userScore != 2 and oppScore != 2:
                        print(f"\n   The current score is {userScore} - {oppScore}. It's a tie game.")  
                        
                if userScore == 2:                    
                    print("\n\n\nThe results are in...")
                    print()
                    print("\n☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
                    print(f"\n   Player 1 won! Great job! The final score was {userScore} - {oppScore}!\n")
                    print("☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
                    # Created dataframe using pandas module.
                    plt.title("Post Game Analysis")
                    df = pd.DataFrame({"Items": ["Rock", "Paper", "Scissors"],"Frequency": [rockNum, paperNum, scissorsNum]})
                    # Plots a pie chart using matplotlib module.
                    plt.pie(df["Frequency"], labels=df["Items"], colors = colors.values())
                    plt.show()
                    break
                    
                elif oppScore == 2:
                    print("\n\n\nThe results are in...")
                    print()
                    print("\n☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
                    print(f"\n   Player 2 won! Great job! The final score was {userScore} - {oppScore}!\n")
                    print("☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
                    # Created dataframe using pandas module.
                    plt.title("Post Game Analysis")
                    df = pd.DataFrame({"Items": ["Rock", "Paper", "Scissors"],"Frequency": [rockNum, paperNum, scissorsNum]})
                    # Plots a pie chart using matplotlib module.
                    plt.pie(df["Frequency"], labels=df["Items"], colors = colors.values())
                    plt.show()
                    break
            
        elif opponentType == "HUMAN" and matchLen == 7:

            while True:
                
                userItem = input("\n\nPlayer 1 enter an item (Rock/Paper/Scissors or quit to exit): ").upper()
                
                if userItem == "QUIT":
                    if userScore > oppScore:
                        print("\n\n\nThe results are in...")
                        print()
                        print("\n☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
                        print(f"\n   Player 1 Won! Great job! The final score was {userScore} - {oppScore}!\n")
                        print("☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
                        if rockNum != 0 or scissorsNum != 0 or paperNum != 0:
                            # Created dataframe using pandas module.
                            plt.title("Post Game Analysis")
                            df = pd.DataFrame({"Items": ["Rock", "Paper", "Scissors"],"Frequency": [rockNum, paperNum, scissorsNum]})
                            # Plots a pie chart using matplotlib module.
                            plt.pie(df["Frequency"], labels = df["Items"], colors = colors.values())
                            plt.show()
                            break
                        break
                    elif userScore < oppScore:
                        print("\n\n\nThe results are in...")
                        print()
                        print("\n☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
                        print(f"\n   Player 2 won! Great job! The final score was {userScore} - {oppScore}!\n")
                        print("☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
                        if rockNum != 0 or scissorsNum != 0 or paperNum != 0:
                            # Created dataframe using pandas module.
                            plt.title("Post Game Analysis")
                            df = pd.DataFrame({"Items": ["Rock", "Paper", "Scissors"],"Frequency": [rockNum, paperNum, scissorsNum]})
                            # Plots a pie chart using matplotlib module.
                            plt.pie(df["Frequency"], labels = df["Items"], colors = colors.values())
                            plt.show()
                            break
                        break
                    elif userScore == oppScore:
                        print("\n\n\nThe results are in...")
                        print()
                        print("\n☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
                        print(f"\n   It was a tie! Nice try! The final score was {userScore} - {oppScore}!\n")
                        print("☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
                        if rockNum != 0 or scissorsNum != 0 or paperNum != 0:
                            # Created dataframe using pandas module.
                            plt.title("Post Game Analysis")
                            df = pd.DataFrame({"Items": ["Rock", "Paper", "Scissors"],"Frequency": [rockNum, paperNum, scissorsNum]})
                            # Plots a pie chart using matplotlib module.
                            plt.pie(df["Frequency"], labels = df["Items"], colors = colors.values())
                            plt.show()
                            break
                        break
                
                while userItem not in itemList: # Checks the inputted item, if not in list, user is prompted to change input.
                    print("\n   Enter only rock, paper, or scissors.")
                    userItem = input("\nPlayer 1 enter an item (Rock/Paper/Scissors): ").upper()
                   
                while True: # Uses a try except statement to check if the inputted guess is composed of only letters.
                    try:    # This try except is designed to only work when the exception is met.
                        userItem = int(userItem) 
                        print("\n   Enter only rock, paper, or scissors.")
                        userItem = input("\nPlayer 1 enter an item (Rock/Paper/Scissors): ").upper()
                    except:
                        break
                    
                while userItem not in itemList: # Checks the inputted item, if not in list, user is prompted to change input.
                    print("\n   Enter only rock, paper, or scissors.")
                    userItem = input("\nPlayer 1 enter an item (Rock/Paper/Scissors): ").upper()
                    
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                
                oppItem = input("Player 2 enter an item (Rock/Paper/Scissors or quit to exit): ").upper()
                
                if oppItem == "QUIT":
                    if userScore > oppScore:
                        print("\n\n\nThe results are in...")
                        print()
                        print("\n☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
                        print(f"\n   Player 1 Won! Great job! The final score was {userScore} - {oppScore}!\n")
                        print("☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
                        if rockNum != 0 or scissorsNum != 0 or paperNum != 0:
                            # Created dataframe using pandas module.
                            plt.title("Post Game Analysis")
                            df = pd.DataFrame({"Items": ["Rock", "Paper", "Scissors"],"Frequency": [rockNum, paperNum, scissorsNum]})
                            # Plots a pie chart using matplotlib module.
                            plt.pie(df["Frequency"], labels = df["Items"], colors = colors.values())
                            plt.show()
                            break
                        break
                    elif userScore < oppScore:
                        print("\n\n\nThe results are in...")
                        print()
                        print("\n☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
                        print(f"\n   Player 2 won! Great job! The final score was {userScore} - {oppScore}!\n")
                        print("☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
                        if rockNum != 0 or scissorsNum != 0 or paperNum != 0:
                            # Created dataframe using pandas module.
                            plt.title("Post Game Analysis")
                            df = pd.DataFrame({"Items": ["Rock", "Paper", "Scissors"],"Frequency": [rockNum, paperNum, scissorsNum]})
                            # Plots a pie chart using matplotlib module.
                            plt.pie(df["Frequency"], labels = df["Items"], colors = colors.values())
                            plt.show()
                            break
                        break
                    elif userScore == oppScore:
                        print("\n\n\nThe results are in...")
                        print()
                        print("\n☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
                        print(f"\n   It was a tie! Nice try! The final score was {userScore} - {oppScore}!\n")
                        print("☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
                        if rockNum != 0 or scissorsNum != 0 or paperNum != 0:
                            # Created dataframe using pandas module.
                            plt.title("Post Game Analysis")
                            df = pd.DataFrame({"Items": ["Rock", "Paper", "Scissors"],"Frequency": [rockNum, paperNum, scissorsNum]})
                            # Plots a pie chart using matplotlib module.
                            plt.pie(df["Frequency"], labels = df["Items"], colors = colors.values())
                            plt.show()
                            break
                        break
                
                while oppItem not in itemList: # Checks the inputted item, if not in list, user is prompted to change input.
                    print("\n   Enter only rock, paper, or scissors.")
                    oppItem = input("\nPlayer 2 enter an item (Rock/Paper/Scissors): ").upper()
                   
                while True: # Uses a try except statement to check if the inputted guess is composed of only letters.
                    try:    # This try except is designed to only work when the exception is met.
                        oppItem = int(userItem) 
                        print("\n   Enter only rock, paper, or scissors.")
                        oppItem = input("\nPlayer 2 enter an item (Rock/Paper/Scissors): ").upper()
                    except:
                        break
                    
                while oppItem not in itemList: # Checks the inputted item, if not in list, user is prompted to change input.
                    print("\n   Enter only rock, paper, or scissors.")
                    oppItem = input("\nPlayer 2 enter an item (Rock/Paper/Scissors): ").upper()
                
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    
                    
                winner = whoWon(userItem, oppItem)[0]
                rockNum += whoWon(userItem, oppItem)[1]
                paperNum += whoWon(userItem, oppItem)[2]
                scissorsNum += whoWon(userItem, oppItem)[3]
                
                if winner == -1:   # If opponent wins.
                    print(f"\n   Player 1 lost this round. Player 2 chose {oppItem} and Player 1 chose {userItem}.")
                    oppScore += 1
                    if userScore > oppScore and userScore != 4 and oppScore != 4:
                        print(f"\n   The current score is {userScore} - {oppScore}. Player 1 is in the lead.")
                    elif userScore < oppScore and userScore != 4 and oppScore != 4:
                        print(f"\n   The current score is {userScore} - {oppScore}. Player 2 is in the lead.")
                    elif userScore == oppScore and userScore != 4 and oppScore != 4:
                        print(f"\n   The current score is {userScore} - {oppScore}. It's a tie game.")
                elif winner == 1:  # If user wins.
                    print(f"\n   Player 1 won this round. Player 2 chose {oppItem} and Player 1 chose {userItem}.")
                    userScore += 1
                    if userScore > oppScore and userScore != 4 and oppScore != 4:
                        print(f"\n   The current score is {userScore} - {oppScore}.  Player 1 is in the lead.")
                    elif userScore < oppScore and userScore != 4 and oppScore != 4:
                        print(f"\n   The current score is {userScore} - {oppScore}. Player 2 is in the lead.")
                    elif userScore == oppScore and userScore != 4 and oppScore != 4:
                        print(f"\n   The current score is {userScore} - {oppScore}. It's a tie game.")
                elif winner == 0:  # If a draw, do nothing.
                    print(f"\n   This round was a draw. Player 2 chose {oppItem} and Player 1 chose {userItem}.")
                    if userScore > oppScore and userScore != 4 and oppScore != 4:
                        print(f"\n   The current score is {userScore} - {oppScore}.  Player 1 is in the lead.")
                    elif userScore < oppScore and userScore != 4 and oppScore != 4:
                        print(f"\n   The current score is {userScore} - {oppScore}. Player 2 is in the lead.")
                    elif userScore == oppScore and userScore != 4 and oppScore != 4:
                        print(f"\n   The current score is {userScore} - {oppScore}. It's a tie game.")  
                        
                if userScore == 4:                    
                    print("\n\n\nThe results are in...")
                    print()
                    print("\n☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
                    print(f"\n   Player 1 won! Great job! The final score was {userScore} - {oppScore}!\n")
                    print("☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
                    # Created dataframe using pandas module.
                    plt.title("Post Game Analysis")
                    df = pd.DataFrame({"Items": ["Rock", "Paper", "Scissors"],"Frequency": [rockNum, paperNum, scissorsNum]})
                    # Plots a pie chart using matplotlib module.
                    plt.pie(df["Frequency"], labels=df["Items"], colors = colors.values())
                    plt.show()
                    break
                
                elif oppScore == 4:
                    print("\n\n\nThe results are in...")
                    print()
                    print("\n☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
                    print(f"\n   Player 2 won! Great job! The final score was {userScore} - {oppScore}!\n")
                    print("☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
                    # Created dataframe using pandas module.
                    plt.title("Post Game Analysis")
                    df = pd.DataFrame({"Items": ["Rock", "Paper", "Scissors"],"Frequency": [rockNum, paperNum, scissorsNum]})
                    # Plots a pie chart using matplotlib module.
                    plt.pie(df["Frequency"], labels=df["Items"], colors = colors.values())
                    plt.show()
                    break
                
        elif opponentType == "HUMAN" and matchLen == 999:

            while True:
                
                userItem = input("\n\nPlayer 1 enter an item (Rock/Paper/Scissors or quit to exit): ").upper()
                
                if userItem == "QUIT":
                    if userScore > oppScore:
                        print("\n\n\nThe results are in...")
                        print()
                        print("\n☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
                        print(f"\n   Player 1 Won! Great job! The final score was {userScore} - {oppScore}!\n")
                        print("☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
                        if rockNum != 0 or scissorsNum != 0 or paperNum != 0:
                            # Created dataframe using pandas module.
                            plt.title("Post Game Analysis")
                            df = pd.DataFrame({"Items": ["Rock", "Paper", "Scissors"],"Frequency": [rockNum, paperNum, scissorsNum]})
                            # Plots a pie chart using matplotlib module.
                            plt.pie(df["Frequency"], labels = df["Items"], colors = colors.values())
                            plt.show()
                            break
                        break
                    elif userScore < oppScore:
                        print("\n\n\nThe results are in...")
                        print()
                        print("\n☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
                        print(f"\n   Player 2 won! Great job! The final score was {userScore} - {oppScore}!\n")
                        print("☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
                        if rockNum != 0 or scissorsNum != 0 or paperNum != 0:
                            # Created dataframe using pandas module.
                            plt.title("Post Game Analysis")
                            df = pd.DataFrame({"Items": ["Rock", "Paper", "Scissors"],"Frequency": [rockNum, paperNum, scissorsNum]})
                            # Plots a pie chart using matplotlib module.
                            plt.pie(df["Frequency"], labels = df["Items"], colors = colors.values())
                            plt.show()
                            break
                        break
                    elif userScore == oppScore:
                        print("\n\n\nThe results are in...")
                        print()
                        print("\n☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
                        print(f"\n   It was a tie! Nice try! The final score was {userScore} - {oppScore}!\n")
                        print("☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
                        if rockNum != 0 or scissorsNum != 0 or paperNum != 0:
                            # Created dataframe using pandas module.
                            plt.title("Post Game Analysis")
                            df = pd.DataFrame({"Items": ["Rock", "Paper", "Scissors"],"Frequency": [rockNum, paperNum, scissorsNum]})
                            # Plots a pie chart using matplotlib module.
                            plt.pie(df["Frequency"], labels = df["Items"], colors = colors.values())
                            plt.show()
                            break
                        break
                
                while userItem not in itemList: # Checks the inputted item, if not in list, user is prompted to change input.
                    print("\n   Enter only rock, paper, or scissors.")
                    userItem = input("\nPlayer 1 enter an item (Rock/Paper/Scissors): ").upper()
                   
                while True: # Uses a try except statement to check if the inputted guess is composed of only letters.
                    try:    # This try except is designed to only work when the exception is met.
                        userItem = int(userItem) 
                        print("\n   Enter only rock, paper, or scissors.")
                        userItem = input("\nPlayer 1 enter an item (Rock/Paper/Scissors): ").upper()
                    except:
                        break
                    
                while userItem not in itemList: # Checks the inputted item, if not in list, user is prompted to change input.
                    print("\n   Enter only rock, paper, or scissors.")
                    userItem = input("\nPlayer 1 enter an item (Rock/Paper/Scissors): ").upper()
                    
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                
                oppItem = input("Player 2 enter an item (Rock/Paper/Scissors or quit to exit): ").upper()
                
                if oppItem == "QUIT":
                    if userScore > oppScore:
                        print("\n\n\nThe results are in...")
                        print()
                        print("\n☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
                        print(f"\n   Player 1 Won! Great job! The final score was {userScore} - {oppScore}!\n")
                        print("☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
                        if rockNum != 0 or scissorsNum != 0 or paperNum != 0:
                            # Created dataframe using pandas module.
                            plt.title("Post Game Analysis")
                            df = pd.DataFrame({"Items": ["Rock", "Paper", "Scissors"],"Frequency": [rockNum, paperNum, scissorsNum]})
                            # Plots a pie chart using matplotlib module.
                            plt.pie(df["Frequency"], labels = df["Items"], colors = colors.values())
                            plt.show()
                            break
                        break
                    elif userScore < oppScore:
                        print("\n\n\nThe results are in...")
                        print()
                        print("\n☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
                        print(f"\n   Player 2 won! Great job! The final score was {userScore} - {oppScore}!\n")
                        print("☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
                        if rockNum != 0 or scissorsNum != 0 or paperNum != 0:
                            # Created dataframe using pandas module.
                            plt.title("Post Game Analysis")
                            df = pd.DataFrame({"Items": ["Rock", "Paper", "Scissors"],"Frequency": [rockNum, paperNum, scissorsNum]})
                            # Plots a pie chart using matplotlib module.
                            plt.pie(df["Frequency"], labels = df["Items"], colors = colors.values())
                            plt.show()
                            break
                        break
                    elif userScore == oppScore:
                        print("\n\n\nThe results are in...")
                        print()
                        print("\n☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
                        print(f"\n   It was a tie! Nice try! The final score was {userScore} - {oppScore}!\n")
                        print("☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
                        if rockNum != 0 or scissorsNum != 0 or paperNum != 0:
                            # Created dataframe using pandas module.
                            plt.title("Post Game Analysis")
                            df = pd.DataFrame({"Items": ["Rock", "Paper", "Scissors"],"Frequency": [rockNum, paperNum, scissorsNum]})
                            # Plots a pie chart using matplotlib module.
                            plt.pie(df["Frequency"], labels = df["Items"], colors = colors.values())
                            plt.show()
                            break
                        break
                
                while oppItem not in itemList: # Checks the inputted item, if not in list, user is prompted to change input.
                    print("\n   Enter only rock, paper, or scissors.")
                    oppItem = input("\nPlayer 2 enter an item (Rock/Paper/Scissors): ").upper()
                   
                while True: # Uses a try except statement to check if the inputted guess is composed of only letters.
                    try:    # This try except is designed to only work when the exception is met.
                        oppItem = int(userItem) 
                        print("\n   Enter only rock, paper, or scissors.")
                        oppItem = input("\nPlayer 2 enter an item (Rock/Paper/Scissors): ").upper()
                    except:
                        break
                    
                while oppItem not in itemList: # Checks the inputted item, if not in list, user is prompted to change input.
                    print("\n   Enter only rock, paper, or scissors.")
                    oppItem = input("\nPlayer 2 enter an item (Rock/Paper/Scissors): ").upper()
                
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    
                    
                winner = whoWon(userItem, oppItem)[0]
                rockNum += whoWon(userItem, oppItem)[1]
                paperNum += whoWon(userItem, oppItem)[2]
                scissorsNum += whoWon(userItem, oppItem)[3]
                
                if winner == -1:   # If opponent wins.
                    print(f"\n   Player 1 lost this round. Player 2 chose {oppItem} and Player 1 chose {userItem}.")
                    oppScore += 1
                    if userScore > oppScore:
                        print(f"\n   The current score is {userScore} - {oppScore}. Player 1 is in the lead.")
                    elif userScore < oppScore:
                        print(f"\n   The current score is {userScore} - {oppScore}. Player 2 is in the lead.")
                    elif userScore == oppScore:
                        print(f"\n   The current score is {userScore} - {oppScore}. It's a tie game.")
                elif winner == 1:  # If user wins.
                    print(f"\n   Player 1 won this round. Player 2 chose {oppItem} and Player 1 chose {userItem}.")
                    userScore += 1
                    if userScore > oppScore:
                        print(f"\n   The current score is {userScore} - {oppScore}.  Player 1 is in the lead.")
                    elif userScore < oppScore:
                        print(f"\n   The current score is {userScore} - {oppScore}. Player 2 is in the lead.")
                    elif userScore == oppScore:
                        print(f"\n   The current score is {userScore} - {oppScore}. It's a tie game.")
                elif winner == 0:  # If a draw, do nothing.
                    print(f"\n   This round was a draw. Player 2 chose {oppItem} and Player 1 chose {userItem}.")
                    if userScore > oppScore:
                        print(f"\n   The current score is {userScore} - {oppScore}.  Player 1 is in the lead.")
                    elif userScore < oppScore:
                        print(f"\n   The current score is {userScore} - {oppScore}. Player 2 is in the lead.")
                    elif userScore == oppScore:
                        print(f"\n   The current score is {userScore} - {oppScore}. It's a tie game.")  
                
                
        elif opponentType == "AI" and matchLen == 3:
            
            while True:
                
                oppItem = random.choice(itemList)
                userItem = input("\n\nEnter an item (Rock/Paper/Scissors or quit to exit): ").upper()
                
                if userItem == "QUIT":
                    if userScore > oppScore:
                        print("\n\n\nThe results are in...")
                        print()
                        print("\n☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
                        print(f"\n   You won! Great job! The final score was {userScore} - {oppScore}!\n")
                        print("☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
                        if rockNum != 0 or scissorsNum != 0 or paperNum != 0:
                            # Created dataframe using pandas module.
                            plt.title("Post Game Analysis")
                            df = pd.DataFrame({"Items": ["Rock", "Paper", "Scissors"],"Frequency": [rockNum, paperNum, scissorsNum]})
                            # Plots a pie chart using matplotlib module.
                            plt.pie(df["Frequency"], labels = df["Items"], colors = colors.values())
                            plt.show()
                            break
                        break
                    elif userScore < oppScore:
                        print("\n\n\nThe results are in...")
                        print()
                        print("\n☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
                        print(f"\n   You lost! Nice try! The final score was {userScore} - {oppScore}!\n")
                        print("☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
                        if rockNum != 0 or scissorsNum != 0 or paperNum != 0:
                            # Created dataframe using pandas module.
                            plt.title("Post Game Analysis")
                            df = pd.DataFrame({"Items": ["Rock", "Paper", "Scissors"],"Frequency": [rockNum, paperNum, scissorsNum]})
                            # Plots a pie chart using matplotlib module.
                            plt.pie(df["Frequency"], labels = df["Items"], colors = colors.values())
                            plt.show()
                            break
                        break
                    elif userScore == oppScore:
                        print("\n\n\nThe results are in...")
                        print()
                        print("\n☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
                        print(f"\n   You tied! Nice try! The final score was {userScore} - {oppScore}!\n")
                        print("☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
                        if rockNum != 0 or scissorsNum != 0 or paperNum != 0:
                            # Created dataframe using pandas module.
                            plt.title("Post Game Analysis")
                            df = pd.DataFrame({"Items": ["Rock", "Paper", "Scissors"],"Frequency": [rockNum, paperNum, scissorsNum]})
                            # Plots a pie chart using matplotlib module.
                            plt.pie(df["Frequency"], labels = df["Items"], colors = colors.values())
                            plt.show()
                            break
                        break
                    
                while userItem not in itemList: # Checks the inputted item, if not in list, user is prompted to change input.
                    print("\n   Enter only rock, paper, or scissors.")
                    userItem = input("\nEnter an item (Rock/Paper/Scissors): ").upper()
                   
                while True: # Uses a try except statement to check if the inputted guess is composed of only letters.
                    try:    # This try except is designed to only work when the exception is met.
                        userItem = int(userItem) 
                        print("\n   Enter only rock, paper, or scissors.")
                        userItem = input("\nEnter an item (Rock/Paper/Scissors): ").upper()
                    except:
                        break
                    
                while userItem not in itemList: # Checks the inputted item, if not in list, user is prompted to change input.
                    print("\n   Enter only rock, paper, or scissors.")
                    userItem = input("\nEnter an item (Rock/Paper/Scissors): ").upper()
                
                winner = whoWon(userItem, oppItem)[0]
                rockNum += whoWon(userItem, oppItem)[1]
                paperNum += whoWon(userItem, oppItem)[2]
                scissorsNum += whoWon(userItem, oppItem)[3]
                
                if winner == -1:   # If opponent wins.
                    print(f"\n   You lost this round. The AI chose {oppItem} and you chose {userItem}.")
                    oppScore += 1
                    if userScore > oppScore and userScore != 2 and oppScore != 2:
                        print(f"\n   The current score is {userScore} - {oppScore}. You're in the lead.")
                    elif userScore < oppScore and userScore != 2 and oppScore != 2:
                        print(f"\n   The current score is {userScore} - {oppScore}. You're losing to the AI.")
                    elif userScore == oppScore and userScore != 2 and oppScore != 2:
                        print(f"\n   The current score is {userScore} - {oppScore}. It's a tie game.")
                elif winner == 1:  # If user wins.
                    print(f"\n   You won this round. The AI chose {oppItem} and you chose {userItem}.")
                    userScore += 1
                    if userScore > oppScore and userScore != 2 and oppScore != 2:
                        print(f"\n   The current score is {userScore} - {oppScore}. You're in the lead.")
                    elif userScore < oppScore and userScore != 2 and oppScore != 2:
                        print(f"\n   The current score is {userScore} - {oppScore}. You're losing to the AI.")
                    elif userScore == oppScore and userScore != 2 and oppScore != 2:
                        print(f"\n   The current score is {userScore} - {oppScore}. It's a tie game.")
                elif winner == 0:  # If a draw, do nothing.
                    print(f"\n   This round was a draw. The AI chose {oppItem} and you chose {userItem}.")
                    if userScore > oppScore and userScore != 2 and oppScore != 2:
                        print(f"\n   The current score is {userScore} - {oppScore}. You're in the lead.")
                    elif userScore < oppScore and userScore != 2 and oppScore != 2:
                        print(f"\n   The current score is {userScore} - {oppScore}. You're losing to the AI.")
                    elif userScore == oppScore and userScore != 2 and oppScore != 2:
                        print(f"\n   The current score is {userScore} - {oppScore}. It's a tie game.")  
                        
                if userScore == 2:                    
                    print("\n\n\nThe results are in...")
                    print()
                    print("\n☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
                    print(f"\n   You won! Great Job! The final score was {userScore} - {oppScore}!\n")
                    print("☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
                    # Created dataframe using pandas module.
                    plt.title("Post Game Analysis")
                    df = pd.DataFrame({"Items": ["Rock", "Paper", "Scissors"],"Frequency": [rockNum, paperNum, scissorsNum]})
                    # Plots a pie chart using matplotlib module.
                    plt.pie(df["Frequency"], labels=df["Items"], colors = colors.values())
                    plt.show()
                    break
                    
                elif oppScore == 2:
                    print("\n\n\nThe results are in...")
                    print()
                    print("\n☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
                    print(f"\n   You lost! Nice try! The final score was {userScore} - {oppScore}!\n")
                    print("☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
                    # Created dataframe using pandas module.
                    plt.title("Post Game Analysis")
                    df = pd.DataFrame({"Items": ["Rock", "Paper", "Scissors"],"Frequency": [rockNum, paperNum, scissorsNum]})
                    # Plots a pie chart using matplotlib module.
                    plt.pie(df["Frequency"], labels=df["Items"], colors = colors.values())
                    plt.show()
                    break
                    
                     
        elif opponentType == "AI" and matchLen == 7:
            
            while True:
                
                oppItem = random.choice(itemList)
                userItem = input("\n\nEnter an item (Rock/Paper/Scissors or quit to exit): ").upper()
                
                if userItem == "QUIT":
                    if userScore > oppScore:
                        print("\n\n\nThe results are in...")
                        print()
                        print("\n☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
                        print(f"\n   You won! Great job! The final score was {userScore} - {oppScore}!\n")
                        print("☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
                        if rockNum != 0 or scissorsNum != 0 or paperNum != 0:
                            # Created dataframe using pandas module.
                            plt.title("Post Game Analysis")
                            df = pd.DataFrame({"Items": ["Rock", "Paper", "Scissors"],"Frequency": [rockNum, paperNum, scissorsNum]})
                            # Plots a pie chart using matplotlib module.
                            plt.pie(df["Frequency"], labels = df["Items"], colors = colors.values())
                            plt.show()
                            break
                        break
                    elif userScore < oppScore:
                        print("\n\n\nThe results are in...")
                        print()
                        print("\n☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
                        print(f"\n   You lost! Nice try! The final score was {userScore} - {oppScore}!\n")
                        print("☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
                        if rockNum != 0 or scissorsNum != 0 or paperNum != 0:
                            # Created dataframe using pandas module.
                            plt.title("Post Game Analysis")
                            df = pd.DataFrame({"Items": ["Rock", "Paper", "Scissors"],"Frequency": [rockNum, paperNum, scissorsNum]})
                            # Plots a pie chart using matplotlib module.
                            plt.pie(df["Frequency"], labels = df["Items"], colors = colors.values())
                            plt.show()
                            break
                        break
                    elif userScore == oppScore:
                        print("\n\n\nThe results are in...")
                        print()
                        print("\n☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
                        print(f"\n   You tied! Nice try! The final score was {userScore} - {oppScore}!\n")
                        print("☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
                        if rockNum != 0 or scissorsNum != 0 or paperNum != 0:
                            # Created dataframe using pandas module.
                            plt.title("Post Game Analysis")
                            df = pd.DataFrame({"Items": ["Rock", "Paper", "Scissors"],"Frequency": [rockNum, paperNum, scissorsNum]})
                            # Plots a pie chart using matplotlib module.
                            plt.pie(df["Frequency"], labels = df["Items"], colors = colors.values())
                            plt.show()
                            break
                        break
                    
                while userItem not in itemList: # Checks the inputted item, if not in list, user is prompted to change input.
                    print("\n   Enter only rock, paper, or scissors.")
                    userItem = input("\nEnter an item (Rock/Paper/Scissors): ").upper()
                   
                while True: # Uses a try except statement to check if the inputted guess is composed of only letters.
                    try:    # This try except is designed to only work when the exception is met.
                        userItem = int(userItem) 
                        print("\n   Enter only rock, paper, or scissors.")
                        userItem = input("\nEnter an item (Rock/Paper/Scissors): ").upper()
                    except:
                        break
                    
                while userItem not in itemList: # Checks the inputted item, if not in list, user is prompted to change input.
                    print("\n   Enter only rock, paper, or scissors.")
                    userItem = input("\nEnter an item (Rock/Paper/Scissors): ").upper()
                
                winner = whoWon(userItem, oppItem)[0]
                rockNum += whoWon(userItem, oppItem)[1]
                paperNum += whoWon(userItem, oppItem)[2]
                scissorsNum += whoWon(userItem, oppItem)[3]
                
                if winner == -1:   # If opponent wins.
                    print(f"\n   You lost this round. The AI chose {oppItem} and you chose {userItem}.")
                    oppScore += 1
                    if userScore > oppScore and userScore != 4 and oppScore != 4:
                        print(f"\n   The current score is {userScore} - {oppScore}. You're in the lead.")
                    elif userScore < oppScore and userScore != 4 and oppScore != 4:
                        print(f"\n   The current score is {userScore} - {oppScore}. You're losing to the AI.")
                    elif userScore == oppScore and userScore != 4 and oppScore != 4:
                        print(f"\n   The current score is {userScore} - {oppScore}. It's a tie game.")
                elif winner == 1:  # If user wins.
                    print(f"\n   You won this round. The AI chose {oppItem} and you chose {userItem}.")
                    userScore += 1
                    if userScore > oppScore and userScore != 4 and oppScore != 4:
                        print(f"\n   The current score is {userScore} - {oppScore}. You're in the lead.")
                    elif userScore < oppScore and userScore != 4 and oppScore != 4:
                        print(f"\n   The current score is {userScore} - {oppScore}. You're losing to the AI.")
                    elif userScore == oppScore and userScore != 4 and oppScore != 4:
                        print(f"\n   The current score is {userScore} - {oppScore}. It's a tie game.")
                elif winner == 0:  # If a draw, do nothing.
                    print(f"\n   This round was a draw. The AI chose {oppItem} and you chose {userItem}.")
                    if userScore > oppScore and userScore != 4 and oppScore != 4:
                        print(f"\n   The current score is {userScore} - {oppScore}. You're in the lead.")
                    elif userScore < oppScore and userScore != 4 and oppScore != 4:
                        print(f"\n   The current score is {userScore} - {oppScore}. You're losing to the AI.")
                    elif userScore == oppScore and userScore != 4 and oppScore != 4:
                        print(f"\n   The current score is {userScore} - {oppScore}. It's a tie game.")  
                        
                if userScore == 4:                    
                    print("\n\n\nThe results are in...")
                    print()
                    print("\n☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
                    print(f"\n   You won! Great Job! The final score was {userScore} - {oppScore}!\n")
                    print("☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
                    # Created dataframe using pandas module.
                    plt.title("Post Game Analysis")
                    df = pd.DataFrame({"Items": ["Rock", "Paper", "Scissors"],"Frequency": [rockNum, paperNum, scissorsNum]})
                    # Plots a pie chart using matplotlib module.
                    plt.pie(df["Frequency"], labels=df["Items"], colors = colors.values())
                    plt.show()
                    break

                    
                elif oppScore == 4:
                    print("\n\n\nThe results are in...")
                    print()
                    print("\n☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
                    print(f"\n   You lost! Nice try! The final score was {userScore} - {oppScore}!\n")
                    print("☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
                    # Created dataframe using pandas module.
                    plt.title("Post Game Analysis")
                    df = pd.DataFrame({"Items": ["Rock", "Paper", "Scissors"],"Frequency": [rockNum, paperNum, scissorsNum]})
                    # Plots a pie chart using matplotlib module.
                    plt.pie(df["Frequency"], labels=df["Items"], colors = colors.values())
                    plt.show()
                    break

            
        elif opponentType == "AI" and matchLen == 999:
            
            while True:
                
                oppItem = random.choice(itemList)
                userItem = input("\n\nEnter an item (Rock/Paper/Scissors or quit): ").upper()
                
                if userItem == "QUIT":
                    if userScore > oppScore:
                        print("\n\n\nThe results are in...")
                        print()
                        print("\n☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
                        print(f"\n   You won! Great job! The final score was {userScore} - {oppScore}!\n")
                        print("☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
                        if rockNum != 0 or scissorsNum != 0 or paperNum != 0:
                            # Created dataframe using pandas module.
                            plt.title("Post Game Analysis")
                            df = pd.DataFrame({"Items": ["Rock", "Paper", "Scissors"],"Frequency": [rockNum, paperNum, scissorsNum]})
                            # Plots a pie chart using matplotlib module.
                            plt.pie(df["Frequency"], labels = df["Items"], colors = colors.values())
                            plt.show()
                            break
                        break
                    elif userScore < oppScore:
                        print("\n\n\nThe results are in...")
                        print()
                        print("\n☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
                        print(f"\n   You lost! Nice try! The final score was {userScore} - {oppScore}!\n")
                        print("☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
                        if rockNum != 0 or scissorsNum != 0 or paperNum != 0:
                            # Created dataframe using pandas module.
                            plt.title("Post Game Analysis")
                            df = pd.DataFrame({"Items": ["Rock", "Paper", "Scissors"],"Frequency": [rockNum, paperNum, scissorsNum]})
                            # Plots a pie chart using matplotlib module.
                            plt.pie(df["Frequency"], labels = df["Items"], colors = colors.values())
                            plt.show()
                            break
                        break
                    elif userScore == oppScore:
                        print("\n\n\nThe results are in...")
                        print()
                        print("\n☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
                        print(f"\n   You tied! Nice try! The final score was {userScore} - {oppScore}!\n")
                        print("☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
                        if rockNum != 0 or scissorsNum != 0 or paperNum != 0:
                            # Created dataframe using pandas module.
                            plt.title("Post Game Analysis")
                            df = pd.DataFrame({"Items": ["Rock", "Paper", "Scissors"],"Frequency": [rockNum, paperNum, scissorsNum]})
                            # Plots a pie chart using matplotlib module.
                            plt.pie(df["Frequency"], labels = df["Items"], colors = colors.values())
                            plt.show()
                            break
                        break
                    
                while userItem not in itemList: # Checks the inputted item, if not in list, user is prompted to change input.
                    print("\n   Enter only rock, paper, or scissors. (Input quit to exit.)")
                    userItem = input("\nEnter an item (Rock/Paper/Scissors or quit): ").upper()
                   
                while True: # Uses a try except statement to check if the inputted guess is composed of only letters.
                    try:    # This try except is designed to only work when the exception is met.
                        userItem = int(userItem) 
                        print("\n   Enter only rock, paper, or scissors. (Input quit to exit.)")
                        userItem = input("\nEnter an item (Rock/Paper/Scissors or quit): ").upper()
                    except:
                        break
                    
                while userItem not in itemList: # Checks the inputted item, if not in list, user is prompted to change input.
                    print("\n   Enter only rock, paper, or scissors. (Input quit to exit.)")
                    userItem = input("\nEnter an item (Rock/Paper/Scissors or quit): ").upper()
                
                winner = whoWon(userItem, oppItem)[0]
                rockNum += whoWon(userItem, oppItem)[1]
                paperNum += whoWon(userItem, oppItem)[2]
                scissorsNum += whoWon(userItem, oppItem)[3]
                
                if winner == -1:   # If opponent wins.
                    print(f"\n   You lost this round. The AI chose {oppItem} and you chose {userItem}.")
                    oppScore += 1
                    if userScore > oppScore:
                        print(f"\n   The current score is {userScore} - {oppScore}. You're in the lead.")
                    elif userScore < oppScore:
                        print(f"\n   The current score is {userScore} - {oppScore}. You're losing to the AI.")
                    elif userScore == oppScore:
                        print(f"\n   The current score is {userScore} - {oppScore}. It's a tie game.")
                elif winner == 1:  # If user wins.
                    print(f"\n   You won this round. The AI chose {oppItem} and you chose {userItem}.")
                    userScore += 1
                    if userScore > oppScore:
                        print(f"\n   The current score is {userScore} - {oppScore}. You're in the lead.")
                    elif userScore < oppScore:
                        print(f"\n   The current score is {userScore} - {oppScore}. You're losing to the AI.")
                    elif userScore == oppScore:
                        print(f"\n   The current score is {userScore} - {oppScore}. It's a tie game.")
                elif winner == 0:  # If a draw, do nothing.
                    print(f"\n   This round was a draw. The AI chose {oppItem} and you chose {userItem}.")
                    if userScore > oppScore:
                        print(f"\n   The current score is {userScore} - {oppScore}. You're in the lead.")
                    elif userScore < oppScore:
                        print(f"\n   The current score is {userScore} - {oppScore}. You're losing to the AI.")
                    elif userScore == oppScore:
                        print(f"\n   The current score is {userScore} - {oppScore}. It's a tie game.")  
                        
                                
    elif option == 3: # Aggie Trivia Game (Done)
    
# Aggie Trivia Instructions ###############################################################################################################

        print("""\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nHowdy again! This game is called Aggie Trivia. 
It is basically the same as normal a normal trivia game but the questions are focused on Texas A&M culture.
    


☆ How to play ☆ 
Enter a letter A, B, C, or D corresponding to the correct answer choice of the question that is being displayed. 
You get 3 guesses per question, so you should do good. If you get a 100% (12/12) you'll win a special prize, so try your best!



☆ Attention ☆
Open the "Plots" window in the console to see the special prize! 
    


☆ How to Exit Game ☆
Feel free to enter the word 'quit' at any time to exit the game. 
Using this command will take you back to the main menu screen. Have fun!


              """)
###########################################################################################################################################
        import random # Imports random module.
        from matplotlib import pyplot as plt  # Imports pyplot from matplotlib.
        from matplotlib import image as mpimg # Imports image from matplotlib. #!!! New Thing!
    
        # Creates a list of 12 questions.
        questions = ["Which section of ENGR 102 is the best?", "How many libraries are on the Texas A&M - College Station campus?",
                    "What is the name of the Texas A&M mascot?","What breed of dog is Texas A&M's mascot?", 
                    "What is the highest score Texas A&M has scored in one football game?", 
                    "Who is the last person to with the Heisman Trophy from Texas A&M?", "What does A&M stand for in Texas A&M?",
                    "What year was Texas A&M founded?", "What number mascot is currently at Texas A&M?", 
                    "Who is Texas A&M's football stadium named after?", "Who was the original 12th man?", 
                    "What significant tree is on the Texas A&M campus?"]
        
        # Creates an answer bank of 4 questions for each of the 12 questions.
        answerbank = [["A: 472", "B: 573", "C: 474", "D: 575"], ["A: 8", "B: 5", "C: 3", "D: 9"], ["A: Reveille", "B: Bucky", "C: Smokey", "D: Bevo"], 
                      ["A: Golden Retriever", "B: German Shepard", "C: Rough Collie", "D: Great Dane"], ["A: 68", "B: 74", "C: 82", "D: 55"],
                      ["A: Johnny Manziel", "B: John David Crow", "C: Ray Rice", "D: Marcus Mariota"], 
                      ["A: Awesome and Magnificent", "B: Agricultural and Mechanical", "C: Academic and Majestic", "D: Alcatraz and Melodic"],
                      ["A: 1922", "B: 1888", "C: 1802", "D: 1876"], ["A: 7", "B: 9", "C: 10", "D: 8"], 
                      ["A: Edwin Jackson Kyle", "B: Kyler Korver", "C: Kyle Kuzma", "D: Kyle Lowry"], 
                      ["A: Lyle Lovett", "B: Rick Perry", "C: E. King Gill", "D: Steven Swanson"],
                      ["A: Bonsai Tree", "B: Century Tree", "C: Pine Tree", "D: The Giant Sequoia Tree"]]
        
        # Creates a dictionary containing the correct answers to each question using the list and list of lists created above. 
        answerkey = {questions[0] : "D", questions[1] : "B", questions[2] : "A", questions[3] : "C", 
                     questions[4] : "B", questions[5] : "A", questions[6] : "B",
                     questions[7] : "D", questions[8] : "C", questions[9] : "A", 
                     questions[10] : "C", questions[11] : "B"}
          
        # Q1 = "Which section of ENGR 102 is the best?"                                 # 575
        # Q2 = "How many libraries are on the Texas A&M - College Station campus?"      # 5
        # Q3 = "What is the name of the Texas A&M mascot?"                              # Reveille
        # Q4 = "What breed of dog is Texas A&M's mascot?"                               # Rough Collie
        # Q5 = "What is the highest score Texas A&M has scored in one football game?"   # 74
        # Q6 = "Who is the last person to with the Heisman Trophy from Texas A&M?"      # Johnny Manziel
        # Q7 = "What does A&M stand for in Texas A&M?"                                  # Agricultural and Mechanical
        # Q8 = "What year was Texas A&M founded?"                                       # 1876
        # Q9 = "What number mascot is currently at Texas A&M?"                          # 10
        # Q10 = "Who is Texas A&M's football stadium named after?"                      # Edwin Jackson Kyle
        # Q11 = "Who was the original 12th man?"                                        # E. King Gill
        # Q12 = "What significant tree is on the Texas A&M campus?"                     # Century Tree
          
        var = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] # Creates a list of numbers 0-11 so the random module can choose a random question.
        correctQuestions = 0
        userAnswer = "placeholder variable"
          
        def verifyAnswers(userAnswer, actualAnswer):
            """Verifies if the user's inputted answer is correct."""
            correct = False
            if userAnswer == actualAnswer:
                print("\n☆☆☆ Correct! ☆☆☆\n")
                correct = True
            elif numOfGuesses != 3: 
                print("\nIncorrect! Try Again!")
                correct = False
            else: 
                print("\nIncorrect! Good try, but onto the next question!\n")
                correct = False
            return correct
          
        for i in range(len(questions)): # This loop cycles through each of the 12 questions once the inner loop is completed.
            
            if userAnswer == "QUIT":
                break
            numOfGuesses = 0
            randomVar = random.choice(var)
            correct = False
            print(questions[randomVar])
            actualAnswer = answerkey.get(questions[randomVar])
            
            print(answerbank[randomVar][0])
            print(answerbank[randomVar][1])
            print(answerbank[randomVar][2])
            print(answerbank[randomVar][3])
            
            while numOfGuesses < 3 and not correct: # This loop gives the user 3 attmempts per question and after each attempt it "checks" if the user is right.
                print()                 # If right, then done with this cycle. If not right, continue until 3 guesses are used. 
                userAnswer = input("Enter guess (A, B, C, D, or quit to exit): ").upper()
                
                if userAnswer == "QUIT":
                    print(f"\nHey {username}, try harder next time you stinkin' quitter. Your score was: {(correctQuestions / 12) * 100}%!")
                    break
                
                while len(userAnswer) != 1: # Checks the inputted guess length and gives according messages to the user.
                    if len(userAnswer) > 1: 
                        print("\n   Enter one capital letter (A, B, C, D).")
                    elif len(userAnswer) < 1:
                        print("\n   Enter one capital letter (A, B, C, D).")
                    userAnswer = input("\nEnter guess (A, B, C, D): ").upper()
                   
                while True: # Uses a try except statement to check if the inputted guess is composed of only letters.
                    try:    # This try except is designed to only work when the exception is met.
                        userAnswer = int(userAnswer) 
                        print("\n   Enter one capital letter (A, B, C, D).")
                        userAnswer = input("\nEnter guess (A, B, C, D): ").upper()
                    except:
                        break
                    
                while len(userAnswer) != 1: # Checks the inputted guess length and gives according messages to the user.
                    if len(userAnswer) > 1: # This is to ensure the user has a letter guess that is also the correct length.
                        print("\n   Enter one capital letter (A, B, C, D).")
                    elif len(userAnswer) < 1:
                        print("\n   Enter one capital letter (A, B, C, D).")
                    userAnswer = input("\nEnter guess (A, B, C, D): ").upper()
                    
                print("\nYou guessed:", userAnswer)
                numOfGuesses += 1
                correct = verifyAnswers(userAnswer, actualAnswer)
            if correct: 
                correctQuestions += 1
            var.remove(randomVar) # This updates the list (var) by removing the question that was just answered.
        
        # Outputs score with some cool formatting.
        print("\nThe score is calculating...")
        print()
        print("\n☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
        print(f"\n   You made a {(correctQuestions / 12) * 100:.2f}%! Great Job!\n")
        print("☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
        
        # Outputs a graph of a picture of Reveille X as the Special Prize for making a 100% on the Trivia Game!
        if (correctQuestions / 12) * 100 == 100:
            
            ax = plt.gca()
            plt.title("The Special Prize of Texas A&M")
            ax.axes.get_xaxis().set_visible(False)
            ax.axes.get_yaxis().set_visible(False)
             
            image = mpimg.imread("Reveille.jpg")
            plt.imshow(image)
            plt.show()

    elif option == 4: # Quits program (Done)
        signature = " 𝑷𝒓𝒐𝒋𝒆𝒄𝒕 𝒃𝒚 𝒥𝒶𝒸𝑜𝒷 𝒥𝑜𝓃𝑒𝓈 "
        centerSignature = signature.center(90, "☆")
        signoff = f"Thanks for playing {username}!"
        centerSignoff = signoff.center(90)
        print("\n\n\n\n\n☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
        print(f"\n\n\n{centerSignoff}")
        print(f"\n\n\n{centerSignature}")
        break