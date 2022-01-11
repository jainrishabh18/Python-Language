class student:

    def __init__(self,name,rollnum):
        self.name=name
        self.rollnum=rollnum
        self.lap=self.laptop()

    def show(self):
        print(self.name,self.rollnum)
        self.lap.show()
    class laptop:

        def __init__(self):
            self.cpu='i5'
            self.ram=16
            self.brand='hp'

        def show(self):
            print( self.cpu, self.ram, self.brand)


s1= student('rishabh',64)
s2= student('brother',99)


s1.show()
s2.show()