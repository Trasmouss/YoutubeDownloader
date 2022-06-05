from tkinter import *

# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Window(object):

    def __init__(self):
        self.window = Tk()
        self.window.resizable(width=FALSE, height=FALSE)
        self.window.geometry("600x400+300+300")
        self.window.title("Youtube Downloader")

        self.alert = Label(text="Wellcome to Youtube Downloader. Pleace insert Youtube Link.",
                           fg="red",
                           font="Helvetica 10 bold")

        self.alert.place(x=5, y=15)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    w = Window()
    mainloop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
