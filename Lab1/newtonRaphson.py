import numpy as np

def newtonRaphson(f, fprime, x0, tol):
##
#  Implementation of the Newton-Raphson method to approximate
#  the root of a nonlinear function f(x)
#
#  INPUT:
#    f      - function f(x)                         OBS! passed as a lambda function
#    fprime - first derivative of the function f(x) OBS! passed as a lambda function
#    x0     - initial guess of the root location
#    tol    - error tolerance to stop the iteration
#
#  OUTPUT:
#    xVals  - sequence of approximate values for the root of the function f(x)
#    iter   - number of iterations it took to achieve user set tolerance

#  Set the maximum iteration count `max_its` and initialize a vector `xVals` to store the sequence of guesses
   max_its = 15
   xVals = np.zeros(max_its + 1)

#  save the initial guess
   xVals[0] = x0

#  perform Newton-Raphson for a fixed number of iterations
   for k in range(max_its):

#  update to the next value
      fk  = f(xVals[k])
      dfk = fprime(xVals[k])
      xVals[k+1] = xVals[k] - fk / dfk

# check the stopping condition
      stopCond = abs(f(xVals[k+1]))
      if stopCond < tol:
         xVals = xVals[0:k+2]
         iter  = k+2
         break

   return xVals, iter