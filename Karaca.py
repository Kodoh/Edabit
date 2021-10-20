def encrypt(word):
    rev = word[::-1].lower()
    newWord = ""
    for i in rev:
        if i == "a":
            newWord += "0"
        elif i == "e":
            newWord += "1"
        elif i == "i":
            newWord += "2"
        elif i == "o":
            newWord += "2"
        elif i == "u":
            newWord += "3"
        else:
            newWord += i
    newWord += "aca"
    return newWord

print(encrypt("karaca"))