from tkinter import *
from tkinter import messagebox


class GUI:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("730x200")

        self.window.title("TASK II")

        self.name = Label(text="NAME", font=("Arial", 16))
        self.name.grid(row=0, column=0)

        self.age = Label(text="AGE", font=("Arial", 16))
        self.age.grid(row=0, column=1)

        self.exp = Label(text="WORK EXPERIENCE", font=("Arial", 16))
        self.exp.grid(row=0, column=2)

        self.name_entry = Entry(self.window, width=30)
        self.name_entry.grid(row=1, column=0, padx=10)

        self.age_entry = Entry(self.window, width=30)
        self.age_entry.grid(row=1, column=1, padx=20)

        self.exp_entry = Entry(self.window, width=30)
        self.exp_entry.grid(row=1, column=2)

        self.btn1 = Button(self.window, text="Proceed", font=("Arial", 12), command=self.Evaluation)
        self.btn1.grid(row=2, column=4)

        self.window.mainloop()

    def Evaluation(self):
        age_blank = int(self.age_entry.get())
        exp_blank = int(self.exp_entry.get())

        if exp_blank > 10 and age_blank >= 35:
            messagebox.showinfo(title="Salary", message="Your Salary is 600,000 Naira")
        elif exp_blank > 5 and 28 <= age_blank < 35:
            messagebox.showinfo(title="Salary", message="Your Salary is 480,000 Naira")
        elif exp_blank < 5 and age_blank < 28:
            messagebox.showinfo(title="Salary", message="Your Salary is 250,000 Naira")


GUI()
