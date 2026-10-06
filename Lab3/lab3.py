import numpy as np

# 3.1

# a)

# This sucks but I wont be bothered to change it
_h = 1/5

def Dxa(N = 5, h = False):
    if not h:
        h = 1/N


    # Interior central differences
    lower = np.diag(-np.ones(N)/(2*h), -1)
    upper = np.diag( np.ones(N)/(2*h), 1)

    Dx = lower + upper

    # Replace boundary differences
    Dx[0, 0] = -1/h
    Dx[0, 1] =  1/h

    Dx[N, N-1] = -1/h
    Dx[N, N]   =  1/h

    return Dx

print("3.1 a)\n", Dxa())

# b)
print("b)")

f = (np.array([1, 1, 1, 1, 1, 1])*_h).transpose()
print("f(x) = 1\n", Dxa()@f)

f = (np.array([0, 1, 2, 3, 4, 5])*_h).transpose()
print("f(x) = x\n", Dxa()@f)

f = (np.array([0, 1, 4, 9, 16, 25])*_h*_h).transpose()
print("f(x) = x²\n", Dxa()@f)

# c)
print("c)")

def Dxc(N = 5):
    Dx = Dxa(N)
    Dx[0, 0] = -3/(2*_h)
    Dx[0, 1] = 4/(2*_h)
    Dx[0, 2] = -1/(2*_h)
    Dx[0, -1] = 1/(2*_h)
    Dx[0, -2] = -4/(2*_h)
    Dx[0, -3] = 3/(2*_h)
    return Dx

f = (np.array([1, 1, 1, 1, 1, 1])*_h).transpose()
f_der = Dxc()@f
print("f(x) = 1\n", f_der)

f = (np.array([0, 1, 2, 3, 4, 5])*_h).transpose()
f_der = Dxc()@f
print("f(x) = x\n", f_der)

f = (np.array([0, 1, 4, 9, 16, 25])*_h*_h).transpose()
f_der = Dxc()@f
print("f(x) = x²\n", f_der)

# d)
print("d)")

def fx(x):
    return np.exp(np.sin(4*x))

def fp(x):
    return 4*np.cos(4*x)*np.exp(np.sin(4*x))

def error(N, Dx = Dxa):
    max = 0
    f = np.array(list(map(fx, np.arange(N + 1)*_h))).transpose()
    f_der = Dx(N)@f

    for i in np.arange(N + 1):
        err = np.abs(fp(i*_h)-f_der[i])
        if err > max:
            max = err

    return max

print("Using stencil from a)")
print("N = 10, error =", error(10))
print("N = 100, error =", error(100))
print("N = 1000, error =", error(1000))

print("\nUsing stencil from c)")
print("N = 10, error =", error(10, Dxc))
print("N = 100, error =", error(100, Dxc))
print("N = 1000, error =", error(1000, Dxc))
