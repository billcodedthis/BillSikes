import math
import tkinter as tk
from tkinter import *
from tkinter import constants
from tkinter.ttk import Entry
from sys import argv
from tkinter import messagebox
from typing import Literal
from PIL import Image,ImageTk
from tkinter import ttk

class Example(Frame): 
 
    def __init__(self):
        super().__init__()
        self.circle_calculator_active = False
        self.square_root_active = False
        self.circumference_active=False
        self.area_rectangle_active=False 
        self.area_square_active=False  
        self.area_triangle_active=False
        self.area_rhombus_active=False
        self.area_kite_active=False
        self.area_parallelogram_active=False
        self.area_trapezium_active=False
        self.theorem_active=False
        self.calc_active=False
        
        self.initUI()


    def initUI(self):

        self.master.title("BillSikes")

        self.canvas = tk.Canvas(self.master, width = 600, height = 600,  relief = 'raised')
        self.canvas.pack(expand=YES)
        
        filename = PhotoImage(master= self.canvas,file ="C:/BillSikes/images/144565.png")
        self.canvas.create_image(300,300,image=filename)

        menubar = Menu(self.master)
        self.master.config(menu=menubar)

        fileMenu = Menu(menubar,tearoff=0)
        fileMenu0 =Menu(menubar,tearoff=0)
        fileMenu1 =Menu(menubar,tearoff=0)
        fileMenu2 =Menu(menubar,tearoff=0)
        fileMenu3 =Menu(menubar,tearoff=0)
        fileMenu4 =Menu(menubar,tearoff=0)
        fileMenu5 =Menu(menubar,tearoff=0)
        fileMenu6 =Menu(menubar,tearoff=0)
        fileMenu7 =Menu(menubar,tearoff=0)
        fileMenu8 =Menu(menubar,tearoff=0)
        
        submenu0=Menu(fileMenu0,tearoff=0)
        submenu0.add_command(label="circle",command=self.toggle_circle_calculation)
        submenu0.add_command(label="rectangle",command=self.toggle_area_rectangle)
        submenu0.add_command(label="square",command=self.toggle_area_square)
        submenu0.add_command(label="triangle",command=self.toggle_area_triangle)
        submenu0.add_command(label="rhombus",command=self.toggle_area_rhombus)
        submenu0.add_command(label="parallelogram",command=self.toggle_area_parallelogram)
        submenu0.add_command(label="kite",command=self.toggle_area_kite)
        submenu0.add_command(label="trapezium",command=self.toggle_area_trapezium)
        fileMenu0.add_cascade(label="Area",menu=submenu0)

        submenu1=Menu(fileMenu0,tearoff=0)
        submenu1.add_command(label="rectangle")
        submenu1.add_command(label="square")
        submenu1.add_command(label="triangle")
        fileMenu0.add_cascade(label="Perimeter",menu=submenu1)

        submenu2=Menu(fileMenu0,tearoff=0)
        submenu2.add_command(label="Prism")
        submenu2.add_command(label="Cone")
        submenu2.add_command(label="Cylinder")
        submenu2.add_command(label="Pyramid")
        submenu2.add_command(label="Cuboid")
        submenu2.add_command(label="Sphere")
        fileMenu0.add_cascade(label="Surface Area",menu=submenu2)

        submenu3=Menu(fileMenu0,tearoff=0)
        submenu3.add_command(label="Prism")
        submenu3.add_command(label="Cone")
        submenu3.add_command(label="Cylinder")
        submenu3.add_command(label="Pyramid")
        submenu3.add_command(label="Cuboid")
        submenu3.add_command(label="Sphere")
        fileMenu0.add_cascade(label="Volume",menu=submenu3)
        fileMenu0.add_separator()
        fileMenu0.add_cascade(label="Pythagorean theorem",command=self.toggle_theorem)
        fileMenu0.add_cascade(label="Circumference of a circle",command=self.toggle_circumference)
        fileMenu0.add_cascade(label="Polygons")

        fileMenu1.add_cascade(label="Simple Interest")
        fileMenu1.add_cascade(label="Discount")
        fileMenu1.add_cascade(label="Commisssion")
        fileMenu1.add_cascade(label="Depreciation")
        fileMenu1.add_cascade(label="VAT")
        fileMenu1.add_cascade(label="NHIL")
        fileMenu1.add_cascade(label="Insurance")

        submenu0=Menu(fileMenu2,tearoff=0)
        submenu0.add_command(label="Direct")
        submenu0.add_command(label="Inverse")
        fileMenu2.add_cascade(label="Proportion",menu=submenu0)
        fileMenu2.add_separator()
        fileMenu2.add_cascade(label="Ratio")
        fileMenu2.add_cascade(label="Proportional Division")
        fileMenu2.add_cascade(label="Financial Partnership")

        fileMenu3.add_cascade(label="Rotation")
        fileMenu3.add_cascade(label="Reflection")
        fileMenu3.add_cascade(label="Translation")
        fileMenu3.add_cascade(label="Enlargement")

        fileMenu8.add_cascade(label="square root",command=self.toggle_square_root)

        fileMenu.add_cascade(label="Calculator",command=self.toggle_calc)

        menubar.add_cascade(label="Figures(Shapes)", menu=fileMenu0)
        menubar.add_cascade(label="Percentages", menu=fileMenu1)
        menubar.add_cascade(label="Ratio & proportion", menu=fileMenu2)
        menubar.add_cascade(label="Rigid motion", menu=fileMenu3)
        menubar.add_cascade(label="Probability", menu=fileMenu4)
        menubar.add_cascade(label="Conversions", menu=fileMenu5)
        menubar.add_cascade(label="Rates", menu=fileMenu6)
        menubar.add_cascade(label="Bearings and vectors", menu=fileMenu7)
        menubar.add_cascade(label="Others", menu=fileMenu8)
        menubar.add_cascade(label="Tools", menu=fileMenu)

        self.master.iconbitmap('c:/BillSikes/yh1.ico')
        self.master.mainloop()

    
    
    def toggle_circle_calculation(self):   
        self.circle_calculator_active = not self.circle_calculator_active

        self.master.title("BillSikes/area of circle")
        def comboclick(event):
            if myCombo.get()=='Area':
                label.after(1000, label.destroy())
                label3 = tk.Label(self.master,bg='grey', text='Radius:')
                label3.config(font=('helvetica', 12))
                canvas1.create_window(100, 400, window=label3)
                label4 = tk.Label(self.master,bg='grey', text='Diameter:')
                label4.config(font=('helvetica', 12))
                canvas1.create_window(95, 430, window=label4)
                entry2 = tk.Entry (self.master) 
                canvas1.create_window(200, 400, window=entry2)
                entry3 = tk.Entry (self.master) 
                canvas1.create_window(200, 430, window=entry3)
                def Area ():
                    x2=entry2.get()
                    x3=entry3.get()
                    if len(entry3.get())!=0:
                        x2=str(float(x3)//2)
                    else:
                        x2=entry2.get()
                    label5 = tk.Label(self.master,bg='grey', text= 'The Area of the circle is:',font=('helvetica', 10))
                    canvas1.create_window(300, 480, window=label5)
                    label6 = tk.Label(self.master,bg='grey', text= str(22/7 * float(x2)**2)+str('cm²'),font=('helvetica', 10, 'bold'))
                    canvas1.create_window(300, 500, window=label6)
                    def reset ():
                        label5.destroy()
                        label6.destroy()
                        button1.destroy()
                        button2.destroy()
                        label3.destroy()
                        label4.destroy()
                        entry2.destroy()
                        entry3.destroy()
                    button = tk.Button(self.master,text="Reset",command=reset,bg='blue',fg='white', font=('helvetica', 9, 'bold'))
                    canvas1.create_window(25,560,window=button)
                    def ok():
                        label5.destroy()
                        label6.destroy()
                    button2 = tk.Button(self.master,text="ok",command=ok,bg='blue',fg='white', font=('helvetica', 9, 'bold'))
                    canvas1.create_window(300,530,window=button2)
                
                button1 = tk.Button(self.master,text='Get the Area', command=Area, bg='yellow', fg='black', font=('helvetica', 9, 'bold'))
                canvas1.create_window(300, 455, window=button1)
                
            elif myCombo.get()=='Radius':
                label2 = tk.Label(self.master,bg='grey', text='Area:')
                label2.config(font=('helvetica', 12))
                canvas1.create_window(100, 400, window=label2)
                label4 = tk.Label(self.master,bg='grey', text='Diameter:')
                label4.config(font=('helvetica', 12))
                canvas1.create_window(95, 430, window=label4)
                entry1 = tk.Entry (self.master) 
                canvas1.create_window(200, 400, window=entry1)
                entry3 = tk.Entry (self.master) 
                canvas1.create_window(200, 430, window=entry3)
                def Radius ():
                    x1=entry1.get()
                    x3=entry3.get()
                    label5 = tk.Label(self.master,bg='grey', text= 'The Radius of the circle is:',font=('helvetica', 10))
                    canvas1.create_window(300, 480, window=label5)
                    if len(entry3.get())==0:
                        label6 = tk.Label(self.master,bg='grey', text=str(math.sqrt(float(x1)//3.14))+str('cm'),font=('helvetica', 10, 'bold'))
                        canvas1.create_window(300, 500, window=label6)
                    else:
                        label6 = tk.Label(self.master,bg='grey', text=str(float(x3)/2)+str('cm'),font=('helvetica', 10, 'bold'))
                        canvas1.create_window(300, 500, window=label6)
                    def reset ():
                        label5.destroy()
                        label6.destroy()
                        button2.destroy()
                        button1.destroy()
                        label2.destroy()
                        label4.destroy()
                        entry1.destroy()
                        entry3.destroy()
                    button = tk.Button(self.master,text="Reset",command=reset,bg='blue',fg='white', font=('helvetica', 9, 'bold'))
                    canvas1.create_window(25,560,window=button)
                    def ok():
                        label5.destroy()
                        label6.destroy()
                    button1 = tk.Button(self.master,text="ok",command=ok,bg='blue',fg='white', font=('helvetica', 9, 'bold'))
                    canvas1.create_window(300,530,window=button1)
                
                button2 = tk.Button(self.master,text='Get the Radius', command=Radius, bg='blue', fg='white', font=('helvetica', 9, 'bold'))
                canvas1.create_window(300, 455, window=button2)
            elif myCombo.get()=='Diameter':
                label2 = tk.Label(self.master,bg='grey', text='Area:')
                label2.config(font=('helvetica', 12))
                canvas1.create_window(100, 400, window=label2)
                label3 = tk.Label(self.master,bg='grey', text='Radius:')
                label3.config(font=('helvetica', 12))
                canvas1.create_window(95, 430, window=label3)
                entry1 = tk.Entry (self.master) 
                canvas1.create_window(200, 400, window=entry1)
                entry2 = tk.Entry (self.master) 
                canvas1.create_window(200, 430, window=entry2)
                def Diameter ():
                    x1=entry1.get()
                    x2=entry2.get()
                    label5 = tk.Label(self.master,bg='grey', text= 'The Diameter of the circle is:',font=('helvetica', 10))
                    canvas1.create_window(300, 480, window=label5)
                    if len(entry2.get())==0:
                        d=math.sqrt(float(x1)//3.14)
                    else:
                        d=float(x2)
                    label6 = tk.Label(self.master,bg='grey', text=str(d*2)+str('cm'),font=('helvetica', 10, 'bold'))
                    canvas1.create_window(300, 500, window=label6)
                    def reset ():
                        label5.destroy()
                        label6.destroy()
                        button3.destroy()
                        button1.destroy()
                        label2.destroy()
                        label3.destroy()
                        entry1.destroy()
                        entry2.destroy()
                    button = tk.Button(self.master,text="Reset",command=reset,bg='blue',fg='white', font=('helvetica', 9, 'bold'))
                    canvas1.create_window(25,560,window=button)
                    def ok():
                        label5.destroy()
                        label6.destroy()
                    button1 = tk.Button(self.master,text="ok",command=ok,bg='blue',fg='white', font=('helvetica', 9, 'bold'))
                    canvas1.create_window(300,530,window=button1)
                
                button3 = tk.Button(self.master,text='Get the Diameter', command=Diameter, bg='green', fg='white', font=('helvetica', 9, 'bold'))
                canvas1.create_window(300, 455, window=button3)

        self.canvas.delete("all")
        canvas1 = self.canvas
        canvas1.config(width = 600, height = 600)

        option =[
            "Choose desired value needed",
            "Area",
            "Radius",
            "Diameter"
        ]

        myCombo =ttk.Combobox(master=canvas1,value=option)
        myCombo.config(width=26)
        myCombo.current(0)
        myCombo.bind("<<ComboboxSelected>>",comboclick)
        canvas1.create_window(300,350,window=myCombo)

        filename = PhotoImage(master= canvas1,file ="C:/BillSikes/images/144565.png")
        canvas1.create_image(300,300,image=filename)

        filename1 = PhotoImage(master = canvas1,file="C:/BillSikes/images/circle.png")
        canvas1.create_image(300, 185,image=filename1)

        label = tk.Label(self.master,bg='grey', text='~Input the known values and select from the list of options the required value needed')
        label.config(font=('helvetica', 16))
        canvas1.create_window(300, 590, window=label)
        label1 = tk.Label(self.master,bg='grey', text='Calculate the Area of a Circle')
        label1.config(font=('helvetica', 12))
        canvas1.create_window(300, 25, window=label1)
        self.master.mainloop()

    def toggle_calc(self):
        self.calc_active = not self.calc_active 
        self.master.title("BillSikes/square root") 
        
    
        root = Tk()
        root.title("Calculator")
        root.iconbitmap('c:/BillSikes/yh2.ico')
        root.geometry("312x324")  # this is for the size of the window 
        root.resizable(0, 0)
        def btn_click(item):
            global expression
            expression = expression + str(item)
            input_text.set(expression)

        # 'bt_clear' function :This is used to clear 
        # the input field

        def bt_clear(): 
            global expression 
            expression = "" 
            input_text.set("")
        
        # 'bt_equal':This method calculates the expression 
        # present in input field
        
        def bt_equal():
            global expression
            result = str(eval(expression)) # 'eval':This function is used to evaluates the string expression directly
            input_text.set(result)
            expression = ""
        
        expression = ""
        
        # 'StringVar()' :It is used to get the instance of input field
        
        input_text = StringVar()
        
        # Let us creating a frame for the input field
        
        input_frame = Frame(root, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
        
        input_frame.pack(side=TOP)
        
        #Let us create a input field inside the 'Frame'
        
        input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0, justify=RIGHT)
        
        input_field.grid(row=0, column=0)
        
        input_field.pack(ipady=10) # 'ipady' is internal padding to increase the height of input field
        
        #Let us creating another 'Frame' for the button below the 'input_frame'
        
        btns_frame = Frame(root, width=312, height=272.5, bg="grey")
        
        btns_frame.pack()
        
        # first row
        
        clear = Button(btns_frame, text = "C", fg = "black", width = 32, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: bt_clear()).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)
        
        divide = Button(btns_frame, text = "/", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("/")).grid(row = 0, column = 3, padx = 1, pady = 1)
        
        # second row
        
        seven = Button(btns_frame, text = "7", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(7)).grid(row = 1, column = 0, padx = 1, pady = 1)
        
        eight = Button(btns_frame, text = "8", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
        
        nine = Button(btns_frame, text = "9", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(9)).grid(row = 1, column = 2, padx = 1, pady = 1)
        
        multiply = Button(btns_frame, text = "*", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("*")).grid(row = 1, column = 3, padx = 1, pady = 1)
        
        # third row
        
        four = Button(btns_frame, text = "4", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
        
        five = Button(btns_frame, text = "5", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
        
        six = Button(btns_frame, text = "6", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
        
        minus = Button(btns_frame, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("-")).grid(row = 2, column = 3, padx = 1, pady = 1)
        
        # fourth row
        
        one = Button(btns_frame, text = "1", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
        
        two = Button(btns_frame, text = "2", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
        
        three = Button(btns_frame, text = "3", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(3)).grid(row = 3, column = 2, padx = 1, pady = 1)
        
        plus = Button(btns_frame, text = "+", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("+")).grid(row = 3, column = 3, padx = 1, pady = 1)
        
        # fourth row
        
        zero = Button(btns_frame, text = "0", fg = "black", width = 21, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(0)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
        
        point = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click(".")).grid(row = 4, column = 2, padx = 1, pady = 1)
        
        equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: bt_equal()).grid(row = 4, column = 3, padx = 1, pady = 1)
        
        root.mainloop()
    def toggle_square_root(self):
        self.square_root_active = not self.square_root_active
        
        self.master.title("BillSikes/square root") 
        self.canvas.delete("all")
        canvas1 = self.canvas
        canvas1.config(width = 400, height = 300)
        filename = PhotoImage(master= canvas1,file ="C:/BillSikes/images/144565.png")
        canvas1.create_image(200,150,image=filename)
        label = tk.Label(self.master, bg='grey',text='~Input the known values and select from the list of options the required value needed')
        label.config(font=('helvetica', 16))
        canvas1.create_window(300, 490, window=label)
        label1 = tk.Label(self.master, text='Calculate the Square root',bg='grey')
        label1.config(font=('helvetica', 12))
        canvas1.create_window(200, 25, window=label1)
        label2 = tk.Label(self.master, text='Type your Number:',bg='grey')
        label2.config(font=('helvetica', 10))
        canvas1.create_window(200, 100, window=label2)
        entry1 = tk.Entry (self.master) 
        canvas1.create_window(200, 140, window=entry1)

        def getSquareroot ():
            x1 = entry1.get()

            label3 = tk.Label(self.master,bg='grey', text= 'The Square root of ' + x1 + ' is:',font=('helvetica', 10))
            canvas1.create_window(200, 210, window=label3)

            label4 = tk.Label(self.master,bg='grey', text= float(x1)**0.5,font=('helvetica', 10, 'bold'))
            canvas1.create_window(200, 230, window=label4)
            def ok ():
                label3.destroy()
                label4.destroy()
            button2 = tk.Button(self.master,text="Reset",command=ok,bg='blue',fg='white', font=('helvetica', 9, 'bold'))
            canvas1.create_window(200,270,window=button2)
        
        button1 = tk.Button(self.master,text='Get the Square root', command=getSquareroot, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
        canvas1.create_window(200, 180, window=button1)
        self.master.mainloop()
        
    def toggle_circumference(self):
        self.circumference_active= not self.circumference_active
         
         
        self.master.title("BillSikes/circumference of circle")
        def comboclick(event):
            #myLabel = Label(self.master,text=myCombo.get()).pack()
            if myCombo.get()=='Circumference':
                label3 = tk.Label(self.master,bg='grey', text='Radius:')
                label3.config(font=('helvetica', 12))
                canvas1.create_window(100, 400, window=label3)
                label4 = tk.Label(self.master,bg='grey', text='Diameter:')
                label4.config(font=('helvetica', 12))
                canvas1.create_window(95, 430, window=label4)
                entry2 = tk.Entry (self.master) 
                canvas1.create_window(200, 400, window=entry2)
                entry3 = tk.Entry (self.master) 
                canvas1.create_window(200, 430, window=entry3)
                def Circumference ():
                    x2=entry2.get()
                    x3=entry3.get()
                    if len(entry3.get())!=0:
                        x2=str(float(x3)//2)
                    else:
                        x2=entry2.get()
                    label5 = tk.Label(self.master,bg='grey', text= 'The Circumference of the circle is:',font=('helvetica', 10))
                    canvas1.create_window(300, 480, window=label5)
                    label6 = tk.Label(self.master,bg='grey', text=str( 2*(22/7)*float(x2))+str('cm'),font=('helvetica', 10, 'bold'))
                    canvas1.create_window(300, 500, window=label6)
                    def reset ():
                        label5.destroy()
                        label6.destroy()
                        button1.destroy()
                        button2.destroy()
                        label3.destroy()
                        label4.destroy()
                        entry2.destroy()
                        entry3.destroy()
                    button = tk.Button(self.master,text="Reset",command=reset,bg='blue',fg='white', font=('helvetica', 9, 'bold'))
                    canvas1.create_window(25,560,window=button)
                    def ok ():
                        label5.destroy()
                        label6.destroy()
                    button2 = tk.Button(self.master,text="ok",command=ok,bg='blue',fg='white', font=('helvetica', 9, 'bold'))
                    canvas1.create_window(300,530,window=button2)
                def buttom():
                    canvas1.destroy()
                    self.master.title("BillSikes")
                buttom1 = tk.Button(self.master,text='Done', command=buttom, bg='violet', fg='black', font=('helvetica', 9, 'bold'))
                canvas1.create_window(580, 560, window=buttom1)
                button1 = tk.Button(self.master,text='Get the Circumference', command=Circumference, bg='yellow', fg='black', font=('helvetica', 9, 'bold'))
                canvas1.create_window(300, 455, window=button1)
            
                
            elif myCombo.get()=='Radius':
                label2 = tk.Label(self.master,bg='grey', text='Circumference:')
                label2.config(font=('helvetica', 14))
                canvas1.create_window(68, 400, window=label2)
                label4 = tk.Label(self.master,bg='grey', text='Diameter:')
                label4.config(font=('helvetica', 14))
                canvas1.create_window(95, 430, window=label4)
                entry1 = tk.Entry (self.master) 
                canvas1.create_window(200, 400, window=entry1)
                entry3 = tk.Entry (self.master) 
                canvas1.create_window(200, 430, window=entry3)
                def Radius ():
                    x1=entry1.get()
                    x3=entry3.get()
                    label5 = tk.Label(self.master.master,bg='grey', text= 'The Radius of the circle is:',font=('helvetica', 10))
                    canvas1.create_window(300, 480, window=label5)
                    if len(entry3.get())==0:
                        label6 = tk.Label(self.master.master,bg='grey', text=str(float(x1)//(2*3.14))+str('cm'),font=('helvetica', 10, 'bold'))
                        canvas1.create_window(300, 500, window=label6)
                    else:
                        label6 = tk.Label(self.master.master,bg='grey', text=str(float(x3)/2)+str('cm'),font=('helvetica', 10, 'bold'))
                        canvas1.create_window(300, 500, window=label6)
                    def reset ():
                        label5.destroy()
                        label6.destroy()
                        button2.destroy()
                        button1.destroy()
                        label2.destroy()
                        label4.destroy()
                        entry1.destroy()
                        entry3.destroy()
                    button = tk.Button(self.master,text="Reset",command=reset,bg='blue',fg='white', font=('helvetica', 9, 'bold'))
                    canvas1.create_window(25,560,window=button)
                    def ok():
                        label5.destroy()
                        label6.destroy()
                    button1 = tk.Button(self.master,text="ok",command=ok,bg='blue',fg='white', font=('helvetica', 9, 'bold'))
                    canvas1.create_window(300,530,window=button1)
                def buttom():
                    canvas1.destroy()
                    self.master.title("BillSikes")
                buttom1 = tk.Button(self.master,text='Done', command=buttom, bg='violet', fg='black', font=('helvetica', 9, 'bold'))
                canvas1.create_window(580, 560, window=buttom1)
                button2 = tk.Button(self.master,text='Get the Radius', command=Radius, bg='blue', fg='white', font=('helvetica', 9, 'bold'))
                canvas1.create_window(300, 455, window=button2)

            elif myCombo.get()=='Diameter':
                label2 = tk.Label(self.master,bg='grey', text='Circumference:')
                label2.config(font=('helvetica', 14))
                canvas1.create_window(68, 400, window=label2)
                label3 = tk.Label(self.master,bg='grey', text='Radius:')
                label3.config(font=('helvetica', 14))
                canvas1.create_window(95, 430, window=label3)
                entry1 = tk.Entry (self.master) 
                canvas1.create_window(200, 400, window=entry1)
                entry2 = tk.Entry (self.master) 
                canvas1.create_window(200, 430, window=entry2)
                def Diameter ():
                    x1=entry1.get()
                    x2=entry2.get()
                    label5 = tk.Label(self.master,bg='grey', text= 'The Diameter of the circle is:',font=('helvetica', 10))
                    canvas1.create_window(300, 480, window=label5)
                    if len(entry2.get())==0:
                        d=float(x1)//(2*3.14)
                    else:
                        d=float(x2)
                    label6 = tk.Label(self.master.master,bg='grey', text=str(d*2)+str('cm'),font=('helvetica', 10, 'bold'))
                    canvas1.create_window(300, 500, window=label6)
                    def reset ():
                        label5.destroy()
                        label6.destroy()
                        button3.destroy()
                        button1.destroy()
                        label2.destroy()
                        label3.destroy()
                        entry1.destroy()
                        entry2.destroy()
                    button = tk.Button(self.master,text="Reset",command=reset,bg='blue',fg='white', font=('helvetica', 9, 'bold'))
                    canvas1.create_window(25,560,window=button)
                    def ok():
                        label5.destroy()
                        label6.destroy()
                    button1 = tk.Button(self.master,text="ok",command=ok,bg='blue',fg='white', font=('helvetica', 9, 'bold'))
                    canvas1.create_window(300,530,window=button1)
                def buttom():
                    canvas1.destroy()
                    self.master.title("BillSikes")
                buttom1 = tk.Button(self.master,text='Done', command=buttom, bg='violet', fg='black', font=('helvetica', 9, 'bold'))
                canvas1.create_window(580, 560, window=buttom1)
                button3 = tk.Button(self.master,text='Get the Diameter', command=Diameter, bg='green', fg='white', font=('helvetica', 9, 'bold'))
                canvas1.create_window(300, 455, window=button3)

        self.canvas.delete("all")
        canvas1 = self.canvas
        canvas1.config(width = 600, height = 600)

        option =[
            "Choose desired value needed",
            "Circumference",
            "Radius",
            "Diameter"
        ]

        myCombo =ttk.Combobox(master=canvas1,value=option)
        myCombo.config(width=26)
        myCombo.current(0)
        myCombo.bind("<<ComboboxSelected>>",comboclick)
        canvas1.create_window(300,350,window=myCombo)

        filename = PhotoImage(master= canvas1,file ="C:/BillSikes/images/144565.png")
        canvas1.create_image(300,300,image=filename)

        filename1 = PhotoImage(master = canvas1,file="C:/BillSikes/images/ccircle.png")
        canvas1.create_image(300, 185,image=filename1)

        label = tk.Label(self.master,bg='grey', text='~Input the known values and select from the list of options the required value needed')
        label.config(font=('helvetica', 16))
        canvas1.create_window(300, 590, window=label)
        label1 = tk.Label(self.master,bg='grey', text='Calculate the Circumference of a Circle')
        label1.config(font=('helvetica', 14))
        canvas1.create_window(300, 25, window=label1)
        self.master.mainloop()

    def toggle_area_rectangle(self):
        self.area_rectangle_active = not self.area_rectangle_active
        self.master.title("BillSikes/area of rectangle")
        self.canvas.delete("all")
        canvas1 = self.canvas
        canvas1.config(width = 600, height = 600)
        
        filename = PhotoImage(master= canvas1,file ="C:/BillSikes/images/144565.png")
        canvas1.create_image(300,300,image=filename)
        
        filename1 = PhotoImage(master = canvas1,file="C:/BillSikes/images/rectangle.png")
        canvas1.create_image(300, 185,image=filename1)

        label = tk.Label(self.master,bg='grey', text='~Input the known values and select from the list of options the required value needed')
        label.config(font=('helvetica', 16))
        canvas1.create_window(300, 590, window=label)
        label1 = tk.Label(self.master,bg='grey', text='Calculate the Area of a Rectangle')
        label1.config(font=('helvetica', 12))
        canvas1.create_window(300, 25, window=label1)
        label2 = tk.Label(self.master,bg='grey', text='Area:')
        label2.config(font=('helvetica', 12))
        canvas1.create_window(100, 350, window=label2)
        label3 = tk.Label(self.master,bg='grey', text='Length:')
        label3.config(font=('helvetica', 12))
        canvas1.create_window(300, 350, window=label3)
        label4 = tk.Label(self.master,bg='grey', text='Breadth/Width:')
        label4.config(font=('helvetica', 12))
        canvas1.create_window(500, 350, window=label4)
        entry1 = tk.Entry (self.master) 
        canvas1.create_window(100, 370, window=entry1)
        entry2 = tk.Entry (self.master) 
        canvas1.create_window(300, 370, window=entry2)
        entry3 = tk.Entry (self.master) 
        canvas1.create_window(500, 370, window=entry3)
        def Area():
            x2=entry2.get()
            x3=entry3.get()
            label5 = tk.Label(self.master,bg='grey', text= 'The Area of the rectangle is:',font=('helvetica', 10))
            canvas1.create_window(300, 470, window=label5)
            label6 = tk.Label(self.master,bg='grey', text= str(float(x2)*float(x3))+str('cm²'),font=('helvetica', 10, 'bold'))
            canvas1.create_window(300, 490, window=label6)
            def ok ():
                label5.destroy()
                label6.destroy()
            button = tk.Button(self.master,text="Reset",command=ok,bg='blue',fg='white', font=('helvetica', 9, 'bold'))
            canvas1.create_window(300,520,window=button)
        def Length():
            x1=entry1.get()
            x3=entry3.get()
            label5 = tk.Label(self.master,bg='grey', text= 'The Length of the rectangle is:',font=('helvetica', 10))
            canvas1.create_window(300, 470, window=label5)
            label6 = tk.Label(self.master,bg='grey', text= str(float(x1)/float(x3))+str('cm'),font=('helvetica', 10, 'bold'))
            canvas1.create_window(300, 490, window=label6)
            def ok ():
                label5.destroy()
                label6.destroy()
            button = tk.Button(self.master,text="Reset",command=ok,bg='blue',fg='white', font=('helvetica', 9, 'bold'))
            canvas1.create_window(300,520,window=button)
        def Breadth():
            x1=entry1.get()
            x2=entry2.get()
            label5 = tk.Label(self.master,bg='grey', text= 'The Breadth/Width of the rectangle is:',font=('helvetica', 10))
            canvas1.create_window(300, 470, window=label5)
            label6 = tk.Label(self.master,bg='grey', text= str(float(x1)/float(x2))+str('cm'),font=('helvetica', 10, 'bold'))
            canvas1.create_window(300, 490, window=label6)
            def ok ():
                label5.destroy()
                label6.destroy()
            button = tk.Button(self.master,text="Reset",command=ok,bg='blue',fg='white', font=('helvetica', 9, 'bold'))
            canvas1.create_window(300,520,window=button)
        
        button1 = tk.Button(self.master,text='Get the Area', command=Area, bg='yellow', fg='black', font=('helvetica', 9, 'bold'))
        canvas1.create_window(100, 400, window=button1)
        button2 = tk.Button(self.master,text='Get the Length', command=Length, bg='blue', fg='white', font=('helvetica', 9, 'bold'))
        canvas1.create_window(300, 400, window=button2)
        button3 = tk.Button(self.master,text='Get the Breadth/Width', command=Breadth, bg='green', fg='white', font=('helvetica', 9, 'bold'))
        canvas1.create_window(500, 400, window=button3)
        self.master.mainloop()

    def toggle_area_square(self):
        self.area_square_active = not self.area_square_active

         
        self.master.title("BillSikes/area of square")
        self.canvas.delete("all")
        canvas1 = self.canvas
        canvas1.config(width = 600, height = 600)

        filename = PhotoImage(master= canvas1,file ="C:/BillSikes/images/144565.png")
        canvas1.create_image(300,300,image=filename)
        
        filename1 = PhotoImage(master = canvas1,file="C:/BillSikes/images/square.png")
        canvas1.create_image(300, 185,image=filename1)

        label = tk.Label(self.master,bg='grey', text='~Input the known values and select from the options given,the required value needed')
        label.config(font=('helvetica', 16))
        canvas1.create_window(300, 590, window=label)
        label1 = tk.Label(self.master,bg='grey', text='Calculate the Area of a Square')
        label1.config(font=('helvetica', 12))
        canvas1.create_window(300, 25, window=label1)
        label2 = tk.Label(self.master,bg='grey', text='Area:')
        label2.config(font=('helvetica', 12))
        canvas1.create_window(100, 350, window=label2)
        label3 = tk.Label(self.master,bg='grey', text='Side/Length:')
        label3.config(font=('helvetica', 12))
        canvas1.create_window(500, 350, window=label3)
        entry1 = tk.Entry (self.master) 
        canvas1.create_window(100, 370, window=entry1)
        entry2 = tk.Entry (self.master) 
        canvas1.create_window(500, 370, window=entry2)
        def Area():
            x2=entry2.get()
            label5 = tk.Label(self.master,bg='grey', text= 'The Area of the square is:',font=('helvetica', 10))
            canvas1.create_window(300, 470, window=label5)
            label6 = tk.Label(self.master,bg='grey', text= str(float(x2)**2)+str('cm²'),font=('helvetica', 10, 'bold'))
            canvas1.create_window(300, 490, window=label6)
            def ok ():
                label5.destroy()
                label6.destroy()
            button = tk.Button(self.master,text="Reset",command=ok,bg='blue',fg='black', font=('helvetica', 9, 'bold'))
            canvas1.create_window(300,520,window=button)
        def Side():
            x1=entry1.get()
            label5 = tk.Label(self.master,bg='grey', text= 'The Area of the square is:',font=('helvetica', 10))
            canvas1.create_window(300, 470, window=label5)
            label6 = tk.Label(self.master,bg='grey', text= str(math.sqrt(float(x1)))+str('cm'),font=('helvetica', 10, 'bold'))
            canvas1.create_window(300, 490, window=label6)
            def ok ():
                label5.destroy()
                label6.destroy()
            button = tk.Button(self.master,text="Reset",command=ok,bg='blue',fg='white', font=('helvetica', 9, 'bold'))
            canvas1.create_window(300,520,window=button)
        
        button1 = tk.Button(self.master,text='Get the Area', command=Area, bg='blue', fg='white', font=('helvetica', 9, 'bold'))
        canvas1.create_window(100, 400, window=button1)
        button2 = tk.Button(self.master,text='Get the Side', command=Side, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
        canvas1.create_window(500, 400, window=button2)
        self.master.mainloop()
    
    def toggle_area_triangle(self):
        self.toggle_area_triangle_active = not self.toggle_area_triangle_active
        self.master.mainloop()
    
    def toggle_area_rhombus(self):
        self.toggle_area_rhombus_active = not self.toggle_area_rhombus_active
        self.master.mainloop()
    
    def toggle_area_kite(self):
        self.toggle_area_kite_active = not self.toggle_area_kite_active
        self.master.mainloop()

    def toggle_area_parallelogram(self):
        self.toggle_area_parallelogram_active = not self.toggle_area_parallelogram_active
        self.master.mainloop()
    
    def toggle_area_trapezium(self):   
        self.toggle_area_trapezium_active = not self.toggle_area_trapezium_active
        self.master.mainloop()

    def toggle_theorem(self):
        self.theorem_active = not self.theorem_active
         
         
        self.master.title("BillSikes/Pythagorean theorem")
        self.canvas.delete("all")
        canvas1 = self.canvas
        canvas1.config(width = 600, height = 600)

        filename = PhotoImage(master= canvas1,file ="C:/BillSikes/images/144565.png")
        canvas1.create_image(300,280,image=filename)
        
        filename1 = PhotoImage(master = canvas1,file="C:/BillSikes/images/theorem.png")
        canvas1.create_image(300, 185,image=filename1)

        label = tk.Label(self.master,bg='grey', text='~Input the known values and select from the options given,the required value needed')
        label.config(font=('helvetica', 16))
        canvas1.create_window(300, 590, window=label)
        label1 = tk.Label(self.master,bg='grey', text='Calculate using Pythagorean theorem')
        label1.config(font=('helvetica', 12))
        canvas1.create_window(300, 25, window=label1)
        label2 = tk.Label(self.master,bg='grey', text='length of c:')
        label2.config(font=('helvetica', 12))
        canvas1.create_window(100, 350, window=label2)
        label3 = tk.Label(self.master,bg='grey', text='length of a:')
        label3.config(font=('helvetica', 12))
        canvas1.create_window(300, 350, window=label3)
        label4 = tk.Label(self.master,bg='grey', text='length of b:')
        label4.config(font=('helvetica', 12))
        canvas1.create_window(500, 350, window=label4)
        entry1 = tk.Entry (self.master) 
        canvas1.create_window(100, 370, window=entry1)
        entry2 = tk.Entry (self.master) 
        canvas1.create_window(300, 370, window=entry2)
        entry3 = tk.Entry (self.master) 
        canvas1.create_window(500, 370, window=entry3)
        def c():
            x1=entry2.get()
            x2=entry3.get()
            label5 = tk.Label(self.master, bg='grey',text= 'The length of c is:',font=('helvetica', 10))
            canvas1.create_window(300, 470, window=label5)
            label6 = tk.Label(self.master,bg='grey', text= str(math.sqrt(float(x1)**2+float(x2)**2))+str('cm'),font=('helvetica', 10, 'bold'))
            canvas1.create_window(300, 490, window=label6)
            def ok ():
                label5.destroy()
                label6.destroy()
            button = tk.Button(self.master,text="Reset",command=ok,bg='blue',fg='black', font=('helvetica', 9, 'bold'))
            canvas1.create_window(300,520,window=button)
        def a():
            x1=entry1.get()
            x2=entry3.get()
            label5 = tk.Label(self.master,bg='grey', text= 'The length of a is:',font=('helvetica', 10))
            canvas1.create_window(300, 470, window=label5)
            label6 = tk.Label(self.master,bg='grey', text= str(math.sqrt(float(x1)**2-float(x2)**2))+str('cm'),font=('helvetica', 10, 'bold'))
            canvas1.create_window(300, 490, window=label6)
            def ok ():
                label5.destroy()
                label6.destroy()
            button = tk.Button(self.master,text="Reset",command=ok,bg='blue',fg='black', font=('helvetica', 9, 'bold'))
            canvas1.create_window(300,520,window=button)
        def b():
            x1=entry1.get()
            x2=entry2.get()
            label5 = tk.Label(self.master,bg='grey', text= 'The length of b is:',font=('helvetica', 10))
            canvas1.create_window(300, 470, window=label5)
            label6 = tk.Label(self.master,bg='grey', text= str(math.sqrt(float(x1)**2-float(x2)**2))+str('cm'),font=('helvetica', 10, 'bold'))
            canvas1.create_window(300, 490, window=label6)
            def ok ():
                label5.destroy()
                label6.destroy()
            button = tk.Button(self.master,text="Reset",command=ok,bg='blue',fg='white', font=('helvetica', 9, 'bold'))
            canvas1.create_window(300,520,window=button)
        
        button1 = tk.Button(self.master,text='Get length of c', command=c, bg='blue', fg='white', font=('helvetica', 9, 'bold'))
        canvas1.create_window(100, 400, window=button1)
        button3 = tk.Button(self.master,text='Get length of a', command=a, bg='orange', fg='white', font=('helvetica', 9, 'bold'))
        canvas1.create_window(300, 400, window=button3)
        button2 = tk.Button(self.master,text='Get length of b', command=b, bg='green', fg='white', font=('helvetica', 9, 'bold'))
        canvas1.create_window(500, 400, window=button2)
        self.master.mainloop()
    def onExit(self):
        self.quit()
    
    
    
def main():

    root = Tk()
    root.geometry("1100x600")
    filename1 = PhotoImage(master= root,file ="C:/BillSikes/images/144565.png")
    background_label = Label(root, image=filename1)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()