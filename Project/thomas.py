import numpy as np

# create three random vectors
main = N * np.ones((N,)) + np.random.rand((N,))
sub = np.random.rand((N - 1,))
super = np.random.rand((N - 1,))
# use the ’np.diag’ command to create tridiagonal matrix
A = np.diag(sub, k=-1) + np.diag(main, k=0) + np.diag(super, k=1)
