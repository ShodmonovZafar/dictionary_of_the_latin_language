import gui_class
import tkinter as tk
from tkinter import ttk

def gui_main_funksiyasi():
    
    
    my_gui = gui_class.Gui()
    
    my_gui.tab_control()
    my_gui.mighty()
    my_gui.widjetlar()
    my_gui.menyu_qatori()
    
    my_gui.mainloop()

if __name__ == "__main__":
    import tkinter as tk
    from pathlib import Path
    p = Path(".")
    for x in p.iterdir():
        if x.is_file() and x.name == "activate_the_latin_language_system.txt":
            with open("activate_the_latin_language_system.txt", 'r') as f:
                data = f.read()
            if data == "12345678":
                T = True
                break
        else:
            T = False

    while (not T):
        def kod_():
            ff = kod.get()
            with open("activate_the_latin_language_system.txt", 'w') as f:
                f.write(ff)
        win = tk.Tk()
        win.title("Aktivate")
        win.geometry("400x200")
        win.resizable(False, False)
        
        label1 = ttk.Label(win, text="Litsenziya olish uchun +998-99-772-33-28 nomer bilan bo'glaning.")
        label1.grid(column=0, row=0, columnspan=2)
        kod = tk.StringVar()
        et = ttk.Entry(win, width=40, textvariable=kod)
        et.grid(column=1, row=1)
        label2 = ttk.Label(win, text="Kodni kiriting: ")
        label2.grid(column=0, row=1)
        button1 = ttk.Button(win, text="OK", command=kod_)
        button1.grid(column=0, row=2)
        


    gui_main_funksiyasi()
