def increment_string(string):
    
    number = []
    word = []
    i = 0
    revString = list(reversed(string))
    
    for char in revString:
        if char.isdigit():
            number += char
            i = i + 1
        else:
            break
    
    number = revString[:i]
    word = revString[i:]
    
    number = list(reversed(number))
    word = reversed(word)
    
    if len(number) == 0:
        number = "0"
            
    number = "".join(number)
    incrementedNumber = str(int(number) + 1)
    
    if len(number) > len(incrementedNumber):
        diff = len(number) - len(incrementedNumber)
        for _ in range(diff):
            incrementedNumber = "0" + incrementedNumber
    
    return  "".join(word) + incrementedNumber
