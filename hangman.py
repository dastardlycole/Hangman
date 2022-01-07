from word import words
import random
import time
from turtle_actions import *
import winsound


class Hangman():
    word_list = []
    lives = 8
    def __init__(self):
        self.play()
        

    def remove_stuff(self):
        for word in words:
            if  '-' not in word and ' ' not in word:
                self.word_list.append(word)

    def play(self):
        self.remove_stuff()
        letters_guessed = []
        correct_letters = []
        chosen_word = list(random.choice(self.word_list))
        print("Welcome to Hangman")
        winsound.PlaySound("Hangman\\intro.wav",winsound.SND_FILENAME)
        print("Generating word...")
        time.sleep(2)
        for i in range(len(chosen_word)):
            correct_letters.append('-')
        print(f"Guess the {len(chosen_word)}-letter word")   
        print(' '.join(correct_letters))

        while correct_letters != chosen_word:
            user_guess = input('Enter a letter: ').lower()

            while True:
                if not user_guess.isalpha() or not len(user_guess) == 1:
                    print("Enter one letter")
                elif user_guess in letters_guessed:
                    print("Oops you already guessed that. Try again")
                else:
                    break
                user_guess = input('Enter a letter: ').lower()

            letters_guessed.append(user_guess)
            letters_guessed.sort()
            if user_guess in chosen_word:
                indices = []
                for i in range(len(chosen_word)):
                    if chosen_word[i] == user_guess:
                        indices.append(i)   
                for i in indices:
                    correct_letters[i] = user_guess
            else:
                self.lives -= 1
                if self.lives == 7:
                    winsound.PlaySound("Hangman\\heartbeat1.wav",winsound.SND_ASYNC)
                    first_life()   
                    time.sleep(1)
                    turtle.bye()
                elif self.lives == 6:
                    winsound.PlaySound("Hangman\\heartbeat1.wav",winsound.SND_ASYNC)
                    second_life()             
                    time.sleep(1)
                    turtle.bye()
                elif self.lives == 5:
                    winsound.PlaySound("Hangman\\heartbeat1.wav",winsound.SND_ASYNC)
                    third_life()   
                    time.sleep(1)
                    turtle.bye()    
                elif self.lives == 4: 
                    winsound.PlaySound("Hangman\\heartbeat1.wav",winsound.SND_ASYNC)
                    fourth_life()   
                    time.sleep(1)
                    turtle.bye()    
                elif self.lives == 3:
                    winsound.PlaySound("Hangman\\heartbeat1.wav",winsound.SND_ASYNC)
                    fifth_life()   
                    time.sleep(1)
                    turtle.bye()    
                elif self.lives == 2:
                    winsound.PlaySound("Hangman\\heartbeat1.wav",winsound.SND_ASYNC)
                    sixth_life()   
                    time.sleep(1)
                    turtle.bye()    
                elif self.lives == 1:
                    winsound.PlaySound("Hangman\\heartbeat1.wav",winsound.SND_ASYNC)
                    seventh_life()   
                    time.sleep(1)
                    turtle.bye()    
                elif self.lives == 0:
                    winsound.PlaySound("Hangman\\heartbeat1.wav",winsound.SND_ASYNC)
                    eighth_life()   
                    winsound.PlaySound("Hangman\\scream_x.wav",winsound.SND_ASYNC)
                    time.sleep(2)
                    turtle.bye()
                    print(f"Your hangman has been hanged. YOU LOSE. {''.join(chosen_word).title()} was the right answer")    
                    winsound.PlaySound("Hangman\\whah_whah.wav",winsound.SND_FILENAME)
                    return
            if correct_letters != chosen_word:    
                print(f"You have guessed: {', '.join(letters_guessed)}")
                print(' '.join(correct_letters))    
        print(f"YOU WIN! {''.join(chosen_word).title()} was the right answer")        
        winsound.PlaySound("Hangman\\yay_z.wav",winsound.SND_FILENAME)
                    
                
a = Hangman()





    