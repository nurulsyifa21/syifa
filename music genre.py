#!/usr/bin/env python
import random

def MusicGenre():
    """Start a music genre guessing game. """
print("Guess the music genre!")

music = [
    "pop",
    "hip - pop",
    "rock",
    "rap",
    "jazz"
     ] 

x = random.choice(music)
guess = None

while x != guess:

    guess = str(input("What is my favourite music genre?"))

    if x == guess:
        print("You guessed {}.You get it right!".format(guess))
    else:
        print("You guessed {}.Ops!Try again!".format(guess))

MusicGenre()
        
        
              
            
               
              
            



      
      
      

                   



                   