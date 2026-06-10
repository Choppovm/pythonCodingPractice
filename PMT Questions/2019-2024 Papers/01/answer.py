# Function to convert a string into array of its characters
def extractLetters(word):
    letterArray = []
    for i in range(0, len(word)):
        letterArray.append(word[i])
    return letterArray

# Function to determine whether a word can be created from another word's characters.
def compareLetterArrays(letterArray1, letterArray2):
    for i in range(0, len(letterArray2)):
        if letterArray2[i] in letterArray1:
            letterArray1.remove(letterArray2[i])
        else:
            pass
    
    if len(letterArray1) == 0:
        return True
    else:
        return False

# Main Program
firstWord, secondWord = input("Enter the first word: "), input("Enter the second word: ")
firstLetters, secondLetters = extractLetters(firstWord), extractLetters(secondWord)

if compareLetterArrays(firstLetters, secondLetters):
    print(f"{firstWord} can be created from the letters from {secondWord}.")
else:
    print(f"{firstWord} cannot be created from the letters from {secondWord}.")
