#function for valaditing angrams
def anagram(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()
    #sorting word1 and word2
    #if user word is validate angram it return true otherwise false..
    return sorted(word1) == sorted(word2)
#taking user input for valadating angrams
word1=input("enter word1")
word2=input('enter word2')
#calling function
anagram=anagram(word1,word2)
print(anagram)
