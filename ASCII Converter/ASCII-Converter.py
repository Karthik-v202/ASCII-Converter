import string
from tkinter import *

def convert_to_numbers():
    ascii_text = enter1.get("1.0", "end-1c")

    if not all(char in string.ascii_letters for char in ascii_text):
        result_text.delete(1.0, END)
        result_text.insert(END, "Invalid input. Please enter valid ASCII text.")
        return

    numbers = [str(ord(char)) for char in ascii_text]
    result_text.delete(1.0, END)
    result_text.insert(END, "Numbers: " + ", ".join(numbers))

def convert_to_ascii():
    numbers = enter1.get("1.0", "end-1c").split(',')

    try:
        ascii_text = ''.join(chr(int(x.strip())) for x in numbers)
    except ValueError:
        result_text.delete(1.0, END)
        result_text.insert(END, "Invalid input. Please enter numbers separated by commas.")
        return

    result_text.delete(1.0, END)
    result_text.insert(END, "ASCII Text: " + ascii_text)

win = Tk()
win.title("ASCII CONVERTER")
win.config(bg="Navy")
win.geometry("500x600")

label1 = Label(win, text="Enter your Text", font=("Times New Roman", 20, "bold"), bg="Black", fg="lime")
label1.place(x=10, y=20, height=40, width=300)

enter1 = Text(win, font=("Times New Roman", 15), bg="black", fg="lime")
enter1.place(x=20, y=70, height=300, width=455)

btn_encode = Button(win, text="ASCII Encode", font=("Times New Roman", 20), bg="Black", fg="lime",
                    command=convert_to_numbers)
btn_encode.place(x=20, y=390, height=50, width=220)

btn_decode = Button(win, text="ASCII Decode", font=("Times New Roman", 20), bg="Black", fg="lime",
                    command=convert_to_ascii)
btn_decode.place(x=260, y=390, height=50, width=220)

result_text = Text(win, font=("Times New Roman", 15), bg="Black", fg="lime")
result_text.place(x=20, y=460, height=100, width=460)

win.mainloop()
