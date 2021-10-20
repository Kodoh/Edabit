def num_split(num):
    placeholder = []
    if num * 1 > 0:
        length = len(str(num))
        count = 0 
        stringnum = str(num)
        revstr = ""
        for i in stringnum:
            revstr = i + revstr
        for x in range(length):
            times = 10**count
            bigtime = int(revstr[count]) * times
            placeholder.append(bigtime)
            count += 1
        placeholder.reverse()

    else:
        count = 0 
        stringnum = str(num)
        stringnum = stringnum[1::]
        length = len(stringnum)
        revstr = ""
        for i in stringnum:
            revstr = i + revstr
        for x in range(length):
            times = 10**count
            bigtime = int(revstr[count]) * times
            placeholder.append(bigtime*-1)
            count += 1
        placeholder.reverse()
    return placeholder




print(num_split(-434))

