#program that computes the quadratic equation
from math import sqrt 
print "Quadratic Equations: ax^2+bx+c = 0"
a = input("Enter a:")
b = input("Enter b:")
c = input("Enter c:")
solution = (b**2)-((4*(a*c)))
if solution < 0:
    print str(a) + "x^2+" + str(b) + "x+" + str(c) + "has no solutions."
elif solution == 0:
    x = (-b+sqrt(solution))/(2*a)
    print str(a) + "x^2+" + str(b) + "x+" + str(c) + "has one solution."
    print "Solution:",x
else:
    x1 = (-b+sqrt(solution))/(2*a)
    x2 = (-b-sqrt(solution))/(2*a)
    print str(a) + "x^2+" + str(b) + "x+" + str(c) + "has two solutions."
    print "Solution1:", x1
    print "Solution2:", x2
