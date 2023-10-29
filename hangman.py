about = """
Made by Akhila Kulkarni
"""

import random, time, requests, subprocess, os, math

def clear():
    _ = subprocess.call('clear' if os.name =='posix' else ['cmd', '/c', 'cls'])
def downloadWords(quantity):
    source = "https://random-word-api.herokuapp.com/word"
    parameters  ={'number': quantity}
    result = requests.get(url = source, params= parameters)
    data = result.json()
    try:
        with open('words.txt', 'a') as words_file:
            for word in data:
                words_file.write(word+'\n')
    except:
        print ("ERROR! COULDN'T SAVE WORDS. PLEASE CHECK YOUR SYSTEM'S READ / WRITE PERMISSIONS.")
        exit()

def getWords():
    words_list = []
    try: # if internet is available, download words
        downloadWords(10)
    except:  # if internet isn't available, use previously downloaded words
        print ("Couldn't connect to the internet. Using last stored word list.")
    try: 
        with open('words.txt', 'r') as words_file:
            if not words_file.read(1): # words file empty
                print ("ERROR! NO WORDS FOUND. PLEASE TRY CONNECTING TO THE INTERNET OR CHECK YOUR SYSTEM'S READ / WRITE PERMISSIONS.")
                exit()
            
            else: 
                words = words_file.readlines()
                for word in words:
                    words_list.append(word.strip()) # strip removes newline character '\n'

    except: # words file doesn't exist
        print ("ERROR! NO WORDS FILE FOUND. PLEASE CONNECT TO THE INTERNET TO DOWNLOAD SOME WORDS.")
        exit()
    
    return words_list

def askName():
    name = input ("What is your name? ▸ ")
    if name == None or (len(name) in range(0,2)):
        name = "Jenny"
    else:
        name = name.capitalize()
    return name

def printStory(name):
    print(name + " was incorrectly arrested for murder.")
    time.sleep(2)
    print("But....")
    time.sleep(1)
    print(name + " never commited the murder. " + name + " was falsely framed!")
    time.sleep(3)
    print("The mandated punishment for murder is execution by hanging.")
    time.sleep(3)
    print("The court may let " + name + " live, but on one condition...")
    time.sleep(3)
    print("That " + name + " guesses everything they ask correctly.")
    time.sleep(3)
    print(name +"'s intelligence can help prove them wrong.")
    time.sleep(3)
    clear()
    
def printHangman(state):
    if state == 0:
        print("   _________ \n"
          "  |/       |  \n"
          "  |        |  \n"
          "  |        x  \n"
          "  |       ( )    \n"
          "  |               \n"
          "  |                \n"
          "  |                \n"
          "  |                  \n"
          "  |      ____         \n"
          "__|__    /  \        \n\n")

    if state == 1:
        print("   _________ \n"
              "  |/       |  \n"
              "  |        |  \n"
              "  |      __⊥__  \n"
              "  |      (·⌢·)     UH OH \n"
              "  |               \n"
              "  |                \n"
              "  |                \n"
              "  |                  \n"
              "  |      ____         \n"
              "__|__    /  \        \n")
        print("Wrong guess. " + str(5 - state) + " guesses remaining")
    elif state == 2:
        print("   _________ \n"
              "  |/       |  \n"
              "  |        |  \n"
              "  |      __⊥__  \n"
              "  |      (·⌢·)          NOOOOOO \n"
              "  |        |  \n"
              "  |        |  \n"
              "  |                   \n"
              "  |                  \n"
              "  |      ____    \n"
              "__|__    /  \  \n")
        print("Wrong guess. " + str(5 - state) + " guesses remaining")
    elif state == 3:
        print("   _________ \n"
              "  |/       |  \n"
              "  |        |  \n"
              "  |      __⊥__  \n"
              "  |      (·⌢·)  HELP!   \n"
              "  |        |  \n"
              "  |      / | \ \n"
              "  |     /     \  \n"
              "  |                 \n"
              "  |      ____    \n"
              "__|__    /  \  \n")
        print("Wrong guess. " + str(5 - state) + " guesses remaining")
    elif state == 4:
        print("   _________ \n"
              "  |/       |  \n"
              "  |        |  \n"
              "  |      __⊥__  \n"
              "  |      (T⌢T)    my fate's decided i guess...  \n"
              "  |        |     \n"
              "  |      / | \   \n"
              "  |     /  |  \  \n"
              "  |       / \     \n"
              "  |     _/___\_    \n"
              "__|__    /  \  \n")
        print("Wrong guess. " + str(5 - state) + " guesses remaining")
    elif state == 5:
        print("   _________ \n"
              "  |/       |  \n"
              "  |        |  \n"
              "  |        ⊥  \n"
              "  |      (x_x)   goodbye cruel world  \n"
              "  |        |  \n"
              "  |      / | \    \n"
              "  |     /  |  \    \n"
              "  |       / \    \n"
              "  |       | |     __|  \n"
              "__|__             --|  \n")
        print("Wrong guess. " + str(5 - state) + " guesses remaining")
