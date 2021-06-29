#importing textblob
from textblob import TextBlob
#taking user input
words = [input("enter word for correction")]
#create a blank list to append correct word in this
corrected_words = []
for i in words:
    corrected_words.append(TextBlob(i))
print("Wrong words :", words)
print("Corrected Words are :")
for i in corrected_words:
    print(i.correct(), sep="++")
    