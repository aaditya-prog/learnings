class Students:
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

    @classmethod
    def changeIncrement(Cls, Amt):
        Cls.increment = Amt

    def appendFee(self):
        self.fee = int(
            self.fee * Students.increment
        )  # Class variables, instance variables


aaditya = Students("Aaditya", "Dulal", 19030672, 10000)
aadesh = Students("Aadesh", "Shrestha", 19030673, 15000)
print(aadesh.increment)
