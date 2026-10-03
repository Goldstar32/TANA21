import numpy as np

# 3.1

# a)

N = 5
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

print("3.1 a)\n", Dx)

# b)
print("b)")

f = (np.array([1, 1, 1, 1, 1, 1])*h).transpose()
print("f(x) = 1\n", Dx@f)

f = (np.array([0, 1, 2, 3, 4, 5])*h).transpose()
print("f(x) = x\n", Dx@f)

f = (np.array([0, 1, 4, 9, 16, 25])*h*h).transpose()
print("f(x) = x²\n", Dx@f)

# c)
print("c)")

def f0(f):
    return (-3*f[0] + 4*f[1] - f[2])/(2*h)

def fN(f):
    return (f[-3] - 4*f[-2] + 3*f[-1])/(2*h)

f = (np.array([1, 1, 1, 1, 1, 1])*h).transpose()
f_der = Dx@f
f_der[0] = f0(f)
f_der[-1] = fN(f)
print("f(x) = 1\n", f_der)

f = (np.array([0, 1, 2, 3, 4, 5])*h).transpose()
f_der = Dx@f
f_der[0] = f0(f)
f_der[-1] = fN(f)
print("f(x) = x\n", f_der)

f = (np.array([0, 1, 4, 9, 16, 25])*h*h).transpose()
f_der = Dx@f
f_der[0] = f0(f)
f_der[-1] = fN(f)
print("f(x) = x²\n", f_der)

# d)
print("d)")

