def getInputWord():
    userInput = input('Enter word ')
    return userInput

def getInputLanguage():
    userInput = input('Enter language ')
    return userInput

def showUserInput(inputWord,inputLanguage):
    string = "Word: %s; Language:%s " % (inputWord,inputLanguage)
    print(string)

def start():
    inputWord = getInputWord()
    inputLanguage = getInputLanguage()
    showUserInput(inputWord,inputLanguage)
    start()

start()
