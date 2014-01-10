import socket
from builder import *
from Tkinter import *

class ProBuild(Frame):
    def createWidgets(self):
        
                variable  = StringVar()
                variable.set('pyramid')

                f = OptionsMenu(None, variable, 'pyramid', 'inverted pyramid') ##TODO: Add functions
                e1 = Entry()
                e2 = Entry()
                e3 = Entry()
                e4 = Entry()
                e5 = Entry()
                e6 = Entry()  ##TODO: Make this a scrollable options widget.
                e1.insert(0, 'Start pos X')
                e2.insert(0, 'End pos X')
                e3.insert(0, 'Start pos y')
                e4.insert(0, 'Start pos Z')
                e5.insert(0, 'End pos Z')
                e6.insert(0, 'Block Type#')
                f.pack()
                e1.pack()
                e2.pack()
                e3.pack()
                e4.pack()
                e5.pack()
                e6.pack()
                client = Client()
                def cmd():
                    client.__init__()
                    if variable.get() == 'pyramid':
                        client.set_blocks(pyramid(int(e1.get()), int(e2.get()), int(e3.get()), int(e4.get()), int(e5.get())), int(e6.get()))
                    if variable.get() == 'inverted pyramid':
                         client.set_blocks(upyramid(int(e1.get()), int(e2.get()), int(e3.get()), int(e4.get()), int(e5.get())), int(e6.get()))
                        
                b = Button(None, text='BUILD', fg='blue', command=cmd)
                b.pack(fill=None, expand=0)
                
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
