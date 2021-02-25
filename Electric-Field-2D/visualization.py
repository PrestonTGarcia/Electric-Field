##################################################################
# visualization --- Program that creates a matplotlib graph that #
# visualizes the electric field created from two particles       #
# created from the user's inputs.                                #
# @author Preston Garcia                                         #
##################################################################

import matplotlib.pyplot as plt
import numpy as np
import tkinter.messagebox as mb

# Constants
K = 8.99 * 10 ** 9

def findSigns(x, y, x1, y1, q1, x2, y2, q2):
    """
    Method that finds the signs and reduces the length
    of each of the arrows in the vector field. This method
    uses the equation Fx = KQ / r^2 * rx / r and
    Fy = KQ / r^2 * ry / r. Both of these equations simplify
    to Fx = KQrx / r^3 and Fy = KQry / r^3.
    Parameters
    ----------
    x - The x coordinate of the current particle on the vector field
    y - The y coordinate of the current particle on the vector field
    x1 - The x coordinate of the first particle entered by user
    y1 - The y coordinate of the first particle entered by user
    q1 - The charge of the first particle entered by user
    x2 - The x coordinate of the second particle entered by user
    y2 - The y coordinate of the second particle entered by user
    q2 - The charge of the second particle entered by user
    Return
    ----------
    signsArr - The dx and dy of the arrow
    signsArr[0] - The dx
    signsArr[1] - The dy
    """
    # r = dx^2 + dy^2
    r1x = x - x1
    r1y = y - y1
    r1 = np.sqrt(np.square(r1x) + np.square(r1y))
    r2x = x - x2
    r2y = y - y2
    r2 = np.sqrt(np.square(r2x) + np.square(r2y))
    # denominators are saved in the case that they are 0
    denom1 = np.power(r1, 3)
    denom2 = np.power(r2, 3)
    # sets the forces to 0 if the denom is 0
    if (denom1 == 0): 
        eForce1X = 0
        eForce1Y = 0
    else: # calculates the x and y components of the force
        eForce1X = (K * q1 * r1x) / (denom1)
        eForce1Y = (K * q1 * r1y) / (denom1)
    if (denom2 == 0):
        eForce2X = 0
        eForce2Y = 0
    else:
        eForce2X = (K * q2 * r2x) / (np.power(r2, 3))
        eForce2Y = (K * q2 * r2y) / (np.power(r2, 3))
    eNetForceX = eForce1X + eForce2X
    eNetForceY = eForce1Y + eForce2Y
    xSign = eNetForceX / np.abs(eNetForceX)
    ySign = eNetForceY / np.abs(eNetForceY)
    signsArr = [0.01 * xSign, 0.01 * ySign]
    return signsArr
        

def main(x1E, y1E, q1E, x2E, y2E, q2E):
    """
    Method that creates the visualization for the electric field
    around both of the particles created by user.
    Parameters
    ----------
    x1E - The value from the x1 entry on the main window
    y1E - The value from the y1 entry on the main window
    q1E - The value from the q1 entry on the main window
    x2E - The value from the x2 entry on the main window
    y2E - The value from the y2 entry on the main window
    q2E - The value from the q2 entry on the main window
    """

    # Converts each to floats since Entry.get() returns a string
    try:

        x1 = float(x1E)
        y1 = float(y1E)
        q1 = float(q1E)
        x2 = float(x2E)
        y2 = float(y2E)
        q2 = float(q2E)

    except ValueError:
        
        mb.showerror("Value Error", "One or more of your values are not a number.")   

    midXFrom1 = (x2 - x1)/3 
    midXFrom2 = (x1 - x2)/3 
    midYFrom1 = (y2 - y1)/3 
    midYFrom2 = (y1 - y2)/3
    forceXAreas = np.arange(min(x1, x2) - 10, max(x1, x2) + 10, 1)
    forceYAreas = np.arange(min(y1, y2) - 10, max(y1, y2) + 10, 1)
    plt.title("y vs. x")
    plt.xlabel("x(m)")
    plt.ylabel("y(m)")
    plt.xlim([min(x1, x2) - 10, max(x1, x2) + 10])
    plt.ylim([min(y1, y2) - 10, max(y1, y2) + 10])

    if (q1 <= 0): #Checks if particle 1 is electron or proton
        
        plt.plot(x1, y1, 'bo') # b = electron

    else:

        plt.plot(x1, y1, 'ro') # r = proton

    if (q2 <= 0):

        plt.plot(x2, y2, 'bo')

    else:

        plt.plot(x2, y2, 'ro')

    # Coloumb force arrows
    if (q2/q1 > 0):

        plt.arrow(x1, y1, -midXFrom1, -midYFrom1, head_width=0.5)
        plt.arrow(x2, y2, -midXFrom2, -midYFrom2, head_width=0.5)

    else:

        plt.arrow(x1, y1, midXFrom1, midYFrom1, head_width=0.5)
        plt.arrow(x2, y2, midXFrom2, midYFrom2, head_width=0.5)

    # Electric field arrows
    for i in range(0, len(forceXAreas)):

        for j in range(0, len(forceYAreas)):

            signs = findSigns(forceXAreas[i], forceYAreas[j], x1, y1, q1,
                              x2, y2, q2)
            plt.arrow(forceXAreas[i], forceYAreas[j], signs[0], signs[1], head_width=0.3) 

    plt.show()
