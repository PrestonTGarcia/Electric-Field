##################################################################
# main --- Program that opens a tkinter window that asks the user#
# to enter x, y, z and q values for each of the particles that   #
# create the electric field. The submit button links to the      #
# visualization.py program and passes in the data that the user  #
# enters into the main window.                                   #
# @author Preston Garcia                                         #
##################################################################

import tkinter as tk
import visualization

#Constants
GEOMETRY = "500x200"
TITLE = "Electric Field Visualization"
BACKGROUND = "white"

def main():
    """Opens up the main window to ask the user for information
    about the two particles creating the electric field."""

    root = tk.Tk()

    # window settings
    root.title(TITLE)
    root.geometry(GEOMETRY)
    root.configure(bg=BACKGROUND)
    #TODO: add image for the icon of the window

    # x1 section
    x1Label = tk.Label(root, text="x₁ = ", bg=BACKGROUND)
    x1Entry = tk.Entry(root, width=3, bd=2)
    x1MLabel = tk.Label(root, text="m", bg=BACKGROUND)

    # y1 section
    y1Label = tk.Label(root, text="y₁ = ", bg=BACKGROUND)
    y1Entry = tk.Entry(root, width=3, bd=2)
    y1MLabel = tk.Label(root, text="m", bg=BACKGROUND)

    # z1 section
    z1Label = tk.Label(root, text="z₁ = ", bg=BACKGROUND)
    z1Entry = tk.Entry(root, width=3, bd=2)
    z1MLabel = tk.Label(root, text="m", bg=BACKGROUND)

    # q1 section
    q1Label = tk.Label(root, text="q₁ = ", bg=BACKGROUND)
    q1Entry = tk.Entry(root, width=3, bd=2)
    q1CLabel = tk.Label(root, text="C", bg=BACKGROUND)

    # x2 section
    x2Label = tk.Label(root, text="x₂ = ", bg=BACKGROUND)
    x2Entry = tk.Entry(root, width=3, bd=2)
    x2MLabel = tk.Label(root, text="m", bg=BACKGROUND)

    # y2 section
    y2Label = tk.Label(root, text="y₂ = ", bg=BACKGROUND)
    y2Entry = tk.Entry(root, width=3, bd=2)
    y2MLabel = tk.Label(root, text="m", bg=BACKGROUND)

    # z2 section
    z2Label = tk.Label(root, text="z₂ = ", bg=BACKGROUND)
    z2Entry = tk.Entry(root, width=3, bd=2)
    z2MLabel = tk.Label(root, text="m", bg=BACKGROUND)

    # q2 section
    q2Label = tk.Label(root, text="q₂ = ", bg=BACKGROUND)
    q2Entry = tk.Entry(root, width=3, bd=2)
    q2CLabel = tk.Label(root, text="C", bg=BACKGROUND)

    # TODO: make different units available

    # All components
    componentsArr = [[[x1Label, x1Entry, x1MLabel],
                      [y1Label, y1Entry, y1MLabel],
                      [z1Label, z1Entry, z1MLabel],
                      [q1Label, q1Entry, q1CLabel]],
                     [[x2Label, x2Entry, x2MLabel],
                      [y2Label, y2Entry, y2MLabel],
                      [z2Label, z2Entry, z2MLabel],
                      [q2Label, q2Entry, q2CLabel]]]
    # First component goes at (30, 50)
    iteratingX = 30
    iteratingY = 50

    # Submit button that links to the visualization
    submitButton = tk.Button(root, text="Submit", bg="#39FC23",
                             command=lambda: visualization.main(
                                                 x1Entry.get(),
                                                 y1Entry.get(),
                                                 z1Entry.get(),
                                                 q1Entry.get(),
                                                 x2Entry.get(),
                                                 y2Entry.get(),
                                                 z2Entry.get(),
                                                 q2Entry.get()))
    # Exit button that closes the program
    exitButton = tk.Button(root, text="Exit", bg="red",
                           command=root.destroy)

    # For loop placing each of the components
    for i in componentsArr:
        for j in i:
            j[0].pack()
            j[0].place(x=iteratingX, y=iteratingY)
            iteratingX += 25
            j[1].pack()
            j[1].place(x=iteratingX, y=iteratingY)
            iteratingX += 20
            j[2].pack()
            j[2].place(x=iteratingX, y=iteratingY)
            iteratingX += 80
        iteratingX = 30
        iteratingY += 50
        
    submitButton.pack()
    submitButton.place(x=220, y=130)
    exitButton.pack()
    exitButton.place(x=230, y=160)

    root.mainloop()

if __name__ == "__main__":
    main()
