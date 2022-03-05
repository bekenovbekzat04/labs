from math import tan,pi
n=int(input("Input number of sides: "))
print("The area of the polygon is:",pow(int(input("Input the length of a side: ")),2) *n/(4*tan(pi/n)))