def mainMenu():
    clear()
    print("_____________________________________")
    print("||          H A N G M A N          ||")
    print("-------------------------------------")
def printLicense():
    print(about + '\n')
def victoryScreen(speed):
    clear()
    time.sleep(speed)
    clear()
    print("\n   _________ \n"
           "  |/         \n"
           "  |        \n"
           "  |      (^_^)  Hooray!  \n"
           "  |     \  |  /   \n"
           "  |      \ | /   \n"
           "  |        |     \n"
           "  |       / \     \n"
           "  |     _/___\_    \n"
           "__|__    /  \  \n")
    time.sleep(speed+1)
    clear()
    print("\n   _________ \n"
           "  |/         \n"
           "  |          \n"
           "  |        \n"
           "  |               (^_^) \n"
           "  |               / | \\\n"
           "  |              /  |  \\\n"
           "  |                 |\n"
           "  |     ______     / \ \n"
           "__|__    /  \    _/  _\ \n")
   
    time.sleep(speed)
    clear()
    print("\n   _________ \n"
           "  |/         \n"
           "  |          \n"
           "  |        \n"
           "  |               (^_^) \n"
           "  |               / | \ \n"
           "  |              /  |  \ \n"
           "  |                 |\n"
           "  |     ______     / \ \n"
           "__|__    /  \    _/  _\ \n")
   
    time.sleep(speed)
    clear()
    print("\n   _________ \n"
           "  |/         \n"
           "  |          \n"
           "  |        \n"
           "  |             (^_^) \n"
           "  |             / | \ \n"
           "  |            /  |  \ \n"
           "  |               | \n"
           "  |     ______   | \ \n"
           "__|__    /  \   _| _\ \n")
   
    time.sleep(speed)
    clear()
    print("\n   _________ \n"
           "  |/         \n"
           "  |          \n"
           "  |        \n"
           "  |           (^_^) \n"
           "  |             |  \ \n"
           "  |          \  |   \ \n"
           "  |           \ |    \n"
           "  |            \ \ \n"
           "__|__            _\ \n")
    time.sleep(speed)
    clear()
    print("\n   _________ \n"
           "  |/         \n"
           "  |          \n"
           "  |        \n"
           "  |    (^_^) \n"
           "  |    / | \ \n"
           "  |   /  |  \ \n"
           "  |      | \n"
           "  |     / \ \n"
           "__|__ _| _| \n")
    time.sleep(speed)
    clear()
    print("\n    \n"
           "|           \n"
           "|------------------            \n"
           "|  \         /   \|\n"
           "    \ (^_^) /     |\n"
           "     \_ | _/      |\n"
           "        |    \n"
           "        | \n"
           "       / \ \n"
           "     _/  _\ \n")
    time.sleep(speed)
    clear()
    print("\n    \n"
           "     \n"
           "------------            \n"
           "      /   \|\n"
           "^_^) /     |\n"
           " | _/      |\n"
           " |    \n"
           " | \n"
           "/| \n"
           "_| \n")
    time.sleep(speed)
    clear()
    print("\n    \n"
           "     \n"
           "--------            \n"
           "  /   \|\n"
           " /     |\n"
           "/      |\n"
           "  \n"
           ""
           "\n"
           "\n")

    time.sleep(speed)
    clear()
    print("\n   \n"
          "           *  \n"
          "             \n"
          "          *     *   \n"
          "            YOU WON! \n"
          "              *        *\n"
          "         *         \n"
          "                *  \n"
          "           *                    \n"
          "                               \n"
          "\n"
          "                                \n")

