def wrong_number(arr1):
    totalsacross1 = [0,0,0,0]
    totalsdown1 = [0,0,0,0]
    for i in range(3):
        totalsacross1[0] += arr1[0][i]
    for i in range(3):
        totalsacross1[1] += arr1[1][i]
    for i in range(3):
        totalsacross1[2] += arr1[2][i]
    for i in range(3):
        totalsacross1[3] += arr1[3][i]
    for i in range(3):
        totalsdown1[0] += arr1[i][0]
    for i in range(3):
        totalsdown1[1] += arr1[i][1]
    for i in range(3):
        totalsdown1[2] += arr1[i][2]
    for i in range(3):
        totalsdown1[3] += arr1[i][3]
    count = 0 
    count2 = 0
    for i in totalsacross1:
        if i != arr1[count][3]:
            break
        count += 1
    for i in totalsdown1:
        if i != arr1[3][count2]:
            break
        count2 += 1
    ans = arr1[count][count2]
    #count = down / count2 = across 
    if count == 3:
        ans = totalsdown1[count2]
    elif count2 == 3:
        ans = totalsacross1[count]
    else:
        temp = arr1[count][3] - totalsacross1[count] 
        ans += temp
    return ans



lst1 = [
[2, 2, 3, 6 ],
[4, 5, 6, 15],
[7, 8, 9, 24],
[12,15,18,45]
]

print(wrong_number(lst1))