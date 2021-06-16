# class variables and instance variables
class Students:
    # classvariables
    increment = 1.5
    noOfStudents = 0

    def __init__(self, fname, lname, rollnum, fee):
        # instance variables
        self.fname = fname
        self.lname = lname
        self.rollnum = rollnum
        self.fee = fee
        self.increment = 2.0
        Students.noOfStudents += 1

    # class method
    @classmethod
    def changeIncrement(Cls, Amt):
        Cls.increment = Amt

    def appendFee(self):
        self.fee = int(
            self.fee * Students.increment
        )  # Class variables, instance variables

    @staticmethod
    def isopen(day):
        if day == "Sunday":
            print("School Closed")
        else:
            print("School Open")


Students.isopen("Sunday")

print(Students.noOfStudents)
aaditya = Students("Aaditya", "Dulal", 19030672, 10000)
print(Students.noOfStudents)
aadesh = Students("Aadesh", "Shrestha", 19030673, 15000)
print(Students.noOfStudents)


print(aaditya.fee)
Students.changeIncrement(3)
aaditya.appendFee()
print(aaditya.fee)

# inheritence
class Toppers(Students):
    def __init__(self, fname, lname, rollnum, fee, marks):
        super().__init__(fname, lname, rollnum, fee)
        self.marks = marks

    def appendFee(self):
        self.fee = int(self.fee - 5000)


Sakrita = Toppers("Sakrita", "Bariya", 123, 10000, "100/100")
print("Marks:", Sakrita.marks)
print("Fee:", Sakrita.fee)
Sakrita.appendFee()
print("Appended Fee: ", Sakrita.fee)
