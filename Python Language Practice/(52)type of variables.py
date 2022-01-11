class car:

    wheels=4

    def __init__(self):
        self.mill=10
        self.company='porshe'



c1=car()
c2=car()

car.wheels=5

print(c1.mill,c1.company,c1.wheels)
print(c2.mill,c2.company,c2.wheels)
