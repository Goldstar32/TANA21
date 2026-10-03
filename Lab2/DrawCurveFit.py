import numpy as np
import matplotlib.pyplot as plt

def DrawCurveFit(c, t, y):
#
#  Given the original data points (t_i, y_i) and the coefficients c_j
#  for the curve fitting ansatz
#     f(t) = c_1 + c_2 * cos(2 * pi * t / T) + c_3 * sin(2 * pi * t / T)
#                + c_4 * cos(4 * pi * t / T) + c_5 * sin(4 * pi * t / T)
#  where T = t(end) - t(1).
#  This function plots the curve fitting and the original points in the
#  same figure.
#
#  INPUT:
#    c - Vector of coefficient values
#    t - Vector of original time values
#    y - Vector of original data values
#
#  OUTPUT:
#    prints a figure to the screen

#  Compute length of the time interval

   T = t[-1] - t[0]

#  Get an enriched set of uniform points in the interval [t(1), t(end)]
#  for nicer plotting

   tt = np.linspace(t[0], t[-1], 200)

#  Compute the curve ansatz on the enriched points

   f = (c[0] + c[1] * np.cos(2 * np.pi * tt / T) + c[2] * np.sin(2 * np.pi * tt / T)
             + c[3] * np.cos(4 * np.pi * tt / T) + c[4] * np.sin(4 * np.pi * tt / T))

#  Make a new figure (avoids overwriting an existing figure)

   plt.figure()

# Plot original data points with blue dots
   plt.plot(t, y, 'bo', markerfacecolor='b', markersize=7, label='Data')

# Plot curve fit with a red solid line
   plt.plot(tt, f, 'r-', linewidth=1.5, label='Fit')

# Set x-axis limits

   plt.xlim(t[0], t[-1])

# Label axes with LaTeX

   plt.xlabel(r"time (s)", fontsize=20)
   plt.ylabel(r"blood pressure (mmHg)", fontsize=20)

# Set font size for all ticks

   plt.tick_params(labelsize=20)

# Add the legend
   plt.legend(fontsize=16)

# Show the figure
   plt.show()