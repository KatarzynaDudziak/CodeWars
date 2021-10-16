def decode_string(string):
    
    number = 0
    word = []
    
    for char in string:
        if char.isdigit():
            number = int(char)
        word.append(char)
    
    return number, "".join(word)

def order(sentence):

    result = dict()

    for element in sentence.split():
        x = decode_string(element)
        result[x[0]] = x[1]
    
    return " ".join([result[key] for key in sorted(result.keys())])
