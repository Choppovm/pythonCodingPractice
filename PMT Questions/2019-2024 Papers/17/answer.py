"""
THIS CODE IS HIGHLY UNOPTIMIZED.
There is definitely a faster way of doing this question. I'm a bit slow in the head, however, so this will have to do.
"""

# Function for converting an integer into a numerical array
def getDigits(value):
    return [int(i) for i in str(value)]

# Function for getting sum of all digits in numerical array
def getSum(digits):
    sum = 0
    for i in range(0, len(digits)):
        sum += digits[i]
    return sum

# Function for determining if an integer is divisible by the sum of its values
# DEPENDENCIES: getDigits, getSum
def determineDivisble(value):
    if value % getSum(getDigits(value)) != 0:
        return False
    else:
        return True

# Function for getting the nth harshad value
# DEPENDENCIES: determineDivisible (hence: getDigits, getSum)
def getNthHarshad(value):
    harshad = []
    i = 0
    while True:
        i += 1
        if determineDivisble(i): harshad.append(i)
        if len(harshad) == value: return harshad[-1]



# Main program
userInput = int(input("Enter your desired nth harshad number: "))
print(f"Your harshad number (#{userInput}) is {getNthHarshad(userInput)}.")
