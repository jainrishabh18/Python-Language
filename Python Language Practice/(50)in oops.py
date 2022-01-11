
class computer:

    def __init__(self,cpu,ram):
        self.cpu= cpu
        self.ram= ram


    def config(self):
        print("config is",self.cpu,self.ram)


com1=computer(cpu ='i5',ram ='16')#here cpu shows that even i will
                                  # interchange the value
                                  # than also it will come in their
                                  # respective places cpu i5 and ram is 16
com2=computer('ryzen',8)

com1.config()
com2.config()