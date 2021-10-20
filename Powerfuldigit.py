total = 0
current = 0 
for i in range(100):
    for x in range(100):
        sumnum = 0
        number = i**x
        for y in str(number):
            sumnum += int(y)
        if sumnum > total:
            total = sumnum


print(total)