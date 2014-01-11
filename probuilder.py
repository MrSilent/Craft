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
        
                def cmd2():
                    client.__init__()
                    if variable2.get() == 'Cuboid Filled':
                        client.set_blocks(cuboid(int(g1.get()), int(g2.get()), int(g3.get()), int(g4.get()), int(g5.get()), int(g6.get())), int(g7.get()))
                    if variable2.get() == 'Cuboid Empty':
                         client.set_blocks(cuboid1(int(g1.get()), int(g2.get()), int(g3.get()), int(g4.get()), int(g5.get()), int(g6.get())), int(g7.get()))
        
                def cmd3():
                    client.__init__()
                    if variable3.get() == 'Cylinder Y':
                        client.set_blocks(cylinder_y(int(h1.get()), int(h2.get()), int(h3.get()), int(h4.get()), int(h5.get())), int(h6.get()))
                    if variable3.get() == 'Cylinder X':
                         client.set_blocks(cylinder_x(int(h1.get()), int(h2.get()), int(h3.get()), int(h4.get()), int(h5.get())), int(h6.get()))
                    if variable3.get() == 'Cylinder Z':
                         client.set_blocks(cylinder_z(int(h1.get()), int(h2.get()), int(h3.get()), int(h4.get()), int(h5.get())), int(h6.get()))
                    if variable3.get() == 'Cone Y':
                         client.set_blocks(cone_y(int(h1.get()), int(h2.get()), int(h3.get()), int(h4.get()), int(h5.get())), int(h6.get()))
        
                variable  = StringVar()
                variable.set('Pyramid')
                variable1 = StringVar()
                variable1.set('Sphere')
                variable2 = StringVar()
                variable2.set('Cuboid Filled')
                variable3 = StringVar()
                variable3.set('Cylinder Y')

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
                b = Button(None, text='BUILD', fg='red', command=cmd1)
                b.pack(fill=None, expand=0, anchor=W)
                
                g = OptionMenu(None, variable2, 'Cuboid Filled', 'Cuboid Empty')
                g1 = Entry()
                g2 = Entry()
                g3 = Entry()
                g4 = Entry()
                g5 = Entry()
                g6 = Entry()
                g7 = Entry()
                g1.insert(0, 'Start Pos X')
                g2.insert(0, 'End Pos X')
                g3.insert(0, 'Start Pos Y')
                g4.insert(0, 'End Pos Y')
                g5.insert(0, 'Start Pos Z')
                g6.insert(0, 'End Pos Z')
                g7.insert(0, 'Block Type#')
                g.pack(anchor=W)
                g1.pack(anchor=W)
                g2.pack(anchor=W)
                g3.pack(anchor=W)
                g4.pack(anchor=W)
                g5.pack(anchor=W)
                g6.pack(anchor=W)
                g7.pack(anchor=W)
                b1 = Button(None, text='BUILD', fg='green', command=cmd2)
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
                b2 = Button(None, text='BUILD', fg='blue', command=cmd)
                b2.pack(fill=None, expand=0, anchor=W)
                
                h = OptionMenu(None, variable3, 'Cylinder Y', 'Cylinder X', 'Cylinder Z', 'Cone Y')
                h1 = Entry()
                h2 = Entry()
                h3 = Entry()
                h4 = Entry()
                h5 = Entry()
                h6 = Entry()  
                if variable3.get() == 'Cylinder Y':
                    h1.insert(0, 'Start Pos X')
                    h2.insert(0, 'Start Pos Y')
                    h3.insert(0, 'End Pos Y')
                    h4.insert(0, 'Start Pos Z')
                    h5.insert(0, 'Radius')
                    h6.insert(0, 'Block Type#')
                if variable3.get() == 'Cylinder X':
                    h1.insert(0, 'Start Pos X')
                    h2.insert(0, 'End Pos X')
                    h3.insert(0, 'Start Pos Y')
                    h4.insert(0, 'Start Pos Z')
                    h5.insert(0, 'Radius')
                    h6.insert(0, 'Block Type#')
                if variable3.get() == 'Cylinder Z':
                    h1.insert(0, 'Start Pos X')
                    h2.insert(0, 'Start Pos Y')
                    h3.insert(0, 'Start Pos Z')
                    h4.insert(0, 'End Pos Z')
                    h5.insert(0, 'Radius')
                    h6.insert(0, 'Block Type#')
                if variable3.get() == 'Cone Y':
                    h1.insert(0, 'Start Pos X')
                    h2.insert(0, 'Start Pos Y')
                    h3.insert(0, 'End Pos Y')
                    h4.insert(0, 'Start Pos Z')
                    h5.insert(0, 'Radius')
                    h6.insert(0, 'Block Type#')
                h.pack(anchor=W)
                h1.pack(anchor=W)
                h2.pack(anchor=W)
                h3.pack(anchor=W)
                h4.pack(anchor=W)
                h5.pack(anchor=W)
                h6.pack(anchor=W)
                client = Client()
                b3 = Button(None, text='BUILD', fg='orange', command=cmd3)
                b3.pack(fill=None, expand=0, anchor=W)
                
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
