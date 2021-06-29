#import random for random pasword geeration
import random
#length of the pasword that user want
passwordlength=int(input("enter the length of the pasword"))
s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
#creating random pasword 
p="".join(random.sample(s,passwordlength))
#printing the pasword
print(p)