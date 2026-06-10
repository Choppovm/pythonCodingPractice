# Function for checking if string length is valid (5 <= length <= 7)
def checkLength(string):
    if len(string) >= 5 and len(string) <= 7: return True
    else: return False

# Function for checking if string case is valid (uppercase)
def checkCase(string):
    if string == string.upper(): return True
    else: return False

# Function for checking if string is unique (no repeating characters)
def checkUnique(string):
    chars = list(string)
    checked = []
    for i in range(0, len(chars)):
        if chars[i] in checked: return False
        else: checked.append(chars[i])
    return True

# Function for checking if string ascii sum is valid (420 <= ascii sum <= 600)
def checkAscii(string):
    chars = list(string)
    for i in range(0, len(chars)):
        chars[i] = ord(chars[i])
    
    sum = 0
    for i in range(0, len(chars)):
        sum += int(chars[i])
    
    if sum >= 420 and sum <= 600: return True
    else: return False

# Function for generating resultant message
def generateResult(string):
    result = ""
    status = None
    validLength, validCase, validUnique, validAscii = checkLength(string), checkCase(string), checkUnique(string), checkAscii(string)
    stringIsValid = validLength and validCase and validUnique and validAscii
    if stringIsValid:
        status = True
        result += f"The string you have entered ({string}) is valid!"
    else:
        status = False
        result += f"The string you have entered ({string}) is invalid. This is because:"
        if not validLength: result += "\n- The string must be between 5 and 7 characters (inclusive)"
        if not validCase: result += "\n- The string must be entirely uppercase"
        if not validUnique: result += "\n- The string must consist of unique characters only (ie no character in the string appears more than once)"
        if not validAscii: result += "\n- The string's characters must have a total ASCII sum between 420 and 600 (inclusive)"
    return result, status



# Main Program
enteredValid = False
while not enteredValid:
    userInput = input("Enter a string: ")
    result, valid = generateResult(userInput)
    print(result + "\n")
    if valid: enteredValid = True
    else: pass
