# Function to convert string into array of characters
def getCharacterArray(userString):
    return list(userString)

# Function to get index positions of vowels in array
def getVowelPos(charArray):
    positions = []
    for i in range(0, len(charArray)):
        if charArray[i] in "aeiou":
            positions.append(i)
    return positions

# Function to swap two elements in an array
def swapElementPos(array, pos1, pos2):
    array[pos1], array[pos2] = array[pos2], array[pos1]
    return array

# Function to swap all vowels
# DEPENDENCIES: getCharacterArray, getVowelPos, swapElementPos
def swapAllVowels(userString):
    chars = getCharacterArray(userString)
    vowelPos = getVowelPos(chars)

    for i in range(0, len(vowelPos) // 2):
        pos1 = vowelPos[i]
        pos2 = vowelPos[len(vowelPos) - 1 - i]
        swapElementPos(chars, pos1, pos2)

    return "".join(chars)



# Main Program
userString = input("Enter a string: ")
reversedString = swapAllVowels(userString)
print(reversedString)