# label = an area widget that holds text or/and an image within a window

from tkinter import *

window = Tk()

# photo = PhotoImage(file='C:\\Users\\USER\\OneDrive - International Islamic University Malaysia\\Pictures\\Saved Pictures\\karina.jpg')

label = Label(window, 
              text="Hello World", 
              font=('Arial', 40, 'bold'), 
              fg='#00FF00', 
              bg='black',
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
            #   image=photo,
            #   compound='bottom'
            )
label.pack()
# label.place(x=100,y=50)

window.mainloop()