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

        linklabel = Label(text="Youtube Link : ", font="Helvetica 10 bold")
        linklabel.place(x=5, y=50)

        self.linkentry = Entry(width=75)
        self.linkentry.place(x=120, y=52)

        pathlabel = Label(text="Download Path : ", font="Helvetica 10 bold")
        pathlabel.place(x=5, y=85)

        self.pathentry = Entry(width=75)
        self.pathentry.place(x=120, y=87)
        self.pathentry.insert(0, "E:/Footage")

        self.list = Listbox()
        self.list.place(x=120, y=115, width=455)
        self.list.bind('<<ListboxSelect>>', self.items_selected)

        self.get_btn = Button(text="GET VIDEOS", command=self.get_videos)
        self.get_btn.place(x=225, y=350)

        self.download_btn = Button(text="DOWNLOAD", command=self.download, state=DISABLED)
        self.download_btn.place(x=325, y=350)

    def items_selected(self, event):
        pass

    def get_videos(self):
        pass

    def download(self):
        pass



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    w = Window()
    mainloop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
