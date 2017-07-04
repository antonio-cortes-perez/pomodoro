#!/usr/bin/env python
import sys
import tkinter as tk
from tkinter import ttk


def main(intervals):
    print(str(intervals))
    win = tk.Tk()
    win.title('Pomodoro')
    win.resizable(0, 0)
    button = ttk.Button(win, text='counter')
    style = ttk.Style()
    style.configure('Red.TButton', background='red')

    def Action():
        button.configure(style='Red.TButton')
        button.configure(text='=')

    button.configure(command=Action)
    button.grid(column=0, row=0)
    win.mainloop()


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Error: provide at least one interval')
    else:
        main([int(arg) for arg in sys.argv[1:]])
