from Samsung import *
from Poco import *
from Apple import *
from Vivo import *
from Mi import *
import tkinter as tk
main=tk.Tk()
w = tk.Label(main, text="Please select from the followings:""\n""Samsung, Apple, Mi, Poco, Vivo")
w.config(bg='skyblue', font=('Arial', 24, 'italic','bold'))
w.pack()
L1 =tk.Label(main, text="Company Name")
L1.config(bg='yellow', font=('Arial', 18, 'italic','bold'))
L1.pack( side = "top",padx=5, pady=5)
entry = tk.Entry(main)
entry.config(font=('Arial', 10, 'bold'),width=25)
entry.pack( side = "top")
def on_button():
    if entry.get() == "Samsung":
        tlabel=tk.Label(main,text=display_text())
        tlabel.pack()
    elif entry.get() == "Poco":
        tlabel = tk.Label(main, text=display_text2())
        tlabel.pack()
    elif entry.get() == "Vivo":
        tlabel = tk.Label(main, text=display_text4())
        tlabel.pack()
    elif entry.get() == "Apple":
        tlabel = tk.Label(main, text=display_text3())
        tlabel.pack()
    elif entry.get() == "Mi":
        tlabel = tk.Label(main, text=display_text5())
        tlabel.pack()
button2=tk.Button(main, text="ENTER", command=on_button)
button2.config(font=('Arial', 10, 'bold','italic'),width=10)
button2.pack(padx=5, pady=5)
main.mainloop()