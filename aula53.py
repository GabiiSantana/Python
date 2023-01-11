def f(var):
    print(var)

def f2():
    return f

var = f2()
var('imprimindo')