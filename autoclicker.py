import time
import threading
from tkinter import *
from tkinter.ttk import *
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

# Configuration
delay = 0.009           # Time between clicks (seconds)
button = Button.left    # Button to click
start_stop_key = KeyCode(char='s') # Press 's' to toggle
exit_key = KeyCode(char='e')       # Press 'e' to quit

class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super().__init__()
        self.root = Tk()
        self.root.title("Auto Clicker")
        self.root.iconbitmap("Mouse.ico")
        self.root.geometry("300x300")
        self.root.resizable(True, True)
        self.widgets()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

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
            text="Enter",
            command=lambda: self.root.destroy()
        )

        self.topFrame.grid_configure(padx=10, pady=10)
        self.speedBox.grid(row=0, column=0)
        self.enterButton.grid(row=1, column=0)
        for widget in self.topFrame.winfo_children():
            widget.grid_configure(pady=10, padx=10)

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)

        



def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == exit_key:
        click_thread.exit()
        listener.stop()

with Listener(on_press=on_press) as listener:
    listener.join()

mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()