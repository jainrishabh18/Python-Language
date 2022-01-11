class A:
    def feature1(self):
        print('feature1 is working')

    def feature2(self):
        print('feature2 is working')

class B:#single level inheritance if i putB(A) so b will be able to take all
    #feature from A
    def feature3(self):
        print('feature3 is working')

    def feature4(self):
        print('feature4 is working')

class C(A,B):#multiple inheritance
    #multi level inheritance is when C take IT like A,B(A),C(B)
    #then it will be multi level inheritance
    def feature5(self):
        print('feature5 is working')

    def feature6(self):
        print('feature6 is working')


a1=A()
a1.feature2()



b1=B()
b1.feature4()


c1=C()
c1.feature1()
c1.feature4()
