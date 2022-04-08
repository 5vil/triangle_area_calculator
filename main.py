import math

a = input("Side a - ")
b = input("Side b - ")
c = input("Side c - ")

a = int(a)
b = int(b)
c = int(c)

#Calculate the Perimeter and semi perimeter required for the formula

s = (a+b+c)/2

area = math.sqrt(s*(s-a)*(s-b)*(s-c))

print('-------------------')
print('Results Calculated')
print('Perimeter - ',s*2)
print('Area - ',area )
