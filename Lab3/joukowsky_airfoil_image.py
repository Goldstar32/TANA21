import numpy as np
import matplotlib.pyplot as plt

def disp_joukowsky_airfoil():
#
#  This performs the conformal mapping to create a particular instance of a Joukowsky airfoil
#
   theta = np.linspace(0, 2 * np.pi, 300) # angles
   r     = 1.0                            # radius
   s     = 0.175 + 1j * 0.215             # circle origin
   zeta  = s + r * np.exp(1j * theta)     # original circle values in complex space (written in polar form)
   k     = r - s                          # transformation parameter
   z     = zeta + k**2 / zeta             # conformal mapping of airfoil surface in complex space
   z     = z * np.exp(1j * np.pi / 11)    # rotate airfoil location

# Make a new figure
   fig, ax = plt.subplots(figsize=(15, 4))

# Plot the airfoil profile
   ax.plot(-z.real, z.imag, '-k', linewidth=1.5)

# Set limits and such
   ax.set_xlim([-2.0, 2.0])
   ax.set_ylim([-0.2, 0.9])
   ax.set_aspect('equal')
   ax.tick_params(labelsize=16)

# Fill with light gray
   ax.fill(-z.real, z.imag, 'k', alpha=0.05, linewidth=0)

# Return the figure environment for later use
   return fig, ax

# Runs only if this file is executed directly,
# ignored if imported
if __name__ == "__main__":
   disp_joukowsky_airfoil()
   plt.show()
