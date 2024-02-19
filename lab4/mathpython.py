import math as ki

#1 task

degr = float(input("Input degree:"));
radi = ki.radians(degr);

print("Output radian:", radi);

#2 task

h = float(input("Height:"));
a = float(input("Base, first value:"));
b = float(input("Base, second value:"));

print("Expected Output:", (a + b) / 2 * h);

#3 task

n = int(input("Input number of sides:"))
c = float(input("Input the length of a side:"))

print("The area of the polygon is:", (n * c ** 2) / 4 * (ki.tan(ki.pi / n)));

#4 task

l = float(input("Length of base:"));
htol = float(input("Height of parallelogram:"));

print("Expected Output:", l * htol);