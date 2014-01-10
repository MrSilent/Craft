import socket
from builder import *
from Tkinter import *

class ProBuild(Frame):
    def createWidgets(self):
                def cmd():
                    client.__init__()
                    if variable.get() == 'Pyramid':
                        client.set_blocks(pyramid(int(e1.get()), int(e2.get()), int(e3.get()), int(e4.get()), int(e5.get())), int(e6.get()))
                    if variable.get() == 'Inverted Pyramid':
                         client.set_blocks(upyramid(int(e1.get()), int(e2.get()), int(e3.get()), int(e4.get()), int(e5.get())), int(e6.get()))
                def cmd1():
                    client.__init__()
                    if variable1.get() == 'Sphere':
                        client.set_blocks(sphere(int(f1.get()), int(f2.get()), int(f3.get()), int(f4.get())), int(f5.get()))
                    if variable1.get() == 'Circle X':
                        client.set_blocks(circle_x(int(f1.get()), int(f2.get()), int(f3.get()), int(f4.get())), int(f5.get()))
                    if variable1.get() == 'Circle Y':
                        client.set_blocks(circle_y(int(f1.get()), int(f2.get()), int(f3.get()), int(f4.get())), int(f5.get()))
                    if variable1.get() == 'Circle Z':
                        client.set_blocks(circle_z(int(f1.get()), int(f2.get()), int(f3.get()), int(f4.get())), int(f5.get()))
        
                variable  = StringVar()
                variable.set('Pyramid')
                variable1 = StringVar()
                variable1.set('Sphere')

                f = OptionMenu(None, variable1, 'Sphere', 'Circle X', 'Circle Y', 'Circle Z') ##TODO: Add functions
                f1 = Entry()
                f2 = Entry()
                f3 = Entry()
                f4 = Entry()
                f5 = Entry()
                f1.insert(0, 'Center X')
                f2.insert(0, 'Center Y')
                f3.insert(0, 'Center Z')
                f4.insert(0, 'Radius')
                f5.insert(0, 'Block Type#')
                f.pack(anchor=W)
                f1.pack(anchor=W)
                f2.pack(anchor=W)
                f3.pack(anchor=W)
                f4.pack(anchor=W)
                f5.pack(anchor=W)
                b1 = Button(None, text='BUILD', fg='red', command=cmd1)
                b1.pack(fill=None, expand=0, anchor=W)

                e = OptionMenu(None, variable, 'Pyramid', 'Inverted Pyramid')
                e1 = Entry()
                e2 = Entry()
                e3 = Entry()
                e4 = Entry()
                e5 = Entry()
                e6 = Entry()  ##TODO: Make this a scrollable options widget.
                e1.insert(0, 'Start Pos X')
                e2.insert(0, 'End Pos X')
                e3.insert(0, 'Start Pos y')
                e4.insert(0, 'Start Pos Z')
                e5.insert(0, 'End Pos Z')
                e6.insert(0, 'Block Type#')
                e.pack(anchor=W)
                e1.pack(anchor=W)
                e2.pack(anchor=W)
                e3.pack(anchor=W)
                e4.pack(anchor=W)
                e5.pack(anchor=W)
                e6.pack(anchor=W)
                client = Client()
                b = Button(None, text='BUILD', fg='blue', command=cmd)
                b.pack(fill=None, expand=0, anchor=W)
                
                
                
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
probuild = ProBuild(master=root)
probuild.master.title("ProBuilder for Craft")
probuild.master.maxsize(768, 480)
probuild.mainloop()
root.destroy()
