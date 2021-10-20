class Employee:
    def __init__(self, name,**kwargs):
        FLname = name.split(" ")
        self.name = FLname[0]
        self.lastname = FLname[1]
        print(__dict__)

"""
giancarlo = Employee('Giancarlo Rossi', salary=115000, height=182, nationality='Italian')
print(giancarlo.nationality)
print(giancarlo.salary)
#print(giancarlo.__dict__)
"""