from functools import reduce
nums=[1,2,3,6,5,8,4,9,7]

even=list(filter(lambda n : n%2==0,nums))
print(even)

double=list(map(lambda n:n*2,even))
print(double)

sum=reduce(lambda a,b:a+b,double)
print(sum)