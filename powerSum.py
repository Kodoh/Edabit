TPH = False
tris = []
penTri = []
result = []
def Tri(n):
    return n*(n+1)/2


#1533776805*2 = n*(n+1)
count = 0
while TPH == False:
    attempt = Tri(count)
    if attempt == 40755:
        print(count)
        TPH = True


    