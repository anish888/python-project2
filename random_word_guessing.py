#import random module for generate random word..
import random
#use while loop until conditions..break.
while True:
    #list of words
   word=['uneven','employ','slimy','ground','view','wealth','level','embarrass','bumpy','quilt','test','vulgar','permit','point','rambunctious','pin','hospitable','dreary','remain','embarrassed','key','seed','fresh','man','smiling','harm','whip','dusty','sin','basin','harmony','tacit','look','superb','seashore','crook','company','river','smelly','stranger','purpose','temper','divide','empty','person','roasted','shelter','macabre','succinct']
   print(" choose word from below-->")
   #use f-string for printing the word
   print(f"{word}")
   # generating random word  by computer
   computer_guess=random.choice(word)
   #getting user input
   choose_word=input(" enter your word ->")
   #checking condition 
   if choose_word==computer_guess:
       print(f"your guess is {choose_word}...and you win....!!!computer loose")
   else:
       print(f" computer guess is -- {computer_guess},.. and computer win ...!!!you loose")
   play_again=input(" if you want to play again write --> yes/no-->")
   if play_again=='no':
     print("Thanks for the playing ....have a good day!!")
     break
  


     
    

