from tkinter import *
from tkinter.ttk import *
import autoclicker
ac = autoclicker

class clickApp:
    def __init__(self):
        self.root = Tk()
        self.root.title("Auto Clicker")
        self.root.iconbitmap("Mouse.ico")
        self.root.geometry("300x300")
        self.root.resizable(False, False)
        self.widgets()
        self.root.mainloop()

    def widgets(self):
        self.topFrame = LabelFrame(
            self.root,
            text="Speed Options",
            relief=GROOVE
        )

        self.bottomFrame = LabelFrame(
            self.root,
            relief=GROOVE
        )

        self.speedBox = Entry(
            self.topFrame,
            width=10
        )

        self.enterButton = Button(
            self.topFrame,
            text="Enter"
            # command=lambda:
        )
        
        self.instruction = Label(
            text="Press 'S' to start, 'e' to exit"
        )

        self.topFrame.grid_configure(padx=10, pady=10)
        self.bottomFrame.grid_configure(padx=10, pady=10)
        self.speedBox.grid(row=0, column=0)
        self.enterButton.grid(row=1, column=0)
        self.instruction.grid(row=0, column=0)
        for widget in self.topFrame.winfo_children():
            widget.grid_configure(padx=10, pady=10)
        for widget in self.topFrame.winfo_children():
            widget.grid_configure(pady=10, padx=10)
        
        


if __name__ == '__main__':
    clicker = clickApp()