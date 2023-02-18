import tkinter as tk
import gui_funksiyalari as funk
from gui_sozlamalari import Sozlamalar
from lugat_modul import LUGAT
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as msg


soz = Sozlamalar()

class Gui():

    def __init__(self):
        
        # Asosiy oynani yaratish.
        self.asosiy_oyna = tk.Tk()

        # Asosiy oynaga nom berish.
        self.asosiy_oyna.title(soz.asosiy_oyna_nomi)

        # Asosiy oyna o'lchamini boshqarish.

        ## Asosiy oyna o'lchamini belgilash.
        self.asosiy_oyna.geometry("{0}x{1}".format(soz.asosiy_oyna_kengligi, soz.asosiy_oyna_balandligi))

        ## Asosiy oyna o'lchamini o'zgarmaydigan yoki o'zgaradigan qilish.
        self.asosiy_oyna.resizable(False, False)
        
        # Asosiy oyna sozlamalari.

        ## Asosiy oyna orqa fon rangini belgilash.
        self.asosiy_oyna.configure(bg=soz.asosiy_oyna_orqa_fon_rangi, padx=10, pady=10)
        self.KOD = None

        # Style
        ## frame
        self.frame1_style1 = ttk.Style()
        self.frame1_style1.configure("BM.TFrame", background="#343A37")
        ## notebook
        self.notebook1_style1 = ttk.Style()
        self.notebook1_style1.configure("BM.TNotebook", background="#DAD8DC")
        ## labelframe
        self.label_frame1_style1 = ttk.Style()
        self.label_frame1_style1.configure("BM.TLabel", background="#DAD8DC")
        ## label
        self.label1_style1 = ttk.Style()
        self.label1_style1.configure("BW.TLabel", foreground="white", background="#15150F", textcollor="#000000")
        ## button
        self.button1_style1 = ttk.Style()
        self.button1_style1.configure("BW.TButton", background="#050503", foreground="black", collor="red")
        
        # Notebook
        ## notebook1
        self.notebook1 = ttk.Notebook(self.asosiy_oyna, padding=10, label1_style1="BM.TNotebook")
        
        # Frame
        ## frame1
        self.frame1 = ttk.Frame(self.notebook1, padding=10, label1_style1="BM.TFrame")
        self.notebook1.add(self.frame1, text=soz.tab_1_nomi)
        ## frame2
        self.frame2 = ttk.Frame(self.notebook1, padding=10, label1_style1="BM.TFrame")
        self.notebook1.add(self.frame2, text=soz.tab_2_nomi)

        self.notebook1.pack(expand=1, fill="both")

        # LabelFrame
        ## label_frame1
        self.label_frame1 = ttk.LabelFrame(self.frame1, style="BM.TLabel")
        self.label_frame1.grid(column=0, row=0, padx=10, pady=10)
        ## label_frame2
        self.label_frame2 = ttk.LabelFrame(self.frame2, style="BM.TLabel")
        self.label_frame2.grid(column=0, row=0, padx=10, pady=10)

        # Label
        ## label1
        self.label1 = ttk.Label(self.label_frame1, width=50, text="", style="BW.TLabel")
        self.label1.grid(column=0, row=2, padx=4, pady=4)
        ## label2
        self.label2 = ttk.Label(self.label_frame1, width=50, text="", style="BW.TLabel")
        self.label2.grid(column=0, row=2, padx=4, pady=4)

        # Button
        ## button1
        self.button1 = ttk.Button(self.label_frame1, text="OK", command=self.button1_command1, style="BW.TButton")
        self.button1.grid(column=0, row=1, padx=4, pady=4)
        ## button2
        self.button2 = ttk.Button(self.label_frame11, text="OK", command=self.button2_command1, style="BW.TButton")
        self.button2.grid(column=0, row=1, padx=4, pady=4)
        
        # Entry
        ## entry1
        self.entry1_string_var1 = tk.StringVar()
        self.entry1 = ttk.Entry(self.label_frame1, width=50, textvariable=self.entry1_string_var1)
        self.entry1.grid(column=0, row=0)
        ### entry1-ga focus-ni o'ratish.
        self.entry1.focus()
        ## entry2
        self.entry2_string_var1 = tk.StringVar()
        self.entry2 = ttk.Entry(self.label_frame11, width=50, textvariable=self.entry2_string_var1)
        self.entry2.grid(column=0, row=0)
        ### entry2-ga focus-ni o'ratish.
        self.entry2.focus()
 
    def button1_command1(self):
        if self.KOD != None:
            natija = funk.lotinchadan_ozbekchaga(self.et_str.get(), LUGAT)
            if natija == 0:
                natija = "Natija topilmadi!"
            self.label1.configure(text="{}".format(natija))
        
    def button2_command1(self):
        natija = funk.ozbekchadan_lotinchaga(self.et2_str.get(), LUGAT)
        if natija == 0:
            natija = "Natija topilmadi!"
        self.label11.configure(text="{}".format(natija))
    
    def kod_(self):
        self.KOD = self.kod
        self.yangi_hujjat_oynasi.destroy()

    def _yangi_hujjat(self):
        self.yangi_hujjat_oynasi = tk.Tk()
        self.yangi_hujjat_oynasi.title("Aktivlashtirish")
        self.yangi_hujjat_oynasi.geometry("400x200")
        self.yangi_hujjat_oynasi.resizable(False, False)
        label1 = ttk.Label(self.yangi_hujjat_oynasi, text="Litsenziya olish uchun +998-99-772-33-28 nomer bilan bo'glaning.")
        label1.grid(column=0, row=0, columnspan=2)
        self.kod = tk.StringVar()
        et = ttk.Entry(self.yangi_hujjat_oynasi, width=40, textvariable=self.kod)
        et.grid(column=1, row=1)
        label2 = ttk.Label(self.yangi_hujjat_oynasi, text="Kodni kiriting: ")
        label2.grid(column=0, row=1)
        button1 = ttk.Button(self.yangi_hujjat_oynasi, text="OK", command=self.kod_)
        button1.grid(column=0, row=2)
        
        # ## 1-scrolledtext.
        # self.a = tk.WORD
        # self.st1 = scrolledtext.ScrolledText(self.yangi_hujjat_oynasi, width=70, height=34, wrap=self.a)
        # self.st1.grid(column=0, columnspan=3, padx=20, pady=20)
        
        # self.yangi_hujjat_oynasi.mainloop()
        pass
    
    def _chiqish(self):
        self.asosiy_oyna.quit()
        self.asosiy_oyna.destroy()
        exit()
    
    def _msgBox(self):
        msg.showinfo("Lotin vs O'zbek lug'ati ", "Dastur yaratuvchisi: Shodmonov Zafar\n 2023-yilda yaratildi.\n Telefon nomer: +998-99-772-33-28")
        # msg.showwarning("Python Message Warning Box", "A Python GUI created using tkinter:\nWarning: There might be a bug in this code.")
        # msg.showerror("Python Message Error Box", "A Python GUI created using tkinter:\nError: Houston ~ we DO have a serius PROBLEM!")
        # answer = msg.askyesnocancel("Python Message Mul")
    
    def menyu_qatori(self):
        """____"""
        
        # Menyu qatori-ni yaratish.
        self.menyu_qatori = Menu(self.asosiy_oyna)
        self.asosiy_oyna.config(menu=self.menyu_qatori)
        
        # Menyu yaratish va Menyu elementlarini qo'shish.
        self.hujjat_menyu = Menu(self.menyu_qatori, tearoff=0)  # hujjat menyusini yaratish.
        self.hujjat_menyu.add_command(label="Yangi", command=self._yangi_hujjat)  # Hujjat menyusiga element qo'shish.
        self.hujjat_menyu.add_separator()
        self.hujjat_menyu.add_command(label="Chiqish", command=self._chiqish)  # Hujjat menyusiga element qo'shish.
        self.menyu_qatori.add_cascade(label="Hujjat", menu=self.hujjat_menyu)
        
        self.yordam_menyu = Menu(self.menyu_qatori, tearoff=0)
        self.menyu_qatori.add_cascade(label="Yordam", menu=self.yordam_menyu)
        self.yordam_menyu.add_command(label="Haqida", command=self._msgBox)

    def mainloop(self):
        self.asosiy_oyna.mainloop()

        

        
