import tkinter as tk
from tkinter import ttk
import re 
import requests
import json 
import tkcalendar as tcal
import inst_326_project_2

#12/4/20 update 

LARGE_FONT = ("Times")


class user_information:
    def __init__(self):
        self.user_first = ""
        self.user_last =  ""
        self.user_address = "" 
        self.user_item = ""
        self.delivery_date = ""

class Main(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.default = user_information()
        
        tk.Tk.wm_title(self, "Shopping App")
        
        container = tk.Frame(self)
        
        container.pack(side="top", fill="both", expand = True)
        
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        
        for F in (StartPage, PageOne, PageTwo, PageThree, PageFour, PageFive, PageSix):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame(StartPage)
        
    def show_frame(self, cont):
        
        frame = self.frames[cont]
        frame.tkraise()
        
class StartPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Welcome to our app!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        button1 = ttk.Button(self, text="Next",
                            command=lambda: controller.show_frame(PageOne))
        button1.pack()
        
        button2 = ttk.Button(self, text="Quit", command=quit)
        button2.pack()

class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        title = tk.Label(self, text="Dropoff Location?", font=LARGE_FONT)
        title.pack(pady=10,padx=10)
        
        label1 = tk.Label(self, text="Address:")
        label1.pack()
        entry1 = tk.Entry(self)
        entry1.pack()
        
        #save address to user information class
        
        submit = ttk.Button(self, text="Next", command=lambda: controller.show_frame(PageTwo))
        submit.pack()
        
        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()
        
        button2 = ttk.Button(self, text="Quit", command=quit)
        button2.pack()
        
        
class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
                
        title = tk.Label(self, text="What type of place are you trying to buy from?", font=LARGE_FONT)
        title.pack(pady=10,padx=10)
        #title.grid(row=0, column=2, columnspan=3)
        
        label1 = tk.Label(self, text="Search:")
        label1.pack()
        #label1.grid(row=1,column=2, columnspan=1)
        entry1 = tk.Entry(self)
        entry1.pack()
        
        #save type of place to user information class
        
        #entry1.grid(row=1,column=2,columnspan=3)
        submit = ttk.Button(self, text="Next", command=lambda: controller.show_frame(PageThree))
        submit.pack()
        #submit.grid(row=1,column=5)
        
        button1 = ttk.Button(self, text="Back",
                            command=lambda: controller.show_frame(PageOne))
        button1.pack()
        #button1.grid(row=2, column=2)
        
        button2 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button2.pack()
        #button2.grid(row=2,column=3)
        
        button3 = ttk.Button(self, text="Quit", command=quit)
        button3.pack()
        #button3.grid(row=2,column=4)
        
class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        label = tk.Label(self, text="What type of item do you want?", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        label1 = tk.Label(self, text="Search:")
        label1.pack()
        #label1.grid(row=1,column=2, columnspan=1)
        entry1 = tk.Entry(self)
        entry1.pack()
        #entry1.grid(row=1,column=2,columnspan=3)
        
        #save item to user information class
                
        submit = ttk.Button(self, text="Next", command=lambda: controller.show_frame(PageFour))
        submit.pack()
        #submit.grid(row=1,column=5)
        
        button1 = ttk.Button(self, text="Back",
                            command=lambda: controller.show_frame(PageTwo))
        button1.pack()
        #button1.grid(row=2, column=2)
        
        button2 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button2.pack()
        #button2.grid(row=2,column=3)
        
        button3 = ttk.Button(self, text="Quit", command=quit)
        button3.pack()
        #button3.grid(row=2,column=4)
        
class PageFour(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        label = tk.Label(self, text="What store did you purchase from?", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        #dropdown box, save store to user information class
        
        
        button1 = ttk.Button(self, text="Next", command=lambda: controller.show_frame(PageFive))
        button1.pack()
        
        button2 = ttk.Button(self, text="Back",
                            command=lambda: controller.show_frame(PageThree))
        button2.pack()
        #button1.grid(row=2, column=2)
        
        button3 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button3.pack()
        #button2.grid(row=2,column=3)
        
        button4 = ttk.Button(self, text="Quit", command=quit)
        button4.pack()
        #button3.grid(row=2,column=4)
        
class PageFive(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        label = tk.Label(self, text="Contant Information", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        first_name = tk.Label(self, text="Full Name:")
        first_name.pack()
        entry1 = tk.Entry(self)
        entry1.pack()
        last_name = tk.Label(self, text="Email Address:")
        last_name.pack()
        entry2 = tk.Entry(self)
        entry2.pack()
        phone_number =tk.Label(self, text="Phone Number:")
        phone_number.pack()
        entry3 = tk.Entry(self)
        entry3.pack()
        
        #save full name, email and phone to user information class. Bring address from user information class to PageFive       
        
        delivery_date = tk.Label(self, text="Select Delivery Date")
        delivery_date.pack()
        
        myCal = tcal.Calendar(self, setmode = "day'", date_pattern = "mm/dd/yy")
        myCal.pack(pady = 10)
        
        #save myCal value to user information class
        
        openCal = tk.Button(self, text = "Confirm", fg = "black", bg = "snow", command=lambda: controller.show_frame(PageSix))
        openCal.pack(pady = 10)

        
        button2 = ttk.Button(self, text="Back",
                            command=lambda: controller.show_frame(PageThree))
        button2.pack()
        #button1.grid(row=2, column=2)
        
        button3 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button3.pack()
        #button2.grid(row=2,column=3)
        
        button4 = ttk.Button(self, text="Quit", command=quit)
        button4.pack()
        #button3.grid(row=2,column=4)


class PageSix(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Receipt", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        
        
        button1 = ttk.Button(self, text="Next",
                            command=lambda: controller.show_frame(PageOne))
        button1.pack()
        
        button2 = ttk.Button(self, text="Quit", command=quit)
        button2.pack()


if __name__ == '__main__':
    app = Main()
    app.mainloop()