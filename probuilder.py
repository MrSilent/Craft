import socket
from builder import *
from Tkinter import *

class ProBuild(Frame):
    def createWidgets(self):
                def cmd():
                    x = 0
                    if variable1.get() == 'EMPTY':
                        x = 0
                    if variable1.get() == 'GRASS':
                        x = 1
                    if variable1.get() == 'SAND':
                        x = 2
                    if variable1.get() == 'STONE':
                        x = 3
                    if variable1.get() == 'BRICK':
                        x = 4
                    if variable1.get() == 'WOOD':
                        x = 5
                    if variable1.get() == 'CEMENT':
                        x = 6
                    if variable1.get() == 'DIRT':
                        x = 7 
                    if variable1.get() == 'PLANK':
                        x = 8
                    if variable1.get() == 'SNOW':
                        x = 9
                    if variable1.get() == 'GLASS':
                        x = 10
                    if variable1.get() == 'COBBLE':
                        x = 11
                    if variable1.get() == 'LIGHT':
                        x = 12
                    if variable1.get() == 'DARK':
                        x = 13
                    if variable1.get() == 'CHEST':
                        x = 14
                    if variable1.get() == 'LEAVES':
                        x = 15
                    if variable1.get() == 'CLOUD':
                        x = 16
                    if variable1.get() == 'TALL GRASS':
                        x = 17
                    if variable1.get() == 'YELLOW FLOWER':
                        x = 18
                    if variable1.get() == 'RED FLOWER':
                        x = 19
                    if variable1.get() == 'PURPLE FLOWER':
                        x = 20
                    if variable1.get() == 'SUN FLOWER':
                        x = 21
                    if variable1.get() == 'WHITE FLOWER':
                        x = 22
                    if variable1.get() == 'BLUE FLOWER':
                        x = 23
                    
                    if variable.get() == 'Pyramid':
                        client.set_blocks(pyramid(int(f0.get()), int(f1.get()), int(f2.get()), int(f4.get()), int(f5.get())), int(x))
                    if variable.get() == 'Inverted Pyramid':
                         client.set_blocks(upyramid(int(f0.get()), int(f1.get()), int(f2.get()), int(f4.get()), int(f5.get())), int(x))
                    if variable.get() == 'Sphere':
                        client.set_blocks(sphere(int(f0.get()), int(f2.get()), int(f4.get()), int(f6.get())), int(x))
                    if variable.get() == 'Circle X':
                        client.set_blocks(circle_x(int(f0.get()), int(f2.get()), int(f4.get()), int(f6.get())), int(x))
                    if variable.get() == 'Circle Y':
                        client.set_blocks(circle_y(int(f0.get()), int(f2.get()), int(f4.get()), int(f6.get())), int(x))
                    if variable.get() == 'Circle Z':
                        client.set_blocks(circle_z(int(f0.get()), int(f2.get()), int(f4.get()), int(f6.get())), int(x))
                    if variable.get() == 'Cuboid Filled':
                        client.set_blocks(cuboid(int(f0.get()), int(f1.get()), int(f2.get()), int(f3.get()), int(f4.get()), int(f5.get())), int(x))
                    if variable.get() == 'Cuboid Empty':
                         client.set_blocks(cuboid1(int(f0.get()), int(f1.get()), int(f2.get()), int(f3.get()), int(f4.get()), int(f5.get())), int(x))
                    if variable.get() == 'Cylinder X':
                        client.set_blocks(cylinder_x(int(f0.get()), int(f1.get()), int(f2.get()), int(f4.get()), int(f6.get())), int(x))
                    if variable.get() == 'Cylinder Y':
                        client.set_blocks(cylinder_y(int(f0.get()), int(f2.get()), int(f3.get()), int(f4.get()), int(f6.get())), int(x))
                    if variable.get() == 'Cylinder Z':
                        client.set_blocks(cylinder_z(int(f0.get()), int(f2.get()), int(f4.get()), int(f5.get()), int(f6.get())), int(x))
                    if variable.get() == 'Cone Y':
                        client.set_blocks(cone_y(int(f0.get()), int(f2.get()), int(f3.get()), int(f4.get()), int(f6.get())), int(x))

                variable  = StringVar()
                variable.set('Pyramid')
                variable1 = StringVar()
                variable1.set('EMPTY')

                f = OptionMenu(None, variable, 'Sphere', 'Circle X', 'Circle Y', 'Circle Z', 'Pyramid', 'Inverted Pyramid', 'Cuboid Filled', 'Cuboid Empty', 'Cylinder X', 'Cylinder Y', 'Cylinder Z', 'Circle X', 'Circle Y', 'Circle Z', 'Cone Y')
                fb = Label(None, text='Center/Start Pos X')
                f0 = Spinbox(from_=-40000, to=40000)
                fb1 = Label(None, text='End Pos X')
                f1 = Spinbox(from_=-40000, to=40000)
                fb2 = Label(None, text='Center/Start Pos Y')
                f2 = Spinbox(from_=0, to=255)
                fb3 = Label(None, text='End Pos Y')
                f3 = Spinbox(from_=0, to=255)
                fb4 = Label(None, text='Center/Start Pos Z')
                f4 = Spinbox(from_=-40000, to=40000)
                fb5 = Label(None, text='End Pos Z')
                f5 = Spinbox(from_=-40000, to=40000)
                fb6 = Label(None, text='Radius')
                f6 = Spinbox(from_=0, to=100)
                fb7 = Label(None, text='Block Type')
                f7 = OptionMenu(None, variable1, 'EMPTY', 'GRASS', 'SAND', 'STONE', 'BRICK', 'WOOD', 'CEMENT', 'DIRT', 'PLANK', 'SNOW', 'GLASS', 'COBBLE', 'LIGHT', 'DARK', 'CHEST', 'LEAVES', 'CLOUD', 'TALL GRASS' 'YELLOW FLOWER', 'RED FLOWER', 'PURPLE FLOWER', 'SUN FLOWER', 'WHITE FLOWER', 'BLUE FLOWER')
                
                f.pack()
                fb.pack(anchor=N)
                f0.pack(anchor=N)
                fb1.pack(anchor=N)
                f1.pack(anchor=N)
                fb2.pack(anchor=N)
                f2.pack(anchor=N)
                fb3.pack(anchor=N)
                f3.pack(anchor=N)
                fb4.pack(anchor=N)
                f4.pack(anchor=N)
                fb5.pack(anchor=N)
                f5.pack(anchor=N)
                fb6.pack(anchor=N)
                f6.pack(anchor=N)
                fb7.pack(anchor=N)
                f7.pack(anchor=N)
                client = Client()
                b = Button(None, text='BUILD', fg='red', command=cmd)
                b.pack(fill=None, expand=0, anchor=N)
                
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
probuild = ProBuild(master=root)
root.wm_attributes("-topmost", 1)
probuild.master.title("ProBuilder for Craft")
probuild.master.maxsize(180, 400)
probuild.mainloop()
