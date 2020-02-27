word = raw_input("Type a word   ")
wordList = list(word.lower())
updatedSpaces = []
wordLen = len(word)
lives = 5
letter = " "
x = 0
letterIndex = 0
inWord = False

for i in range (0, int(wordLen)):
    updatedSpaces.append("_")
    
def getLetter():
    global letter
    letter = raw_input ("Enter a letter guess    ")

def check():
    global updatedSpaces
    global lives
    global letter
    global x
    global inWord
    global letterIndex
    while updatedSpaces != wordList:
        for i in range(0, int(wordLen)):
            if letter == wordList[i]:
                letterIndex = i
                inWord = True
                break
            else:
                inWord = False
        if inWord:
            updatedSpaces[letterIndex] = wordList[letterIndex]
            print(updatedSpaces)
            print("You have: " + str(lives) + " lives left!")
            checklist = "".join(updatedSpaces)
            master = "".join(wordList)
            if checklist == master:
                print("Congrats you solved the word!    ")
                break
        else:
            lives -= 1
            if lives == 0:
                print("Game Over   ")
                break
            else:
                print("You have:  " + str(lives) + "  lives left!")
                print(updatedSpaces)
        getLetter()
        x += 1
    
      
                
def game():
    getLetter()
    check()
    
game()                      