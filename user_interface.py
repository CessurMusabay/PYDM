from tkinter import *
from tkinter.ttk import *
import downloader
import threading
import os
from tkinter import messagebox



class App:
    def __init__(self):
        self.row = 1
        self.root = Tk()
        self.progress_bars = {}
        self.id = 0
        self.folder_name = 'Downloads'
        self.downloading_files = []


        url_input = Entry(self.root, width=50)
        download_button = Button(text='Download', master=self.root, command=self.download)
        url_input.grid(row=0, column=0, padx=10, pady=10)
        download_button.grid(row=0, column=1, padx=10, pady=10)

        self.url_input = url_input


    def __check_file(self,file_name):
        folder_path = os.path.join('./',self.folder_name)
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)

        path = os.path.join(folder_path,file_name)
        if os.path.exists(path) or file_name in self.downloading_files:
            messagebox.showinfo(file_name, f"{file_name} is already downloaded or currently downloading")
            return None
        else:
            return file_name



    def __add_progress_bar(self,file_name):
        self.progress_bars[str(self.id)] = Progressbar(self.root, orient=HORIZONTAL, length=100, mode='determinate')

        Label(text=file_name).grid(row=self.row, column=1)
        self.progress_bars[str(self.id)].grid(row=self.row, column=0)
        self.row += 1
        self.id += 1
        self.root.update_idletasks()

        return self.id - 1


    def download(self):
        url = self.url_input.get()
        file_name = self.__check_file(url.split('/')[-1])
        if file_name == None:
            return

        self.downloading_files.append(file_name)
        id = self.__add_progress_bar(file_name)
        t = threading.Thread(target=downloader.download,args=(url,self.progress_bars[str(id)],os.path.join('./',self.folder_name,file_name),self.root))
        t.start()
        self.url_input.delete(0, 'end')


    def start(self):
        self.root.mainloop()



if __name__ == '__main__':
    a = App()
    a.start()



