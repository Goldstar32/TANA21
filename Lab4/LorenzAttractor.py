import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def LorenzAttractor(T):
#
# fun example of nonlinear dynamics (possibility for the final lab)
# solve the Lorenz equations for a strange attractor:
#
#      d(x1)/dt = P(x2-x1)
#      d(x2)/dt = Rx1 - x2 - x1x3
#      d(x3)/dt = x1x2 - Bx3

# use a very adhoc tactic to set the time step
   num_steps = 2500
   dt = T / num_steps

# set the initial condition and allocate memory for the solution vector
   y = np.zeros((3,num_steps,))
   ini = 5 * np.ones((3,))

# save the initial condition and enter the Runge-Kutta loop to solve the ODE
   y[:, 0] = ini.copy()
   for i in range(1, num_steps):
      k1 = RHS(y[:, i-1])
      k2 = RHS(y[:, i-1] + 0.5 * dt * k1)
      k3 = RHS(y[:, i-1] + 0.5 * dt * k2)
      k4 = RHS(y[:, i-1] + dt * k3)
      y[:, i] = y[:, i-1] + dt * (k1 + 2 * k2 + 2 * k3 + k4) / 6

# visualize the solution progressively
   fig = plt.figure()
   ax = fig.add_subplot(111, projection='3d')

   ax.set_xlim([-20, 20])
   ax.set_ylim([-30, 30])
   ax.set_zlim([0, 50])
   ax.grid(True)

   for n in range(1, len(y[0]) // 7 + 1):
      ax.cla() # clear the figure to redraw

      # Set axis limits
      ax.set_xlim([-20, 20])
      ax.set_ylim([-30, 30])
      ax.set_zlim([0, 50])
      ax.grid(True)

      ax.plot(y[0, :7*n], y[1, :7*n], y[2, :7*n], 'b', linewidth=0.5)

      # update view angle dynamically
      ax.view_init(elev=24, azim=-37.5 - n)
      plt.pause(0.02)

   plt.show()

###
#  auxiliary function to get the right hand side
###
def RHS(y):
#
# evaluate the right hand side of the nonlinear ODE for the Lorenz
# attractor
   dy    = np.zeros((3,))
   dy[0] =
   dy[1] =
   dy[2] =

   return dy