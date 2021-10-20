def parse_code(txt):
    split = txt.split("0")
    Fname = split[0]
    split.remove(Fname)
    LnameID = []
    for i in split:
        if i != "":
            LnameID.append(i)
    Lname = LnameID[0]
    Id = LnameID[1]
    my_dict = {
        "first_name" : Fname,
        "last_name" : Lname,
        "id" : Id
    }
    return my_dict

print(parse_code("John000Doe000123"))