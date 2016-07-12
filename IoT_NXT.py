
# coding: utf-8

# # Projecte IoT -> Fer una aplicació per a controlar remotament el lego NXT
# 
# ## Requeriments :
# 
# NXT-python:
# 
# > `git clone https://github.com/Eelviny/nxt-python.git` 
# 
# > `cd nxt-python`
# 
# > `python setup.py install`
# 
# BLUEZ:
# 
# > `pip3 install pybluez

# In[8]:

from tkinter import *
class App:
    def __init__(self, master,brick):
        frame = Frame(master)
        frame.pack()
        #self.quit = Button(frame, 
        #                     text="QUIT", fg="red",
        #                     command=frame.quit)
        #self.quit.pack(side=LEFT)
        self.m_left = Motor(brick, PORT_B)
        self.m_right = Motor(brick, PORT_C)

        self.left = Button(frame,
                             text="left",
                             command=self.left)
        self.left.pack(side=LEFT)

        self.up = Button(frame,
                             text="up",
                             command=self.up)
        self.up.pack(side=TOP)

        self.down = Button(frame,
                             text="down",
                             command=self.down)
        self.down.pack(side=BOTTOM)

        self.right = Button(frame,
                             text="right",
                             command=self.right)
        self.right.pack(side=RIGHT)

        self.center = Button(frame,
                             text="stop",
                             command=self.stop)
        self.center.pack(side=LEFT)

    def up(self):
        m_right.run(100)
        m_left.run(100)
        
    def down(self):
        m_right.run(-100)
        m_left.run(-100)
            
    def right(self):
        m_right.turn(100, 360)
        m_left.idle()
    def left(self):
        m_left.turn(100, 360)
        m_right.idle()
    def stop(self):
        m_right.idle()
        m_left.idle()
        
root = Tk()
brick = nxt.locator.find_one_brick()

app = App(root,b)

root.mainloop()

