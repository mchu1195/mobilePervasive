from tkinter import filedialog
import tkinter
import os

#GUI
class PhoneGUI:
    def __init__(self, master):
        #logic variables
        self.files = []
        self.cloudlet = "blah"

        #GUI stuff
        self.master = master
        master.title("Amber Alert Search")

        #Label
        self.label_text = tkinter.StringVar()
        self.label_text.set("Choose images to submit to help out the search!")
        self.label = tkinter.Label(master, textvariable=self.label_text)
        self.label.grid(columnspan=3, sticky=tkinter.N)

        #where we display selected files
        self.text = tkinter.Text(master, height=15, width=60)
        self.text.insert(tkinter.INSERT, "No images selected")
        self.text.grid(columnspan=3, row=1)
        self.yscroller = tkinter.Scrollbar(master, command=self.text.yview)
        self.yscroller.grid(row=1, column=3)
        self.text.config(yscrollcommand=self.yscroller.set)

        #buttons
        self.add_button = tkinter.Button(master, text="Add Images", command=self.add_files)
        self.add_button.grid(column=0, row=3)

        self.clear_button = tkinter.Button(master, text="Clear Selection", command=self.clear)
        self.clear_button.grid(column=1, row=3)

        self.send_button = tkinter.Button(master, text="Send images", command=self.send)
        self.send_button.grid(column=2, row=3)

        self.close_button = tkinter.Button(master, text="Close", command=master.quit)
        self.close_button.grid(column=3, row=3)

    def add_files(self):
        new_files = tkinter.filedialog.askopenfilenames(parent=root, title='Choose images to send')
        for nf in new_files:
            self.files.append(nf)
        self.label_text.set("Send these images?")
        self.text.delete(1.0, tkinter.END)
        for f in self.files:
            name = os.path.basename(f)
            self.text.insert(tkinter.INSERT, name + "\n")

    def clear(self):
        self.files = []
        self.text.delete(1.0, tkinter.END)
        self.text.insert(tkinter.INSERT, "No images selected")
        self.label_text.set("Select images to send")
    
    def send(self):
        if self.files == []:
            self.label_text.set("No Images to send! Select images first!")
            return
        self.files = []
        self.label_text.set("Images sent!, select more images to send?")
        self.text.delete(1.0, tkinter.END)
        self.text.insert(tkinter.INSERT, "No images selected")
        

root = tkinter.Tk()
my_gui = PhoneGUI(root)
root.mainloop()
print("Done")