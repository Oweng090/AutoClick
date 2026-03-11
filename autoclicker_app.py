from tkinter import *
from tkinter.ttk import *
# import autoclicker

class clickApp:
    def __init__(self):
        self.root = Tk()
        self.root.title("Auto Clicker")
        self.root.iconbitmap("Mouse.ico")
        self.root.geometry("300x300")
        self.root.resizable(True, True)
        self.widgets()

    def widgets(self):
        self.topFrame = LabelFrame(
            self.root,
            text="Speed Options",
            relief="groove"
        )

        self.speedBox = Entry(
            self.topFrame,
            width=10
        )

        self.enterButton = Button(
            self.topFrame,
            text="Enter"
        )

        self.topFrame.grid_configure(padx=10, pady=10)
        self.speedBox.grid(row=0, column=0)
        self.enterButton.grid(row=1, column=0)
        for widget in self.topFrame.winfo_children():
            widget.grid_configure(pady=10, padx=10)

if __name__ == '__main__':
    clickapp = clickApp()