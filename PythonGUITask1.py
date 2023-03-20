# Importing tkinter and replacing tkinter as tk
from tkinter import *
from tkinter import messagebox


class GUI:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("700x250")

        # Renaming the title
        self.window.title("TASK I")

        # Making an entry
        self.MTH = Label(text="Insert your MTH-101 score >> ", font=("Arial", 12))
        self.MTH.grid(row=0, column=0)

        self.CSC = Label(text="Insert your CSC-101 score >> ", font=("Arial", 12))
        self.CSC.grid(row=1, column=0)

        self.CHM = Label(text="Insert your CHM-101 score >> ", font=("Arial", 12))
        self.CHM.grid(row=2, column=0)

        self.PHY = Label(text="Insert your PHY-101 score >> ", font=("Arial", 12))
        self.PHY.grid(row=3, column=0)

        self.PHY_2 = Label(text="Insert your PHY-103 score >> ", font=("Arial", 12))
        self.PHY_2.grid(row=4, column=0)

        self.STA = Label(text="Insert your STA-101 score >> ", font=("Arial", 12))
        self.STA.grid(row=5, column=0)

        self.GST = Label(text="Insert your GST-103 score >> ", font=("Arial", 12))
        self.GST.grid(row=6, column=0)

        self.GST_2 = Label(text="Insert your GST-105 score >> ", font=("Arial", 12))
        self.GST_2.grid(row=7, column=0)

        self.gap1 = Entry(self.window, width=50)
        self.gap1.grid(row=0, column=1)

        self.gap2 = Entry(self.window, width=50)
        self.gap2.grid(row=1, column=1)

        self.gap3 = Entry(self.window, width=50)
        self.gap3.grid(row=2, column=1)

        self.gap4 = Entry(self.window, width=50)
        self.gap4.grid(row=3, column=1)

        self.gap5 = Entry(self.window, width=50)
        self.gap5.grid(row=4, column=1)

        self.gap6 = Entry(self.window, width=50)
        self.gap6.grid(row=5, column=1)

        self.gap7 = Entry(self.window, width=50)
        self.gap7.grid(row=6, column=1)

        self.gap8 = Entry(self.window, width=50)
        self.gap8.grid(row=7, column=1)

        self.button1 = Button(self.window, text="Submit Total", font=("Arial", 12), command=self.Total)
        self.button1.grid(row=10, column=0)

        self.button2 = Button(self.window, text="Submit Average", font=("Arial", 12), command=self.Average)
        self.button2.grid(row=10, column=1)

        self.button = Button(self.window, text="Submit Percentage", font=("Arial", 12), command=self.Percentage)
        self.button.grid(row=10, column=2)

        self.window.mainloop()

    def Total(self):
        blank1 = int(self.gap1.get())
        blank2 = int(self.gap2.get())
        blank3 = int(self.gap3.get())
        blank4 = int(self.gap4.get())
        blank5 = int(self.gap5.get())
        blank6 = int(self.gap6.get())
        blank7 = int(self.gap7.get())
        blank8 = int(self.gap8.get())
        blanks = [blank1, blank2, blank3, blank4, blank5, blank6, blank7, blank8]
        total = sum(blanks)
        messagebox.showinfo(title="Total", message=str(total))

    def Average(self):
        blank1 = int(self.gap1.get())
        blank2 = int(self.gap2.get())
        blank3 = int(self.gap3.get())
        blank4 = int(self.gap4.get())
        blank5 = int(self.gap5.get())
        blank6 = int(self.gap6.get())
        blank7 = int(self.gap7.get())
        blank8 = int(self.gap8.get())
        blanks = [blank1, blank2, blank3, blank4, blank5, blank6, blank7, blank8]
        average = sum(blanks) / len(blanks)
        messagebox.showinfo(title="Average", message=str(average))

    def Percentage(self):
        blank1 = int(self.gap1.get())
        blank2 = int(self.gap2.get())
        blank3 = int(self.gap3.get())
        blank4 = int(self.gap4.get())
        blank5 = int(self.gap5.get())
        blank6 = int(self.gap6.get())
        blank7 = int(self.gap7.get())
        blank8 = int(self.gap8.get())
        blanks = [blank1, blank2, blank3, blank4, blank5, blank6, blank7, blank8]
        percentage = sum(blanks) / len(blanks) * 100
        messagebox.showinfo(title="Percentage", message=str(percentage))

GUI()
