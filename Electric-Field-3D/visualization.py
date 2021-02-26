##################################################################
# visualization --- Program that creates a 3D matplotlib graph   #
# that visualizes the electric field created from two particles  #
# created from the user's inputs.                                #
# @author Preston Garcia                                         #
##################################################################

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

# Constants
K = 8.99 * np.power(10, 9)

def createSphere(c, r):
    """Method that creates the information for the sphere
    that represents the particles given the center and the
    radius of the sphere.
    Parameters
    ----------
    c - The array containing the x, y, and z coordinates of
    the center of the sphere.
    r - The radius of the sphere.
    Return
    ----------
    [x, y, z] - The datapoints for the entire cirlce in the x,
    y, and z directions.
    """
    phi = np.linspace(0, 2*np.pi, 100)
    theta = np.linspace(0, np.pi, 100)
    x = r * np.outer(np.cos(phi), np.sin(theta)) + c[0] 
    y = r * np.outer(np.sin(phi), np.sin(theta)) + c[1]
    z = r * np.outer(np.ones(np.size(phi)), np.cos(theta)) + c[2]
    return [x, y, z]

def findSigns(x, y, z, x1, y1, z1, q1, x2, y2, z2, q2):
    """
    Method that finds the signs and reduces the length
    of each of the arrows in the vector field. This method
    uses the equation Fx = KQ / r^2 * rx / r,
    Fy = KQ / r^2 * ry / r and Fz = KQ / r^2 * rz / r.
    All of these equations simplify to Fx = KQrx / r^3 and
    Fy = KQry / r^3 and Fz = KQrz / r^3.
    Parameters
    ----------
    x - The x coordinate of the current particle on the vector field
    y - The y coordinate of the current particle on the vector field
    z - The z coordinate of the current particle on the vector field
    x1 - The x coordinate of the first particle entered by user
    y1 - The y coordinate of the first particle entered by user
    z1 - The z coordinate of the first particle entered by user
    q1 - The charge of the first particle entered by user
    x2 - The x coordinate of the second particle entered by user
    y2 - The y coordinate of the second particle entered by user
    z2 - The z coordinate of the second particle entered by user
    q2 - The charge of the second particle entered by user
    Return
    ----------
    signsArr - The xf, yf, zf, and net force of the arrows
    signsArr[0] - The xf
    signsArr[1] - The yf
    signsArr[2] - The zf
    signs
    """
    r1x = x - x1
    r1y = y - y1
    r1z = z - z1
    r1 = np.sqrt(np.square(r1x) + np.square(r1y) + np.square(r1z))
    r2x = x - x2
    r2y = y - y2
    r2z = z - z2
    r2 = np.sqrt(np.square(r2x) + np.square(r2y) + np.square(r2z))
    denom1 = np.power(r1, 3)
    denom2 = np.power(r2, 3)
    if (denom1 == 0):
        eForce1X = 0
        eForce1Y = 0
        eForce1Z = 0
    else:
        eForce1X = (K * q1 * r1x) / (denom1)
        eForce1Y = (K * q1 * r1y) / (denom1)
        eForce1Z = (K * q1 * r1z) / (denom1)
    if (denom2 == 0):
        eForce2X = 0
        eForce2Y = 0
        eForce2Z = 0
    else:
        eForce2X = (K * q2 * r2x) / (denom2)
        eForce2Y = (K * q2 * r2y) / (denom2)
        eForce2Z = (K * q2 * r2z) / (denom2)
    eNetX = eForce1X + eForce2X
    eNetY = eForce1Y + eForce2Y
    eNetZ = eForce1Z + eForce2Z
    eNetForce = np.sqrt(np.square(eNetX) + np.square(eNetY) + np.square(eNetZ))
    signsArr = [eNetX / np.abs(eNetX), eNetY / np.abs(eNetY), eNetZ / np.abs(eNetZ), eNetForce]
    return signsArr

