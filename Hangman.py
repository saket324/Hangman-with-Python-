import random
# library in order to choose random words

name = input("What is your name? ") #Asking user for thier name
 
print("Good Luck ! ", name)
 
words = ['apple', 'python', 'basketball', 'swimming', 
         'java', 'programming', 'player', 'dictionary', 
         'banana', 'canada', 'goose', 'geeks']              

word = random.choice(words) #Function will choose a random word from this list to use for the game.
 
print("Guess the characters")
 
guesses = ''
 
turns = 10              #Can be changed to liking
 
while turns > 0:
     
    
    failed = 0          #Counting the number of times the user fails
     

    for char in word: 
         
        if char in guesses:       #Comparing the character chosen to the word  
            print(char)
             
        else: 
            print("_")
             
            failed += 1          #failures are counted here
             
 
    if failed == 0:              #User wins the game if there are no failures 
    
        print("You Win") 
         
        print("The word is: ", word)   #Prints the word
        break
     
    guess = input("guess a character:")
     
     
    guesses += guess                    #Characters guessed are stored here 
     
    if guess not in word:               #If the user guesses a character not in the word, they lose a turn
         
        turns -= 1
         
        print("Wrong")
         
        print("You have", + turns, 'more guesses')
         
        if turns == 0:
            print("You Loose")         #Once the user reaches 0 turns, then they lose