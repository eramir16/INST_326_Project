import tkinter as tk
from tkinter import ttk
import re 
import requests
import json 
import tkcalendar as tcal
import get_address
import get_info
import random

#101 Halpine Road Rockville MD


LARGE_FONT = ("Times")

class Main(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        tk.Tk.wm_title(self, "Shopping App")
        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        
        for F in (StartPage, PageOne, PageTwo, PageThree, PageFive, PageSix):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame(StartPage)
        
    def show_frame(self, cont):
        
        frame = self.frames[cont]
        frame.tkraise()
    
    def get_page(self, page_name):
        for page in self.frames.values():
            if str(page.__class__.__name__) == page_name:
                return page
        return None      
    
class StartPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.make_widget(controller)
        
    def make_widget(self, controller):
        label = tk.Label(self, text="Welcome to our app!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        next_page = ttk.Button(self, text="Next", command=lambda: controller.show_frame(PageOne))
        next_page.pack()
        
        quit_program = ttk.Button(self, text="Quit", command=quit)
        quit_program.pack()

class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller               
      
        title = tk.Label(self, text="Dropoff Location?", font=LARGE_FONT)
        title.pack(pady=10,padx=10)
        
        label1 = tk.Label(self, text="Address:")
        label1.pack()
        
        self.address = tk.Entry(self)
        self.address.pack()
        
        next_page = ttk.Button(self, text="Next", command=lambda: self.next_page())
        next_page.pack()
        
        back = ttk.Button(self, text="Back",
                            command=lambda: controller.show_frame(StartPage))
        back.pack()
        
        home = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        home.pack()
        
        quit_program = ttk.Button(self, text="Quit", command=quit)
        quit_program.pack()
    
    def next_page(self):
        self.controller.show_frame(PageTwo)
        
class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        title = tk.Label(self, text="What type of place are you trying to buy from?", font=LARGE_FONT)
        title.pack(pady=10,padx=10)
        
        label1 = tk.Label(self, text="Search:")
        label1.pack()

        self.type_of_place = tk.Entry(self)
        self.type_of_place.pack()

        next_page = ttk.Button(self, text="Next", command=lambda: self.next_page())
        next_page.pack()
        
        back = ttk.Button(self, text="Back",
                            command=lambda: controller.show_frame(PageOne))
        back.pack()
        
        home = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        home.pack()
        
        quit_program = ttk.Button(self, text="Quit", command=quit)
        quit_program.pack()
        
    def next_page(self):
        self.controller.show_frame(PageThree)
            
class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
  
        title = tk.Label(self, text="What type of item do you want?", font=LARGE_FONT)
        title.pack(pady=10,padx=10)
        
        search = tk.Label(self, text="Search:")
        search.pack()

        self.type_of_item = tk.Entry(self)
        self.type_of_item.pack()
                
        next_page = ttk.Button(self, text="Next", command=lambda: self.next_page())
        next_page.pack()
        
        back = ttk.Button(self, text="Back",
                            command=lambda: controller.show_frame(PageTwo))
        back.pack()
        
        home = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        home.pack()
        
        quit_program = ttk.Button(self, text="Quit", command=quit)
        quit_program.pack()
        
    def next_page(self):
        self.controller.show_frame(PageFive)
        
#class PageFour(tk.Frame):

    #def __init__(self, parent, controller):
        #tk.Frame.__init__(self, parent)
        #self.controller = controller
        
        #label = tk.Label(self, text="What store did you purchase from?", font=LARGE_FONT)
        #label.pack(pady=10,padx=10)
        
        #next_page = ttk.Button(self, text="Next", command=lambda: controller.show_frame(PageFive))
        #next_page.pack()
        
        #back = ttk.Button(self, text="Back",
                            #command=lambda: controller.show_frame(PageTwo))
        #back.pack()
        
        #home = ttk.Button(self, text="Back to Home",
                            #command=lambda: controller.show_frame(StartPage))
        #home.pack()
        
        #quit_program = ttk.Button(self, text="Quit", command=quit)
        #quit_program.pack()

        
class PageFive(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Contant Information", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        full_name = tk.Label(self, text="Full Name:")
        full_name.pack()
        
        self.name_entry = tk.Entry(self)
        self.name_entry.pack()
        
        email_address = tk.Label(self, text="Email Address:")
        email_address.pack()
        
        self.email = tk.Entry(self)
        self.email.pack()
        
        phone_number = tk.Label(self, text="Phone Number:")
        phone_number.pack()
        
        self.phone = tk.Entry(self)
        self.phone.pack()
        
        self.myCal = tcal.Calendar(self, setmode = "day'", date_pattern = "mm/dd/yy") #self. makes attribute - ref anytime in class
        self.myCal.pack(pady = 10)
        
        next_page = ttk.Button(self, text = "Next", command=lambda: controller.show_frame(PageSix)) #remove () to not run function by default
        next_page.pack()
        
        
        button2 = ttk.Button(self, text="Back",
                            command=lambda: controller.show_frame(PageThree))
        button2.pack()
        
        button3 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button3.pack()
        
        button4 = ttk.Button(self, text="Quit", command=quit)
        button4.pack()
        
    def next_page(self):
        self.controller.show_frame(PageSix)

class PageSix(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        title = tk.Label(self, text="Receipt", font=LARGE_FONT)
        title.pack(pady=10,padx=10)
        
        button3 = ttk.Button(self, text="Show Receipt", command=lambda: self.show_information())
        button3.pack()

        
    def show_information(self):
        pageone = self.controller.get_page("PageOne")
        user_address = pageone.address.get()
        
        pagetwo = self.controller.get_page("PageTwo")
        type_of_place = pagetwo.type_of_place.get()
        
        pagethree = self.controller.get_page("PageThree")
        type_of_item = pagethree.type_of_item.get()
        
        
        pagefive = self.controller.get_page("PageFive")
        name = pagefive.name_entry.get()
        email_address = pagefive.email.get()
        phone_number = pagefive.phone.get()
        date_picked = pagefive.myCal.get_date()
        
        receipt_order_num = tk.Label(self,text = ('Order #'+str(random.randint(1000,6000))))
        receipt_order_num.pack()
        
        receipt1 = tk.Label(self, text=(f"Your Name: {name}"))
        receipt1.pack()
        
        receipt2 = tk.Label(self, text=(f"Your Address: {user_address}"))
        receipt2.pack()
        
        receipt3 = tk.Label(self, text=(f"Your Email: {email_address}"))
        receipt3.pack()
        
        receipt4 = tk.Label(self, text=(f"Your Number: {phone_number}"))
        receipt4.pack()
        
        receipt5 = tk.Label(self, text=(f"Delivery Date: {date_picked}"))
        receipt5.pack()
        
        receipt6 = tk.Label(self, text=(f"Store Type: {type_of_place}"))
        receipt6.pack()
        
        receipt7 = tk.Label(self, text=(f"Item Type: {type_of_item}"))
        receipt7.pack()
        
        button1 = ttk.Button(self, text="Back", command=lambda: self.controller.show_frame(PageFive))
        button1.pack()
        
        button2 = ttk.Button(self, text="Quit", command=quit)
        button2.pack()
        
        
        get_info.get_info(user_address,type_of_place,type_of_item)
        
if __name__ == '__main__':
    app = Main()
    app.mainloop()