def to_boolean_list(word):
    word = word.lower()
    valuelist = []
    bina = []
    YesNo = []
    for i in word:
        valuelist.append(ord(i)-96)
    for x in valuelist:
        if x % 2 != 0:
            bina.append(1)
        else:
            bina.append(0)
    for e in bina:
        if e == 0:
            YesNo.append(False)
        else:
            YesNo.append(True)
    return YesNo

print(to_boolean_list("rat"))