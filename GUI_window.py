# GUI
# widgets = GUI elements: buttons, textboxes, labels, image_names
# windows = servers as container to hold pr contain these widgets

from tkinter import *

window = Tk()       # instantiate an instance of a window
window.geometry("420x420")
window.title("-My first GUI-")

# icon = PhotoImage(file='265921.png')
# window.iconphoto(True, icon)
window.config(background="#5cfcff")

window.mainloop()   # place window on computer screen, listen for events