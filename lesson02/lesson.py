def getUserInput():
    userInput = input('Enter word to be translated: ')
    return userInput

def showUserInput(userInput):
    string = "The word you are looking for is: %s " % (userInput)
    print(string)

def start():
    userInput = getUserInput()
    showUserInput(userInput)

start()
