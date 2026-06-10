# Function for converting an integer into an array of digits
def getDigits(integer):
    return [int(i) for i in str(integer)]

# Function for checking whether an integer is increasing/decreasing
def checkIncreaseDecrease(integer, IorD):
    digits = getDigits(integer)
    for i in range(len(digits) - 1):
        if IorD == "increase" and digits[i+1] < digits[i]: return False
        if IorD == "decrease" and digits[i+1] > digits[i]: return False
    return True

# Function for classifying a number
# DEPENDENCIES: checkIncreaseDecrease (hence: getDigits)
def classify(integer):
    digits = getDigits(integer)
    inc = checkIncreaseDecrease(integer, "increase")
    dec = checkIncreaseDecrease(integer, "decrease")
    if inc or dec: return "not bouncy"

    ups = 0
    downs = 0
    for i in range(len(digits) - 1):
        if digits[i+1] > digits[i]: ups += 1
        elif digits[i+1] < digits[i]: downs += 1
    if ups == downs: return "perfectly bouncy"

    return "bouncy"



# Main Program
userInput = 0
while userInput <= 0:
    try: userInput = int(input("Enter an integer greater than 0: "))
    except: userInput = 0

print(classify(userInput))
