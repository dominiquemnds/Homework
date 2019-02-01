import random

count=0
guesses=[]

print("Welcome to my guessing game!")
name=input(str("What is your name?"))

print("Alright "+name+". Let's play!")
print("I'm thinking of a number 1-10...Can you guess what it is?")
print("You'll have ten tries to guess the number")

randomnum=random.randrange(10)
#print(type(randomnum))

while count<10 :
    guess=int(input("What's your guess?"))
    #print(type(guess))
    if guess==randomnum:
        print("WOW "+name+" you got it!")
        print("And it only took you "+str(count)+" guesses!")
        print("These were your previous guesses "+str(guesses))
        break
    
    if guess in guesses:
        print("You've already guessed that!")
        
    if guess!=randomnum and count< 9:
        print("Aww, try again..")
        guesses.append(guess)
        count=count+1
        print(count)
        
    if guess!=randomnum and count>=9:
        print("Sorry, you've lost this round :(")
        print("The correct answer was "+str(randomnum))
        print("Here were your previous guesses "+str(guesses))
        break;
    
    
print("Thanks for playing!")
