wordlist = []

while "over" not in wordlist:
    word = input("Enter any words: ")
    wordlist.append(word)
wordlist.remove('over')
print(wordlist)