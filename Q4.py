class student:
    
    def __init__(self):
        self.name = None
        self.age = None
        self.marks = None

    def validate_marks(self):
        if self.marks>65:
            return True
        else:
            return False

    def validate_age(self):
        if self.age>=20:
            return True
        else:
            return False

    def check_qualification(self):
        if self.validate_age() and self.validate_marks():
            return True

    def get_info(self):
        self.name = input("Enter the name:")
        self.age = int(input ("Enter the age:"))
        self.marks = int(input ("Enter the marks:"))

    def put_info(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Marks:",self.marks)


me = student()
me.get_info()
if( me.check_qualification()):
    print("Student is applicable for admission!!")
    me.put_info()

else:
    print("Sudent is not applicable for admission!")
    







