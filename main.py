from tkinter import *
from tkinter import ttk
from PIL import ImageTk
import math
import config
rounds = 0
timer = 0
pomodoros = 0
rep = 0


class Pomodoro:

    # main function with inital ui.
    def __init__(self):
        self.root = Tk()
        self.root.geometry("800x600")
        self.root.title("Pomodoro App")

        self.img1 = ImageTk.PhotoImage(file="images/pexels-alena-darmel-7223311.jpg")
        self.img2 = ImageTk.PhotoImage(file="images/pexels-brett-sayles-1292627.jpg")
        self.img3 = ImageTk.PhotoImage(file="images/pexels-miriam-espacio-110854.jpg")
        self.img4 = ImageTk.PhotoImage(file="images/pexels-tomáš-malík-3509971.jpg")

        self.canvas = Canvas(self.root)
        self.img = self.canvas.create_image(0, 0, image=self.img1, anchor=NW)
        self.title_label = self.canvas.create_text(400, 130, text="", fill="White", font=(config.font, 40, "bold"))
        self.timer_text = self.canvas.create_text(400, 190, text="", fill="white", font=(config.font, 26, "bold"))
        self.canvas.pack(fill="both", expand=True)
        self.pomodoro_counter = self.canvas.create_text(400, 430, text="Pomodoros: 0", fill="White", font=(config.font, 26, "bold"))

        variable = StringVar(self.root)
        variable.set("")  # default value
        w = ttk.OptionMenu(
            self.root,
            variable,
            "Choose a design template",
            *config.design_options,
            command=lambda x: self.change_design_by_template(x)
        )
        w.config(width=40)
        w.pack(pady=0, padx=100)

        self.root.mainloop()

    # Start and working function.
    def start_working_timer(self):
        global rounds, rep
        rounds += 1

        if rounds % 8 == 0:
            self.calculate(config.long_break)
            self.canvas.itemconfig(self.title_label, text="Long Break")
        elif rounds % 2 == 0:
            self.calculate(config.short_break)
            self.canvas.itemconfig(self.title_label, text="Short Break")
        else:
            rep += 1
            self.calculate(config.working_timer)
            self.canvas.itemconfig(self.title_label, text="Work")
            self.canvas.itemconfig(self.pomodoro_counter, text=f"Pomodoros: {rep}")

    # Reset function.
    def reset_working_timer(self):
        global rounds, rep
        rounds = 0
        rep = 0

        self.root.after_cancel(timer)
        self.canvas.itemconfig(self.timer_text, text="00:00")
        self.canvas.itemconfig(self.title_label, text="Timer")
        self.canvas.itemconfig(self.pomodoro_counter, text=f"Pomodoros: {rep}")

    # Calculate remaining term.
    def calculate(self, count):
        count_min = math.floor(count / 60)
        count_sec = count % 60
        if count_sec < 10:
            count_sec = f"0{count_sec}"

        self.canvas.itemconfig(self.timer_text, text=f"{count_min}:{count_sec}")
        if count > 0:
            global timer
            timer = self.root.after(1000, self.calculate, count - 1)
        else:
            self.start_working_timer()

    # Change background and button images by chosen template.
    def change_design_by_template(self, variable):
        global start_btn, stop_btn, bgg

        x = config.design_options[variable]
        if x == 'Tomato':
            self.canvas.itemconfig(self.img, image=self.img1)
            start_btn = PhotoImage(file="images/start.png")
            stop_btn = PhotoImage(file="images/stop.png")
        if x == 'Moon':
            self.canvas.itemconfig(self.img, image=self.img2)
            start_btn = PhotoImage(file="images/start.png")
            stop_btn = PhotoImage(file="images/stop.png")
        if x == 'Stars':
            self.canvas.itemconfig(self.img, image=self.img3)
            start_btn = PhotoImage(file="images/start_red.png")
            stop_btn = PhotoImage(file="images/stop_red.png")
        if x == 'Winter-Forrest':
            self.canvas.itemconfig(self.img, image=self.img4)
            start_btn = PhotoImage(file="images/start.png")
            stop_btn = PhotoImage(file="images/stop.png")

        start_button = Button(self.root, image=start_btn, command=self.start_working_timer, borderwidth=0, cursor="hand2")
        start_button.place(x=100, y=340)
        reset_button = Button(self.root, image=stop_btn, command=self.reset_working_timer, borderwidth=0, cursor="hand2")
        reset_button.place(x=600, y=340)


Pomodoro()
