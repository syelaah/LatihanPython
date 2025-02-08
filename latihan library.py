import tkinter as tk

window = tk.Tk()

hello = tk.Label(text = "Hello Syela!")
hello.pack()

click_me = tk.Button(
    text = "Click me!",
    width = 10,
    height = 5
    )
click_me.pack()

label = tk.Label(text = "Your Name:")
entry = tk.Entry(width = 20)

label.pack()
entry.pack()

comment = tk.Label(text = "Comment:")
text_box = tk.Text(width = 50, height = 10)

comment.pack()
text_box.pack()

window.mainloop()
