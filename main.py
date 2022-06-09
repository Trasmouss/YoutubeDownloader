from tkinter import *
from tkinter import ttk
from pytube import YouTube
import threading

# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Window(object):

    def __init__(self, master):
        master.resizable(width=FALSE, height=FALSE)
        master.title("Youtube Downloader")

        self.bg = "#2B2B2B"
        self.fg = "#CECCBE"
        self.yt = ""
        self.video = ""
        self.tag = 0

        self.alert = Label(text="Wellcome to Youtube Downloader. Pleace insert Youtube Link.",
                           fg="red",
                           bg=self.bg,
                           font="Helvetica 10 bold")
        self.alert.place(x=5, y=15)

        linklabel = Label(text="Youtube Link : ", font="Helvetica 10 bold", bg=self.bg, fg=self.fg)
        linklabel.place(x=5, y=50)

        self.linkentry = Entry(width=75, bg=self.bg, fg=self.fg)
        self.linkentry.place(x=120, y=52)

        pathlabel = Label(text="Download Path : ", font="Helvetica 10 bold", bg=self.bg, fg=self.fg)
        pathlabel.place(x=5, y=85)

        self.pathentry = Entry(width=75, bg=self.bg, fg=self.fg)
        self.pathentry.place(x=120, y=87)
        self.pathentry.insert(0, "E:/Footage")

        self.list = Listbox(bg=self.bg, fg=self.fg)
        self.list.place(x=120, y=115, width=455)
        self.list.bind('<<ListboxSelect>>', self.items_selected)

        self.alertbottom = Label(text="Download : ", bg=self.bg, fg=self.fg, font="Helvetica 10 bold")
        self.alertbottom.place(x=5, y=300)

        self.pb = ttk.Progressbar(
            orient='horizontal',
            mode='determinate',
            length=590
        )

        self.pb.place(x=5000, y=0)

        self.pb["value"] = 0

        self.get_btn = Button(text="GET VIDEOS", command=self.get_videos)
        self.get_btn.place(x=225, y=350)

        self.download_btn = Button(text="DOWNLOAD", command=self.download, state=DISABLED)
        self.download_btn.place(x=325, y=350)

    def items_selected(self, event):
        # get selected indices
        selected_indices = self.list.curselection()
        # get selected items
        selected = ",".join([self.list.get(i) for i in selected_indices])
        # msg = f'You selected: {selected}'
        x = selected.split(" ")
        self.alertbottom["text"] = "Download : " + selected
        self.download_btn["state"] = NORMAL
        self.tag = x[0]
        # print(x[0])

    def set_videos(self):
        self.alert.config(text="Please Wait")
        self.yt = YouTube(self.linkentry.get(), on_progress_callback=self.on_progress,
                          on_complete_callback=self.on_complete)
        self.alert.config(text=self.yt.title)
        self.video = self.yt.streams
        self.setlist()

    def get_videos(self):
        if self.linkentry.get() is not "" and self.pathentry.get() is not "":
            self.get_btn["state"] = DISABLED
            threading.Thread(target=self.set_videos).start()
        else:
            self.alert.config(text="Please Set All Fields.")

    def setlist(self):
        self.video = self.video.order_by('resolution')
        for stream in self.video:
            line = str(stream.itag) + \
                   " RES : " + str(stream.resolution) + \
                   " FPS : " + str(stream.fps) + \
                   " AU : " + str(stream.audio_codec) + \
                   " VD : " + str(stream.video_codec) + \
                   " TYPE : " + str(stream.mime_type)
            self.list.insert(END, line)
            self.get_btn["state"] = NORMAL

    def download(self):
        threading.Thread(target=self.downloadfile).start()

    def downloadfile(self):
        self.download_btn["state"] = DISABLED
        self.pb.place(x=5, y=320)
        stream = self.video.get_by_itag(self.tag)
        stream.download(self.pathentry.get(), skip_existing=False)

    def on_progress(self, stream, chunk, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        percentage_of_completion = bytes_downloaded / total_size * 100
        self.pb['value'] = int(percentage_of_completion)

    def on_complete(self, stream, path):
        self.alertbottom["text"] = path
        self.download_btn["state"] = NORMAL
        self.pb.place(x=5000, y=0)
        self.pb["value"] = 0


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root = Tk()
    root.geometry("600x400+300+300")
    root.config(bg="#2B2B2B")
    window = Window(root)
    root.mainloop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
