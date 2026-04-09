import math

def area_of_circle(radius):
    return math.pi * radius * radius  

r = float(input("Enter the radius of circle: "))
area = area_of_circle(r)
print(f"Area of circle with radius {r} is: {area:.2f}")
