def evenWord(word):
    wordList = word.split()
    for letters in wordList:
        if len(letters) % 2 == 0:
            print("even")
        else:
            print(letters)


evenWord("Hola como se la esta pasando")
