#Random Password Generator
#Use ASCII code

import random	

#function to shuffle all the characters of a string
def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return ''.join(tempList)

#main program starts here
uppercaseLetter1=chr(random.randint(65,90))
lowercaseLetter1=chr(random.randint(97,122))
uppercaseLetter2=chr(random.randint(65,90))
lowercaseLetter2=chr(random.randint(97,122))
digit1=chr(random.randint(48,57))
digit2=chr(random.randint(48,57))
symbol1=chr(random.randint(32,152))

#Generate password using all xters
password = uppercaseLetter1 + lowercaseLetter1 + uppercaseLetter2 + lowercaseLetter2 + digit1 + digit2 + symbol1
password = shuffle(password)

#Output
print(password)