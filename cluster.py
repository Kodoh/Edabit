
def block_player(a,b):
    lines = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for i in lines:
        if i.count(a) and i.count(b) > 0:
            for x in i:
                if x != a:
                    if x != b:
                        return x
print(block_player(0,1))