#import the os module to interact with the underlying operating system
import os
#importing paltform for system information
import platform
#function for shut down
def shutdown():
    #checking system is os or linux
    if platform.system() == "Windows":
        os.system('shutdown -s')
    elif platform.system() == "Linux" :
        os.system("shutdown -h now")
    else:
        print("Os not supported!")
#function for  restarting
def restart():
    #checking system is os  or linux
    if platform.system() == "Windows":
        os.system("shutdown ")
    elif platform.system() == "Linux" :
        os.system('reboot now')
    else:
        print("Os not supported!")

#taking input from the user for reatart os shutdown
command = input("Use \'r\' for restart and \'s\' for shutdown: ")
#condition if user want want to restart or shutdown
if command == "r":
    restart()
elif command == "s":
    shutdown()
else:
    print("Wrong letter")