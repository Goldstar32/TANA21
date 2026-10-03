import numpy as np

def lufact(A):
#
#  Computes the LU factorization of the matrix A. The factorization is done
#  in-place and then the L and U matrices are extracted at the end for
#  output. The factorization is PA = LU
#
#  INPUT:
#    A - n by n square, non-singular matrix
#
#  OUTPUT:
#    L - lower triangular matrix with ones along the main diagonal
#    U - upper triangular matrix
#    P - permutation matrix for pivoting

#  allow function to overwrite the original matrix (avoid reference pointer)
   A = A.copy()

#  ensure that the array uses `float` to avoid possible integer division
   A = A.astype(float)

#  get the size of the system
   n, _ = A.shape

#  initialize the pivoting matrix
   P = np.eye(n)

#  Vectorized in-place LU factorization (with row pivoting) that keeps
#  track of the total permutations by scrambling the matrix P
   for j in range(n-1):

# Find the index of the largest pivot element in the current column


# Swap the rows within the in-place array as well as the permutation matrix P


# Perform the in-place elimination and save the new column of L
      i = range(j + 1, n) # indices for the "active" matrix portion
      A[i, j] = A[i, j] / A[j, j]
      A[j+1:n, j+1:n] = A[j+1:n, j+1:n] - np.outer(A[i, j], A[j, i])
      # print(A)
      # return # this exits the function on the first iteration

# Extract L and U from the in-place form
   U = np.triu(A)
   L = np.eye(n) + np.tril(A, -1)

   return L, U, P
