from tkinter import Tk, Label, Button, Entry

class Root(Tk):
    def _init_(self):
        super()._init_()
        self.title_label = Label(self, text="A Simple eval-based calculator, \nnot for production usage :)")
        self.title_label.pack()
        self.entry = Entry(self)
        self.entry.pack()
        self.entry.insert(0, "1+2")
        self.label = Label(self, text="")
        self.label.pack()
        self.button = Button(self, text="Compute", command=self.onclick)
        self.button.pack()

    def onclick(self):
        self.label.configure(text=str(eval(self.entry.get())))


root = Root()
root.mainloop()
