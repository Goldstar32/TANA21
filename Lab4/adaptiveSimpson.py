import numpy as np

def adaptiveSimpson(f, a, b, tol):
#
#  Adaptive Simpson's rule to approximate a definite integral. This uses
#  a posterioi error estimate to recursively apply Simpson's rule where it
#  is needed
#
#  INPUT:
#
#     a   - lower bound of interval
#     b   - upper bound of the interval
#     f   - integrand function
#     tol - error tolerance for adaptivity
#
#  OUTPUT:
#
#     In - adaptive approximation of the complete definite integral to
#          within the error tolerance
#     t  - vector of nodes for the boundaries of the adapted intervals (for
#          plotting)

#  perform a recursive bisection with error estimation to compute the
#  integral approximation
   m = 0.5 * (b + a) # find the current midpoint
   fa, fm, fb = f(a), f(m), f(b)
   In, x = do_integral(f, a, fa, b, fb, m, fm, tol)
   return In, x

#  helper recursive function for the adaptation
def do_integral(f, a, fa, b, fb, m, fm, tol):
   #  need the two midpoints of the sub-intervals and the function
   #  evaluations for the recursion
   xL  = 0.5 * (a + m)
   fxL = f(xL)
   xR = 0.5 * (b + m)
   fxR = f(xR)
   #  save the five nodes at the current level of the recursion
   x = np.array([a, xL, m, xR, b])
   #  get the h value for the whole interval
   h = 0.5 * (b - a)
   #  compute the Simpson's rule on the whole interval
   S_coarse = h / 3 * (fa + 4 * fm + fb) # SimpsonsRule(a,b,f,2)
   #  compute the Simpson's rule on the two subintervals
   S_Left = h / 6 * (fa + 4 * fxL + fm)  # SimpsonsRule(a,m,f,2)
   S_Right = h / 6 * (fm + 4 * fxR + fb) # SimpsonsRule(m,b,f,2)
   S_fine = S_Left + S_Right
   #  error estimate
   E = S_coarse - S_fine
   #  check against the user set tolerance
   if abs(E) < 15 * tol:
      In = S_fine # exit if tolerance is met
      return In, x
   else:
   #  bisect again if the tolerance is not met
      IL, xL = do_integral(f, a, fa, m, fm, xL, fxL, tol)
      IR, xR = do_integral(f, m, fm, b, fb, xR, fxR, tol)
      In = IL + IR
      x = np.concatenate((xL, xR[1:])) # append the node edges together (also avoids duplicates)
      return In, x