class student:

    school='Rishabh public' #class method

    def __init__(self,m1,m2,m3):#instance method
        self.m1= m1
        self.m2= m2
        self.m3= m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3


    def config(self):
        print("avg is ",self.avg())
    @classmethod
    def getschool(cls):
        return cls.school

    @staticmethod #staticmethod
    def info():
        print("oy jiii sab bhadia class ma maja ma haina sab")



s1=student(34,56,45)
s2=student(54,47,15)



print(student.getschool())

student.info()

s1.config()
s2.config()
