word = raw_input("Type a word   ")
wordList = list(word.lower())
updatedSpaces = []
wordLen = len(word)
lives = 5
letter = " "
x = 0
print("\x1b[2J")
#print("\x1b[5;3H")

for i in range (0,100):
    print

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
    while updatedSpaces != wordList:
        for x in range(0, int(wordLen)):
            if letter == wordList[x]:
                updatedSpaces[x] = wordList[x]
                print(updatedSpaces)
                print("You have:   ", lives, "   lives left!")
                checklist = "".join(updatedSpaces)
                master = "".join(wordList)
                if checklist == master:
                    print("Congrats you solved the word!    ")
                    #break
                else:
                    getLetter()
            else:
                if lives == 0:
                    print("Game Over   ")
                    # break
                else:
                    print("You have:  " + str(lives) + "  lives left!")
                    print(updatedSpaces)
                    getLetter()
                lives -= 1
        if lives == -1:
            break
        x += 1
    
      
                
def game():
    getLetter()
    check()
    
game()                      