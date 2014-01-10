import socket
from builder import *
from Tkinter import *

class PyBuild(Frame):
    def createWidgets(self):

                e1 = Entry()
                e2 = Entry()
                e3 = Entry()
                e4 = Entry()
                e5 = Entry()
                e6 = Entry()
                e1.insert(0, 'Start pos X')
                e2.insert(0, 'End pos X')
                e3.insert(0, 'Start pos y')
                e4.insert(0, 'Start pos Z')
                e5.insert(0, 'End pos Z')
                e6.insert(0, 'Block Type#')
                e1.pack()
                e2.pack()
                e3.pack()
                e4.pack()
                e5.pack()
                e6.pack()
                client = Client()
                def cmd():
                    client.__init__()
                    client.set_blocks(pyramid(int(e1.get()), int(e2.get()), int(e3.get()), int(e4.get()), int(e5.get())), int(e6.get()))
                self.EXEC = Button(self)
                self.EXEC["text"] = "CAUTION!"
                self.EXEC["fg"]   = "red"
                self.EXEC["command"] = cmd

                self.EXEC.pack({"side": "left"})
                
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
pybuild = PyBuild(master=root)
pybuild.master.title("Pyramid Builder for Craft")
pybuild.master.maxsize(768, 480)
pybuild.mainloop()
root.destroy()
