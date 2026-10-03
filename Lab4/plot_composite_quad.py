import numpy as np
import matplotlib.pyplot as plt

def plot_composite_quad(f, x):
#
#  Script that will plot a function and the interval boundaries for use
#  with a composite quadrature rule
#
#  INPUT:
#
#     f - integrand function
#     x - set of nodes used for the composite quadrature rule
#
#  OUTPUT:
#
#     NONE - Produces plot to screen

#  Sample the function at an enriched set of points
   x_more = np.linspace(x[0], x[-1], 500)
   f_vals = f(x_more)

#  Create a figure and axis
   fig, ax = plt.subplots(figsize=(8, 8))

#  Plot the function
   p1, = ax.plot(x_more, f_vals, '-k', linewidth=2)

#  Use a stem plot for the quadrature nodes and customize the colors and annotations
   p2 = ax.stem(x, f(x), linefmt='-', markerfmt='o', basefmt=' ')
   plt.setp(p2.markerline, markersize=9, markerfacecolor=(0.91, 0.41, 0.17), color=(0.91, 0.41, 0.17))
   plt.setp(p2.stemlines, linewidth=1.5, color=(0.91, 0.41, 0.17))

#  Set font size and add the legend
   ax.tick_params(labelsize=16)

   ax.legend(
      [p1, p2.markerline],
      [r'$(x+1)^2\cos\left(\frac{2x+1}{x-3.3}\right)$', 'Quadrature nodes'],
      loc='upper left',
      fontsize=20
   )

#  Display the figure
   plt.show()