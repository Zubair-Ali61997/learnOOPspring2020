class parent:
    fatherName = ""
    motherName = ""

    def motorcycle(self):
        print("this is Father's motorcycle")

class child(parent):
    childName = ""
    childAge = ""

c1 = child()
c1.fatherName = "Ali"
c1.motherName = "Hania"
c1.childName = "Zubair"
c1.childAge = 22

print("Name of child: " + str(c1.childName))
print("Name of child's Father: " + str(c1.fatherName))
print("Name of child's Mother: " + str(c1.motherName))
print("child's Age : " + str(c1.childAge))
print("---------------------------------------------")

c1.motorcycle()
print("----------------------------------------------")