def lossScreen(speed,w):
        clear()
        time.sleep(speed)
        clear()
        print("\n   _________ \n"
              "  |/       |  \n"
              "  |        |  \n"
              "  |        ⊥  \n"
              "  |      (x_x)    \n"
              "  |        |  \n"
              "  |      / | \    \n"
              "  |     /  |  \    \n"
              "  |       / \    \n"
              "  |       | |     __|  \n"
              "__|__             --|  \n")
        
        time.sleep(speed)
        clear()
        print("\n   _________ \n"
              "  |/       x  \n"
              "  |          \n"
              "  |        ⊥  \n"
              "  |      (x_x)    \n"
              "  |        |  \n"
              "  |      / | \    \n"
              "  |     /  |  \    \n"
              "  |       / \    \n"
              "  |       | |     __|  \n"
              "__|__             --|  \n")

        time.sleep(speed)
        clear()
        print("\n   _________ \n"
              "  |/       *  \n"
              "  |          \n"
              "  |          \n"
              "  |        ⊥  \n"
              "  |      (x_x)    \n"
              "  |        |  \n"
              "  |      / | \    \n"
              "  |     /  |  \    \n"
              "  |       / \     __|\n"
              "__|__     | |     --|  \n")

        time.sleep(speed)
        clear()
        print("\n   _________ \n"
              "  |/       *  \n"
              "  |          \n"
              "  |          \n"
              "  |          \n"
              "  |          \n"
              "  |         (x_x)  \n"
              "  |          /  \n"
              "  |        // \    \n"
              "  |      / /   \   __| \n"
              "__|__    / |       --|\n")

        time.sleep(speed)
        clear()
        print("\n   _________ \n"
              "  |/       *  \n"
              "  |          \n"
              "  |          \n"
              "  |          \n"
              "  |          \n"
              "  |           \n"
              "  |             \n"
              "  |               \n"
              "  |     __  __  (x⌢x)| \n"
              "__|__   __/---\---/ --|\n")

        time.sleep(speed)
        clear()
        print("\n   \n"
              "             \n"
              "             \n"
              "         /-----\n"
              "        /     \n"
              "       /      \n"
              "      /        \n"
              "     /          \n"
              "    /               \n"
              "   /    __  __  (x⌢x)| \n"
              "__/__   __/---\---/ --|\n")

        time.sleep(speed)
        clear()
        print("\n   \n"
              "             \n"
              "             \n"
              "         \n"
              "             \n"
              "             \n"
              "              \n"
              " |             \n"
              " |_____________________________\n"
              " |      __  __  (x⌢x)|      \| \n"
              " |      __/---\---/ --|       |\n")

        time.sleep(speed)
        clear()
        print("\n   \n"
              "           *  \n"
              "             \n"
              "          *     *   \n"
              "            YOU DIED \n"
              "              *        *\n"
              "         *         \n"
              "                *  \n"
              "           *                    |\n"
              "\  /                            |\n"
              " \/____________________________/|\n"
              " /\                              \n")

        time.sleep(speed)
        clear()
        print("\n   \n"
              "           *  \n"
              "             \n"
              "          *     *   \n"
              "            YOU DIED \n"
              "              *        *\n"
              "         *         \n"
              "                *  \n"
              "           *                    \n"
              "                               \n"
              "\n"
              "                                \n")
        time.sleep(speed)
        clear()
        print("\nThe word is :",w)
def blankOutLetters(word, number):
    split_word = [letter for letter in word]
    count = 0
    blanks = 0
    for letter in split_word:
        if blanks < number:
            blank = random.choice([True, False])
            if blank == True:
                split_word[count] = '_'
                blanks+=1
            count+=1
        
        else:
            break

    return split_word
    
def fillWord(complete_word, blanked_word, guess):
    index_to_replace = complete_word.index(guess)
    blanked_word [index_to_replace] = guess
    return blanked_word

def requiredLetters(complete_word, blanked_word):
    required = []
    count = 0
    for letter in complete_word:
        if complete_word[count] != blanked_word[count]:
            required.append(letter)
        count+=1

    return required

def startGame(word, level):
    length = len(word)
    complete_word = [letter for letter in word]
    letters_to_blank = 0

    current_word = []
    try_no = 0
    
    if level == 1: 
        letters_to_blank = math.ceil(length * (20 / 100)) # blank out 20% of the word

    elif level == 2:
        letters_to_blank = math.ceil(length * (50 / 100)) # blank out 50% of the word

    elif level == 3:  # blank out 60% of the word
        letters_to_blank = math.ceil(length * (60 / 100)) # blank out 60% of the word
        
    elif level == 4:  # blank out 70% of the word
        letters_to_blank = math.ceil(length * (70 / 100)) # blank out 70% of the word

    current_word = blankOutLetters(word, letters_to_blank)
    required_letters = requiredLetters(complete_word, current_word)

    
    clear()
    printHangman(0)
    print("**************************************")
    for letter in current_word: print(letter.upper(), end=' ') # print word clearly in uppercase with spacing

    required_letters = requiredLetters(complete_word, current_word)
    
    while True:
        if '_' in current_word:
            guess = input("\n-----------------------------\n+ Enter your guess ▸ ").lower()
            if guess in required_letters:
                current_word = fillWord(complete_word, current_word, guess)
                required_letters.remove(guess)
                clear()
                printHangman(try_no)
                print("**************************************")
                for letter in current_word: print(letter.upper(), end=' ')
    
            else:
                try_no+=1
                clear()
                printHangman(try_no)
                print("**************************************")
                for letter in current_word: print(letter.upper(), end=' ')
                if try_no == 5:
                    return False
        
        else:
            return True

if __name__ == "__main__":
    # show main menu sequence
    clear()
    mainMenu()
    printLicense()
    time.sleep(2)
    clear()
    mainMenu()
    input('\33[5m' + "Press ENTER to start" + '\033[0m ')
    clear()
    mainMenu()

    # show story
    printStory(askName())

    # start game
    printHangman(0)
    level = 4
    words = getWords()
    w=words[random.randint(0, len(words))] #w contains randomly selected word
    while True:
        if startGame(w, level) == True:
            victoryScreen(0.8)
            exit()
        
        else:
            lossScreen(0.8,w)
            exit()

    pass
