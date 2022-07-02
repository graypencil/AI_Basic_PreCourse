def f(x):
    result =  2 * x  + 7
    return result
    

def g(x):
    result = x ** 2
    return result


x = 2

print("result:", f(x) + g(x) + f(g(x)) + g(f(x)))
