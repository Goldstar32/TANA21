import numpy as np

def thinQR(A):
#
#  This computes the "thin" version of the QR factorization using modified
#  Gram-Schmidt to find the orthogonal columns of the matrix Q.
#
#  INPUT:
#    A - m x n matrix where m >= n that is assumed to have linearly
#        independent columns
#
#  OUTPUT:
#    Q - m x n orthogonal matrix such that Q'*Q = eye(n)
#    R - n x n upper triangular matrix

#  pull the size of the rectangular system and allocate memory
   m, n = A.shape

   v = np.zeros((m, n,))
   Q = np.zeros((m, n,))
   R = np.zeros((n, n,))

#  copy the columns of the matrix A into vectors that we will use for the
#  modified Gram-Schmidt. Uses extra memory but done for clarity.
   for j in range(n):
      v[:, j] = A[:, j]

#  now go through and determine the columns of Q and the upper
#  triangular matrix R
   for j in range(n):
      R[j, j] = np.linalg.norm(v[:, j])
      Q[:, j] = v[:, j] / R[j, j]
      for k in range(j+1, n):
         R[j, k] = np.dot(Q[:, j], v[:, k])
         v[:, k] = v[:, k] - R[j, k] * Q[:, j]

   return Q, R