def a_calculateRectangleArea():
    print (5 * 7)


def b_calculateRectangleArea(x, y):
    print(x * y)


def c_calculateRectangleArea():
    return 5 *7 


def d_calculateRectangleArea(x, y): #파라미터 값도 있고, return 값도 있어야함.
    return x * y
    

print(d_calculateRectangleArea(5, 7))