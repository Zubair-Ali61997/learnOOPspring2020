class parent:
    fathername = ""
    mothername = ""

    def father_motorcycle(self):
        print("Father name is " + self.fathername)
        print("Mother name is " + self.mothername)
        print("this is father's motorcycle")

class child:
    childName = ""
    childAge = ""

parent1 = parent()
parent1.motorcycle()

child1 = child()
child1.childName = "Zubair"
child1.childAge = 22