def main(x1E, y1E, z1E, q1E, x2E, y2E, z2E, q2E):
    """
    Method that creates the visualization for the electric field
    around both of the particles created by user.
    Parameters
    ----------
    x1E - The value from the x1 entry on the main window
    y1E - The value from the y1 entry on the main window
    z1E - The value from the z1 entry on the main window
    q1E - The value from the q1 entry on the main window
    x2E - The value from the x2 entry on the main window
    y2E - The value from the y2 entry on the main window
    z2E - The value from the z2 entry on the main window
    q2E - The value from the q2 entry on the main window
    """

    # Converts each to floats since Entry.get() returns a string
    try:
        
        x1 = float(x1E)
        y1 = float(y1E)
        z1 = float(z1E)
        q1 = float(q1E)
        x2 = float(x2E)
        y2 = float(y2E)
        z2 = float(z2E)
        q2 = float(q2E)

    except ValueError:

        mb.showerror("Value Error", "One or more of your values are not a number.")
    
    midXFrom1 = (x2 - x1)/2
    midYFrom1 = (y2 - y1)/2
    midZFrom1 = (z2 - z1)/2
    midXFrom2 = -midXFrom1
    midYFrom2 = -midYFrom1
    midZFrom2 = -midYFrom1
    signsList = []
    forceList = []
    forceXAreas = np.arange(min(x1, x2) - 10, max(x1, x2) + 10, 5)
    forceYAreas = np.arange(min(y1, y2) - 10, max(y1, y2) + 10, 5)
    forceZAreas = np.arange(min(z1, z2) - 10, max(z1, z2) + 10, 5)
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.set_xlim(min(x1, x2) - 10, max(x1, x2) + 10)
    ax.set_ylim(min(y1, y2) - 10, max(y1, y2) + 10)
    ax.set_zlim(min(z1, z2) - 10, max(z1, z2) + 10)
    p1 = createSphere([x1, y1, z1], 1)
    p2 = createSphere([x2, y2, z2], 1)
    
    if (q1 <= 0): #Checks for protons or electrons
        
        ax.plot_surface(p1[0], p1[1], p1[2], color='b') # b = electron

    else:
        
        ax.plot_surface(p1[0], p1[1], p1[2], color='r') # r = proton

    if (q2 <= 0):

        ax.plot_surface(p2[0], p2[1], p2[2], color='b')

    else:

        ax.plot_surface(p2[0], p2[1], p2[2], color='r')

    # Coloumb force arrows
    if (q2/q1 > 0):

        ax.quiver(x1, y1, z1, -midXFrom1, -midYFrom1, -midZFrom1, color='black')
        ax.quiver(x2, y2, z2, -midXFrom2, -midYFrom2, -midZFrom2, color='black')

    else:

        ax.quiver(x1, y1, z1, midXFrom1, midYFrom1, midZFrom1, color='black')
        ax.quiver(x2, y2, z2, midXFrom2, midYFrom2, midZFrom2, color='black')

    # Electric field arrows
    for i in range(0, len(forceXAreas)):

        for j in range(0, len(forceYAreas)):

            for k in range(0, len(forceZAreas)):

                forceSigns = findSigns(forceXAreas[i], forceYAreas[j], forceZAreas[k], x1, y1, z1,
                                  q1, x2, y2, z2, q2)
                signsList.append([forceSigns[0], forceSigns[1], forceSigns[2]])
                forceList.append(forceSigns[3])
                #ax.quiver(forceXAreas[i], forceYAreas[j], forceZAreas[k], signs[0], signs[1], signs[2])
    threshholdOne = np.average(forceList) / 3
    threshholdTwo = threshholdOne * 2
    threshholdThree = threshholdOne * 3
    forceIndex = 0

    for i in range(0, len(forceXAreas)):

        for j in range(0, len(forceYAreas)):

            for k in range(0, len(forceZAreas)):

                if forceList[forceIndex] > threshholdThree:

                    ax.quiver(forceXAreas[i], forceYAreas[j], forceZAreas[k], signsList[forceIndex][0],
                              signsList[forceIndex][1], signsList[forceIndex][2], color="red")

                elif forceList[forceIndex] > threshholdTwo and forceList[forceIndex] < threshholdThree:

                    ax.quiver(forceXAreas[i], forceYAreas[j], forceZAreas[k], signsList[forceIndex][0],
                              signsList[forceIndex][1], signsList[forceIndex][2], color="orange")
                    
                elif forceList[forceIndex] > threshholdOne and forceList[forceIndex] < threshholdTwo:

                    ax.quiver(forceXAreas[i], forceYAreas[j], forceZAreas[k], signsList[forceIndex][0],
                              signsList[forceIndex][1], signsList[forceIndex][2], color="yellow")

                elif forceList[forceIndex] < threshholdOne:

                    ax.quiver(forceXAreas[i], forceYAreas[j], forceZAreas[k], signsList[forceIndex][0],
                              signsList[forceIndex][1], signsList[forceIndex][2], color="green")
                forceIndex += 1
    plt.show()

