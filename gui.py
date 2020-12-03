import tkinter as tk
from tkinter import ttk

LARGE_FONT = ("Times")
api = 'asdkjasghasdgjlasdasdas'
class Main(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        tk.Tk.wm_title(self, "Shopping App")
        
        container = tk.Frame(self)
        
        container.pack(side="top", fill="both", expand = True)
        
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        
        for F in (StartPage, PageOne, PageTwo, PageThree, PageFour):
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
        
        button1 = ttk.Button(self, text="Continue",
                            command=lambda: controller.show_frame(PageOne))
        button1.pack()
        
        button2 = ttk.Button(self, text="Quit", command=quit)
        button2.pack()

class PageOne(tk.Frame):

    def __init__(self, parent, controller,address):
        self.address = address
        tk.Frame.__init__(self, parent)
        title = tk.Label(self, text="What is your location?", font=LARGE_FONT)
        title.pack(pady=10,padx=10)
        
        label1 = tk.Label(self, text="Your Address:")
        label1.pack()
        entry1 = tk.Entry(self)
        entry1.pack()
        submit = ttk.Button(self, text="SUBMIT", command=lambda: controller.show_frame(PageTwo))
        submit.pack()
        
        
        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()
        
        button2 = ttk.Button(self, text="Quit", command=quit)
        button2.pack()
        
class PageTwo(PageOne,tk.Frame):

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
        #entry1.grid(row=1,column=2,columnspan=3)
        submit = ttk.Button(self, text="SUBMIT", command=lambda: controller.show_frame(PageThree))
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
        
        submit = ttk.Button(self, text="SUBMIT", command=lambda: controller.show_frame(PageFour))
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
        
        label = tk.Label(self, text="What store would you like to purchase from?", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        button1 = ttk.Button(self, text="Back",
                            command=lambda: controller.show_frame(PageThree))
        button1.pack()
        #button1.grid(row=2, column=2)
        
        button2 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button2.pack()
        #button2.grid(row=2,column=3)
        
        button3 = ttk.Button(self, text="Quit", command=quit)
        button3.pack()
        #button3.grid(row=2,column=4)
        
if __name__ == '__main__':
    app = Main()
    app.mainloop()