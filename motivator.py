import tkinter
from tkinter import ttk
from playsound import playsound
from PIL import ImageTk
from threading import Thread

class App:
    def __init__(self, root, window_title):
        self.root = root
        self.root.title(window_title)

        self.images = {"dothething": ImageTk.PhotoImage(file="dothething.gif"),
                       "reward": ImageTk.PhotoImage(file="reward.gif")}

        self.button_one = ttk.Button(self.root)
        self.button_two = ttk.Button(self.root, text="I have not yet done the thing",
                                     command=lambda: self.play_sound(False))
        self.status = ttk.Label(self.root)
        self.image = ttk.Label(self.root)

        for item in (self.status, self.image, self.button_one):
            item.pack()

        self.do_the_thing()
        self.root.mainloop()

    def play_sound(self, victory):
        if victory:
            Thread(target=playsound, args=("victory.mp3",)).start()
        else:
            Thread(target=playsound, args=("sadtrombone.mp3",)).start()

    def set_image(self, image):
        img = self.images[image]
        self.image.configure(image=img)
        self.image.image = img
        self.root.update_idletasks()

    def do_the_thing(self):
        self.set_image("dothething")

        self.status.configure(text="")
        self.button_two.pack()
        self.button_one.configure(text="I did the thing", command=self.did_the_thing)

    def did_the_thing(self):
        self.set_image("reward")
        self.play_sound(True)

        self.button_two.forget()
        self.status.configure(text="Good job! Reward yourself!")
        self.button_one.configure(text="I have another thing to do", command=self.do_the_thing)

if __name__ == '__main__':
    root = tkinter.Tk()
    app = App(root, "Motivator")
    root.mainloop()