import numpy as np

def forwardEuler(f, t0, tn, y0, h):
#
#  get the size of the problem and allocate memory
   t = np.arange(t0, tn + h, h)
   y = np.zeros(len(t))

#  save the initial values
   y[0] = y0
   t[0] = t0

#  use forward Euler with the given time step h to solve the problem and
#  save the information for later analysis
   for j in range(1, len(t)):
#  this is an explicit method so we always use values from the past solution history
      y[j] = y[j-1] + h * f(t[j-1], y[j-1])

   return t, y