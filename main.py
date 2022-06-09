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
        master.grid_columnconfigure((0, 1), weight=1)

        self.select = []
        self.bg = "#2B2B2B"
        self.fg = "#CECCBE"
        self.yt = ""
        self.video = ""
        self.audio = ""
        self.tag = 0

        self.alert = Label(text="Wellcome to Youtube Downloader. Pleace insert Youtube Link.",
                           fg="red",
                           bg=self.bg,
                           font="Helvetica 10 bold",
                           anchor="center",
                           pady=20)
        self.alert.grid(row=0, column=0, columnspan=2)

        linklabel = Label(text="Youtube Link : ", font="Helvetica 10 bold", bg=self.bg, fg=self.fg)
        linklabel.grid(row=1, column=0, sticky=E)

        self.linkentry = Entry(width=75, bg=self.bg, fg=self.fg)
        self.linkentry.grid(row=1, column=1)

        pathlabel = Label(text="Download Path : ", font="Helvetica 10 bold", bg=self.bg, fg=self.fg)
        pathlabel.grid(row=2, column=0, sticky=E)

        self.pathentry = Entry(width=75, bg=self.bg, fg=self.fg)
        self.pathentry.grid(row=2, column=1)

        self.pathentry.insert(0, "E:/Footage")

        listlabel = Label(text="Videos : ", font="Helvetica 10 bold", bg=self.bg, fg=self.fg)
        listlabel.grid(row=3, column=0, sticky=NE)

        self.list = Listbox(bg=self.bg, fg=self.fg, width=75)
        self.list.grid(row=3, column=1)
        self.list.bind('<<ListboxSelect>>', self.items_selected)

        self.alertbottomtitle = Label(text="Download : ", bg=self.bg, fg=self.fg, font="Helvetica 10 bold")
        self.alertbottomtitle.grid(row=4, column=0)

        self.alertbottom = Label(text="", bg=self.bg, fg=self.fg, font="Helvetica 10 bold")
        self.alertbottom.grid(row=4, column=1, sticky=W)

        self.pb = ttk.Progressbar(
            orient='horizontal',
            mode='determinate',
            length=590
        )

        self.pb.grid(row=5, column=0, columnspan=2)

        self.pb["value"] = 0

        self.get_btn = Button(text="GET VIDEOS", command=self.get_videos)
        self.get_btn.place(x=430, y=320)

        self.download_btn = Button(text="DOWNLOAD", command=self.download, state=DISABLED)
        self.download_btn.place(x=516, y=320)

    def items_selected(self, event):
        # get selected indices
        selected_indices = self.list.curselection()
        # get selected items
        selected = ",".join([self.list.get(i) for i in selected_indices])
        # msg = f'You selected: {selected}'
        self.alertbottom["text"] = selected
        self.download_btn["state"] = NORMAL
        self.tag = self.select[self.list.curselection()[0]]

    def set_videos(self):
        self.alert.config(text="Please Wait")
        self.yt = YouTube(self.linkentry.get(), on_progress_callback=self.on_progress,
                          on_complete_callback=self.on_complete)
        self.alert.config(text=self.yt.title)
        self.video = self.yt.streams.filter(file_extension='mp4')
        self.set_video_list()

    def get_videos(self):
        if self.linkentry.get() is not "" and self.pathentry.get() is not "":
            self.get_btn["state"] = DISABLED
            threading.Thread(target=self.set_videos).start()
        else:
            self.alert.config(text="Please Set All Fields.")

    def set_video_list(self):
        self.video = self.video.order_by('resolution')
        for stream in self.video:
            line = str(stream.resolution) + \
                   " FPS : " + str(stream.fps) + \
                   " ABR : " + str(stream.abr)
            self.list.insert(END, line)
            self.select.insert(len(self.select), str(stream.itag))
            self.get_btn["state"] = NORMAL

    def download(self):
        threading.Thread(target=self.downloadfile).start()

    def downloadfile(self):
        self.download_btn["state"] = DISABLED
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
        self.pb["value"] = 0


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root = Tk()
    root.geometry("600x350+300+300")
    root.config(bg="#2B2B2B")
    window = Window(root)
    root.mainloop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
