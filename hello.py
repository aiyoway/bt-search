# -*- coding: UTF-8 -*-

from tkinter import *
import tkinter.messagebox as message_box
from tkinter import ttk


class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack()
        self.init_widgets()

    def init_widgets(self):
        self.search_btn = Button(self, text='Search', command=self.search)
        self.search_btn.pack()

        self.keywords = Entry(self)
        self.keywords.pack()

        self.strVar = StringVar()
        self.select = ttk.Combobox(self.master, textvariable=self.strVar)

        self.select['values'] = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        self.select.current(0)
        self.select.pack()

        self.create_search_res()

    def create_search_res(self):
        low_f = Frame(self.master)
        low_f.pack(fill=Y, expand=YES)

        li = ['red', 'blue', 'green', 'black', 'white', 'orange', 'gray', 'yellow']
        self.list = Listbox(low_f)
        self.list.pack(side=LEFT, fill=Y, expand=YES)
        for i in li:
            self.list.insert(0, i)

        self.scroll = Scrollbar(low_f, command=self.list.yview())
        self.list['yscrollcommand'] = self.scroll.set
        self.scroll.pack(side=RIGHT, fill=Y)
        self.list.bind('<Double-1>', self.search)

    def change_channel(self):
        message_box.showinfo(title=None, message=str(self.select.get()))

    def search(self):
        name = self.keywords.get() or '默认搜索'
        message_box.showinfo('Message', 'search:%s' % name)

    def choose_res(self):
        info = str(self.list.curselection())
        message_box.showinfo(title=None, message=info)


if __name__ == '__main__':
    root = Tk()
    root.title = 'Hello world!'
    app = App(root)
    root.mainloop()
