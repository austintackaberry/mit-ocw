# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    secretWordList = list(secretWord)
    combinedSet = set(lettersGuessed + secretWordList)
    return len(combinedSet) == len(set(lettersGuessed))


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    newStr = ""
    for char in secretWord:
        if char in lettersGuessed:
            newStr += char
        else:
            newStr += '_'

    return newStr


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    ans = ""
    allLetters = "abcdefghijklmnopqrstuvwxyz"
    for char in allLetters:
        if char not in lettersGuessed:
            ans += char
    return ans


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    lettersGuessed = []
    numGuesses = 0
    display = getGuessedWord(secretWord, lettersGuessed)
    while not isWordGuessed(secretWord, lettersGuessed) and numGuesses < 8:
        newDisplay = getGuessedWord(secretWord, lettersGuessed)
        if display == newDisplay:
            numGuesses += 1
        display = newDisplay
        availableLetters = getAvailableLetters(lettersGuessed)
        guess = input('Guess a letter: ' + display + '\n')
        while guess not in availableLetters:
            guess = input("Letter previously guessed or not a-z. Try again.\n")
        lettersGuessed.append(guess)
        wordGuessed = isWordGuessed(secretWord, lettersGuessed)
        if wordGuessed:
            print("Congratulations, you win! The word was " + secretWord)
            return
    print("You guessed wrong 8 times. Wow... The secret word was " + secretWord)
    return


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)
print(isWordGuessed('grapefruit', [
      'z', 'x', 'q', 'g', 'r', 'a', 'p', 'e', 'f', 'r', 'u', 'i', 't']))
# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
