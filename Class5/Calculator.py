import math

def calculator(a, b, c):

    print('Your equation is %gx^2 + %gx + %g = 0.' % (a, b, c))
    x = b*b - 4*a*c
    if  x > 0: 
        y = math.sqrt(x)
        z = (-b+y)/(2*a)
        w = (-b-y)/(2*a) 
        print('The solutions to the equation are: %g, %g' % (z, w)) 
    elif x == 0:
        z = -b/(2*a)
        print('The solution to the equation is: %g' % z)
    else:
        print('There is no solution to the equation.')