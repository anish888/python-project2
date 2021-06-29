#defining function
def check_guess(guess,answer):
    #used global variable
    global score
    still_guessing=True
    attempt=0
    #use while loop until condition
    while still_guessing and attempt < 3:
#condition for checking answer is wright or wrong
        if guess.lower()==answer.lower():
            print("correct answer")
            score=score+1
            still_guessing=False
        else:
            if attempt<2:
                guess=input("sorry..wrong answer,try again")    

            attempt=attempt+1
    if attempt==3:
        print("correct answe is -->",answer)
score=0
print("guess the animal")
guess1=input("which bear live at the north pole?.")
check_guess(guess1,'Polar bear') 
guess2=input("which is the fastest land animal ?")
check_guess=(guess2,'chhetah')
guess3=input("which is largest animal ?")
check_guess=(guess3,"Blue whale") 
print('your score is',str(score))                   