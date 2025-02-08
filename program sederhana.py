import tkinter as tk

def minus():
    value = int(lbl_value['text'])
    lbl_value ['text'] = str(value - 1)

def plus():
    value = int(lbl_value['text'])
    lbl_value ['text'] = str(value + 1)
    
window = tk.Tk()

btn_minus = tk.Button(text="-", command=minus)
lbl_value = tk.Label(text="0")
btn_plus = tk.Button(text="+", command=plus)

btn_minus.grid(row=0, column=0)
lbl_value.grid(row=0, column=1)
btn_plus.grid(row=0, column=2)

window.mainloop()
