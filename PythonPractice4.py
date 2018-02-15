#This script computes the volume of a cylinder
def circle_area(radius):
    return 3.14 * radius * radius

radius = input("Enter in radius of cylinder: ")
height = input("Enter in height of cylinder: ")
volume = height * circle_area(radius)
print volume 
