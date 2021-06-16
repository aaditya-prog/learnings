# using class methods as alternative constructors
class People:
    pass

    def __init__(self, fname, lname, address):
        self.fname = fname
        self.lname = lname
        self.address = address

    @classmethod
    def from_str(cls, Pstring):
        fname, lname, address = cls.from_str = Pstring.split("-")
        return cls(fname, lname, address)


ram = People.from_str("Ram-Kumar-Sarlahi")

print(ram.address)
