#taking user input in string
name = str(input("Enter Your Name: "))
print(f"{name} you are stuck at work")
#story for user
print(" You are still working and suddenly you you saw a ghost, Now you have two options")
print("1.Run. 2.Jump from the window")
#taking user input from 1 or 2
user = int(input("Choose 1 or 2: "))
if user == 1:
    print("You did it")
elif user == 2:
    print("You are not that smart")
else:
    print("Please Check your input")