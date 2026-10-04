import numpy as np

N = 1

# create three random vectors
main = N * np.ones((N,)) + np.random.random(N)
sub = np.random.random(N - 1)
super = np.random.random(N - 1)
# use the ’np.diag’ command to create tridiagonal matrix
A = np.diag(sub, k=-1) + np.diag(main, k=0) + np.diag(super, k=1)



known_x = np.pi * np.ones((N,)) # create known solution vector filled with pi
manuf_b = A @ known_x # manufacture the right-hand-side
