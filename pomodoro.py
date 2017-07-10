#!/usr/bin/env python
import sys
import tkinter as tk
from tkinter import ttk


class Pomodoro():
    def __init__(self, intervals):
        self.intervals = intervals
        self.win = tk.Tk()
        self.win.title('Pomodoro')
        self.win.resizable(0, 0)
        self.createButton()
        self.positionWindow()

    def positionWindow(self):
        self.win.update()
        ws = self.win.winfo_screenwidth()
        hs = self.win.winfo_screenheight()
        w = self.win.winfo_width()
        h = self.win.winfo_height()
        self.win.geometry("%dx%d+%d+%d" % (w, h, ws-w, hs-h))

    def createButton(self):
        self.button = ttk.Button(self.win, text='counter')
        self.button.configure(command=self.action)
        self.button.grid(column=0, row=0)
        style = ttk.Style()
        style.configure('Red.TButton', background='red')

    def action(self):
        self.button.configure(style='Red.TButton')
        self.button.configure(text='=')
        self.win.title('X')


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Error: provide at least one interval')
    else:
        pomodoro = Pomodoro([int(arg) for arg in sys.argv[1:]])
        pomodoro.win.mainloop()
