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
    """____"""

    def __init__(self):
        """_____"""
        
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
        self.asosiy_oyna.configure(bg=soz.asosiy_oyna_orqa_fon_rangi)
        self.KOD = None

    def tab_control(self):
        """____"""
        
        # 1-notebook.
        self.tab_control = ttk.Notebook(self.asosiy_oyna)  # Create Tab Control.
        
        # 1-tab.
        self.tab1 = ttk.Frame(self.tab_control)  # Create a tab.
        self.tab_control.add(self.tab1, text=soz.tab_1_nomi)  # Add the tab.
        
        # 2-tab.
        self.tab2 = ttk.Frame(self.tab_control)  # Create a tab.
        self.tab_control.add(self.tab2, text=soz.tab_2_nomi)  # Add the tab.
        
        self.tab_control.pack(expand=1, fill="both")
    
    def mighty(self):
        """"____"""
        
        # 1-mighty.
        self.mg = ttk.LabelFrame(self.tab1, text=" Lotin -> O'zbek ")
        self.mg.grid(column=0, row=0, padx=10, pady=10)
        
        self.mg1 = ttk.LabelFrame(self.tab2, text=" O'zbek -> Lotin ")
        self.mg1.grid(column=0, row=0, padx=10, pady=10)
    
    
    def widjetlar(self):
        """_______"""

        # 1-widjet turi: Label.

        ## 1-label.
        self.style = ttk.Style()
        self.style.configure("BW.TLabel", foreground="white", background="#123456", textcollor="#000000")
        self.lb = ttk.Label(self.mg, width=40, text="", style="BW.TLabel")
        self.lb.grid(column=0, row=2, padx=4, pady=4)
        
        ## 2-label.
        self.style1 = ttk.Style()
        self.style1.configure("BW.TLabel", foreground="white", background="#123456", textcollor="#000000")
        self.lb1 = ttk.Label(self.mg1, width=40, text="", style="BW.TLabel")
        self.lb1.grid(column=0, row=2, padx=4, pady=4)


        # 2-widjet turi: Button.
        
        ## 1-button.
        self.bt1_style = ttk.Style()
        self.bt1_style.configure("BW.TButton", background="red", foreground="blue", collor="red")
        self.bt = ttk.Button(self.mg, text="OK", command=self.bt_funk, style="BW.TButton")
        self.bt.grid(column=0, row=1, padx=4, pady=4)
        
        ## 2-button.
        self.bt2 = ttk.Button(self.mg1, text="OK", command=self.bt2_funk)
        self.bt2.grid(column=0, row=1, padx=4, pady=4)
        
        # 3-widjet turi: Entry.

        ## 1-entry.
        self.et_str = tk.StringVar()
        self.et = ttk.Entry(self.mg, width=40, textvariable=self.et_str)
        self.et.grid(column=0, row=0)
        
        ### 1-entry-ga focus-ni o'ratish.
        self.et.focus()
        
        ## 2-entry.
        self.et2_str = tk.StringVar()
        self.et2 = ttk.Entry(self.mg1, width=40, textvariable=self.et2_str)
        self.et2.grid(column=0, row=0)
        
        ### 1-entry-ga focus-ni o'ratish.
        self.et2.focus()

        # 4-widjet turi: Combobox.

        ## 1-combobox.
        # self.cb_str = tk.StringVar()
        # self.cb = ttk.Combobox(self.mg, width=12, textvariable=self.cb_str)
        # self.cb["values"] = (1996, 1997, 1998, 1999, 2000)
        # self.cb.grid(column=0, row=1)
        # self.cb.current(0)

        ## 2-combobox.
        # self.cb1_str = tk.StringVar()
        # self.cb1 = ttk.Combobox(self.mg, width=12, textvariable=self.cb1_str, state="readonly")
        # self.cb1["values"] = (1996, 1997, 1998, 1999, 2000)
        # self.cb1.grid(column=1, row=1)
        # self.cb1.current(0)

        # 5-widjet turi: Checkbutton.

        ## 1-checkbutton.
        # self.ch_var = tk.IntVar()
        # self.ch = tk.Checkbutton(self.mg, text="Nofaol", variable=self.ch_var, state=soz.NOFAOL)
        # self.ch.select()
        # self.ch.grid(column=0, row=3, sticky=soz.CHAP)

        ## 2-checkbutton.
        # self.ch1_var = tk.IntVar()
        # self.ch1 = tk.Checkbutton(self.mg, text="Belgilanmagan", variable=self.ch1_var)
        # self.ch1.deselect()
        # self.ch1.grid(column=1, row=3, sticky=soz.CHAP)

        ## 3-checkbutton.
        # self.ch2_var = tk.IntVar()
        # self.ch2 = tk.Checkbutton(self.mg, text="Faol", variable=self.ch2_var)
        # self.ch2.select()
        # self.ch2.grid(column=2, row=3, sticky=soz.ONG)

        # 6-widjet turi: Radiobutton.

        ## 1-radiobutton.
        # self.rb_var = tk.IntVar()
        # self.rb = tk.Radiobutton(self.mg, text="Ko'k", variable=self.rb_var, value=1, command=self.rb_funk)
        # self.rb.grid(column=0, row=5, sticky=soz.CHAP, columnspan=3)

        ## 2-radiobutton.
        # self.rb2 = tk.Radiobutton(self.mg, text="Oltin", variable=self.rb_var, value=2, command=self.rb_funk)
        # self.rb2.grid(column=1, row=5, sticky=soz.CHAP, columnspan=3)

        # ## 3-radiobutton.
        # self.rb3 = tk.Radiobutton(self.mg, text="Qizil", variable=self.rb_var, value=3, command=self.rb_funk)
        # self.rb3.grid(column=2, row=5, sticky=soz.CHAP, columnspan=3)

        # 7-widjet turi: ScrolledText.

        ## 1-scrolledtext.
        # self.a = tk.WORD
        # self.st = scrolledtext.ScrolledText(self.mg, width=30, height=3, wrap=self.a)
        # self.st.grid(column=0, columnspan=3)
        
    # widjetlar bilan bo'g'lanadigan funksiyalar.

    ## 1, 2, 3 -radiobutton bilan bog'landigan funksiya.
    # def rb_funk(self):
    #     x = self.rb_var.get()
    #     if x == 1:
    #         self.asosiy_oyna.configure(bg=soz.KOK)
    #     elif x == 2:
    #         self.asosiy_oyna.configure(bg=soz.OLTIN)
    #     elif x == 3:
    #         self.asosiy_oyna.configure(bg=soz.QIZIL)

    ## 1-button bilan bog'lanadigan funksiya.
    def bt_funk(self):
        if self.KOD != None:
            natija = funk.lotinchadan_ozbekchaga(self.et_str.get(), LUGAT)
            if natija == 0:
                natija = "Natija topilmadi!"
            self.lb.configure(text="{}".format(natija))
        
    def bt2_funk(self):
        natija = funk.ozbekchadan_lotinchaga(self.et2_str.get(), LUGAT)
        if natija == 0:
            natija = "Natija topilmadi!"
        self.lb1.configure(text="{}".format(natija))
    
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

        

        
