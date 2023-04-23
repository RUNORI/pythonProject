class Student:

    def __init__(self):
        self.phy = int(input("enter the marks of phy:"))

        self.chem = int(input("enter the marks of chem: "))

        self.math = int(input("enter the marks of math:"))

    def average(self):
        return (self.phy + self.chem + self.math) / 3


st = Student()

avg = st.average()
print(avg)
if (avg > 90):

    print("You got rank A")

elif (avg > 70 and avg < 90):

    print("you got rank B")

else:

    print("you got C grade")