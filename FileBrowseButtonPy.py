#1
from tkinter import *
from tkinter import filedialog

base = Tk()

# Create a canvas - δουλεύουμε με canvas
base.geometry('150x150')

# Function for opening the file
def file_opener():
   input = filedialog.askopenfile(initialdir="/")
   print(input)
   for i in input:
      print(i)

# Button label
x = Button(base, text ='Browse .txt/.csv files', command = lambda:file_opener(), bg='red')  #bg - βάζω χρώμα στο κουμπί
x.pack()
mainloop()

#2
from tkinter import *
from tkinter import ttk
from tkinter import filedialog



class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Python Tkinter Dialog Widget")
        self.minsize(640, 400)
        

        self.labelFrame = ttk.LabelFrame(self, text = "Open File")
        self.labelFrame.grid(column = 0, row = 1, padx = 20, pady = 20)

        self.button()



    def button(self):
        self.button = ttk.Button(self.labelFrame, text = "Browse",command = self.fileDialog)
        self.button.grid(column = 1, row = 1)


    def fileDialog(self):

        self.filename = filedialog.askopenfilename(initialdir =  "/", title = "Select A File", filetype = (("jpeg files","*.jpg"),("all files","*.*")) )
        
        self.label = ttk.Label(self.labelFrame, text = "")
        self.label.grid(column = 1, row = 2)
        self.label.configure(text = self.filename)

root = Root()
root.mainloop()




