import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox as msg
from pathlib import Path

LUGAT = {
    ("homo", "inis", "m", "ot") : "odam",
    ("vesica", "ae", "f", "ot") : "pufak",
    ("fundus", "i", "m", "ot") : "tub",
    ("dorsum", "i", "n", "ot") : "orqa",
    ("auris","is","f","ot") : "quloq",
    ("bronchus","i","m","ot") : "bronx",
    ("coccyx","this","m","ot") : ("quyruq", "dum"),
    ("cerebrum","i","m","ot") : "katta miya",
    ("dens","dentis","m","ot") : "tish",
    ("ethmoidalis","e","sifat") : "g'alvirsimon",
    ("flos","floris","m","ot") : "gul", 
    ("gaster","tris","f","ot") : ("oshqozon", "me'da"), 
    ("humerus","i","m","ot") : "yelka suyagi", 
    ("ileum","i","n","ot") : "ichak", 
    ("jejunum","i","n","ot") : "ingichka ichak", 
    ("labium","ii","n","ot") : "lab",
    ("musculus","i","m","ot") : ("mushak", "muskul"), 
    ("nasus","i","m","ot") : "burun", 
    ("orbita","ae","f","ot") : "ko'z kosasi", 
    ("patella","ae","f","ot") : "tizza qopqog'i", 
    ("quadratus","a","um","ot") : "kvadrat", 
    ("ren","renis","m","ot") : "buyrak", 
    ("scapula","ae","f","ot") : "kurak", 
    ("thorax","acis","m","ot") : "ko'krak",
    ("unguis","is","m","ot") : "tirnoq", 
    ("vertebra","ae","f","ot") : "umurtqa", 
    ("larynx","yngis","m","ot") : "hiqildoq", 
    ("hyoideus","a","um","ot") : "til osti",
    ("zygoma","atis","n","ot") : ("yonoq", "bet suyagi"),
    ("keras","atos","ot") : "ko'z shox pardasi"
}


class Sozlamalar:

    def __init__(self):

        # GUI sozlamalari
        self.asosiy_oyna_nomi = " Lotin-O'zbek lug'ati"
        self.asosiy_oyna_balandligi = 300
        self.asosiy_oyna_kengligi = 400

        # Orqa fon sozlamalari.
        self.asosiy_oyna_orqa_fon_rangi = "#1B1C21"

        # O'zgarmaslar.

        ## Tomonlar.
        self.GARB = self.CHAP = "W"  # West
        self.SHARQ = self.ONG = "E"  # East
        self.SHIMOL = self.TEPA = "N"  # North
        self.JANUB = self.PAST = "S"  # South

        ## Aktivlik.
        self.NOFAOL = self.OCHIRILGAN = "disable"

        ## Ranglar.
        self.KOK = "Blue"
        self.OLTIN = "Gold"
        self.QIZIL = "Red"
        
        # tab 1 sozlamalari.
        self.tab_1_nomi = "Lotin -> O'zbek"
        self.tab_2_nomi = "O'zbek -> Lotin"
        

def lotinchadan_ozbekchaga(lotincha: str, lugat: dict):
    for key in lugat.keys():
        if key[0] == lotincha:
            return lugat[key]
    return 0

def ozbekchadan_lotinchaga(ozbekcha: str, lugat: dict):
    for key in lugat:
        ob = lugat[key]
        if type(ob) == str:
            if ozbekcha == lugat[key]:
                return key
        elif type(ob) == tuple:
            for i in ob:
                if ozbekcha == i:
                    return key
    return 0



from gui_kod import KOD


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

        # Style
        ## frame
        self.frame1_style1 = ttk.Style()
        self.frame1_style1.configure("BM.TFrame", background="#343A37")
        ## notebook
        self.notebook1_style1 = ttk.Style()
        self.notebook1_style1.configure("BM.TNotebook", background="#DAD8DC")
        ## labelframe
        self.label_frame1_style1 = ttk.Style()
        self.label_frame1_style1.configure("BM.TLabelframe", background="#DAD8DC")
        ## label
        self.label1_style1 = ttk.Style()
        self.label1_style1.configure("BW.TLabel", foreground="white", background="#15150F", textcollor="#000000")
        ## button
        self.button1_style1 = ttk.Style()
        self.button1_style1.configure("BW.TButton", background="#050503", foreground="black", collor="red")
        
        # Notebook
        ## notebook1
        self.notebook1 = ttk.Notebook(self.asosiy_oyna, padding=10, style="BM.TNotebook")
        
        # Frame
        ## frame1
        self.frame1 = ttk.Frame(self.notebook1, padding=10, style="BM.TFrame")
        self.notebook1.add(self.frame1, text=soz.tab_1_nomi)
        ## frame2
        self.frame2 = ttk.Frame(self.notebook1, padding=10, style="BM.TFrame")
        self.notebook1.add(self.frame2, text=soz.tab_2_nomi)

        self.notebook1.pack(expand=1, fill="both")

        # LabelFrame
        ## label_frame1
        self.label_frame1 = ttk.LabelFrame(self.frame1, style="BM.TLabelframe")
        self.label_frame1.grid(column=0, row=0, padx=10, pady=10)
        ## label_frame2
        self.label_frame2 = ttk.LabelFrame(self.frame2, style="BM.TLabelframe")
        self.label_frame2.grid(column=0, row=0, padx=10, pady=10)

        # Label
        ## label1
        self.label1 = ttk.Label(self.label_frame1, width=50, text="", style="BW.TLabel")
        self.label1.grid(column=0, row=2, padx=4, pady=4)
        ## label2
        self.label2 = ttk.Label(self.label_frame2, width=50, text="", style="BW.TLabel")
        self.label2.grid(column=0, row=2, padx=4, pady=4)

        # Button
        ## button1
        self.button1 = ttk.Button(self.label_frame1, text="OK", command=self.button1_command1, style="BW.TButton")
        self.button1.grid(column=0, row=1, padx=4, pady=4)
        ## button2
        self.button2 = ttk.Button(self.label_frame2, text="OK", command=self.button2_command1, style="BW.TButton")
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
        self.entry2 = ttk.Entry(self.label_frame2, width=50, textvariable=self.entry2_string_var1)
        self.entry2.grid(column=0, row=0)
        ### entry2-ga focus-ni o'ratish.
        self.entry2.focus()

        # Menu
        # Menyu qatori-ni yaratish.
        self.menyu_qatori = Menu(self.asosiy_oyna)
        self.asosiy_oyna.config(menu=self.menyu_qatori)
        
        # Menyu yaratish va Menyu elementlarini qo'shish.
        self.hujjat_menyu = Menu(self.menyu_qatori, tearoff=0)  # hujjat menyusini yaratish.
        self.hujjat_menyu.add_command(label="Aktivlashtirish", command=self._yangi_hujjat)  # Hujjat menyusiga element qo'shish.
        self.hujjat_menyu.add_separator()
        self.hujjat_menyu.add_command(label="Chiqish", command=self._chiqish)  # Hujjat menyusiga element qo'shish.
        self.menyu_qatori.add_cascade(label="Hujjat", menu=self.hujjat_menyu)
        
        self.yordam_menyu = Menu(self.menyu_qatori, tearoff=0)
        self.menyu_qatori.add_cascade(label="Yordam", menu=self.yordam_menyu)
        self.yordam_menyu.add_command(label="Haqida", command=self._msgBox)
 
    def button1_command1(self):
        if KOD:
            natija = lotinchadan_ozbekchaga(self.entry1_string_var1.get(), LUGAT)
            if natija == 0:
                natija = "Natija topilmadi!"
            self.label1.configure(text="{}".format(natija))
        else:
            msg.showinfo("Eslatma!", "Dasturdan foydalanish uchun 'Litsenziya' olish kerak.\n 'Litsenziya' olish uchun +998-99-772-33-28 nomer bilan yoki uzbekdasturchisiman@gmail.com pochta manzili bilan bo'glaning.")
        
        
    def button2_command1(self):
        if KOD:
            natija = ozbekchadan_lotinchaga(self.entry2_string_var1.get(), LUGAT)
            if natija == 0:
                natija = "Natija topilmadi!"
            self.label2.configure(text="{}".format(natija))
        else:
            msg.showinfo("Eslatma!", "Dasturdan foydalanish uchun 'Litsenziya' olish kerak.\n 'Litsenziya' olish uchun +998-99-772-33-28 nomer bilan yoki uzbekdasturchisiman@gmail.com pochta manzili bilan bo'glaning.")
        
    
    def _yangi_hujjat(self):
        kod1 = self.entry1_string_var1.get()
        kod2 = self.entry2_string_var1.get()
        try:
            x = int(kod1)
        except:
            pass
        else:
            if type(kod2) == str and type(int(kod1)) == int:
                x = Path(".")
                for i in x.iterdir():
                    if i.is_file() and i.name == "kod.txt":
                        with open(i, "w") as f:
                            f.write("lu$jsgfqpe83LFsuw*-ndvacys")
        
                    
    
    def _chiqish(self):
        self.asosiy_oyna.quit()
        self.asosiy_oyna.destroy()
        exit()
    
    def _msgBox(self):
        msg.showinfo("Lotin-O'zbek lug'ati ", " Dastur yaratuvchisi: Shodmonov Zafar\n 2023-yilda yaratildi.\n Elektron pochta: uzbekdasturchisiman@gmail.com \n Telefon nomer: +998-99-772-33-28\n Dastur versiyasi 1.0.0 \n")
        # msg.showwarning("Python Message Warning Box", "A Python GUI created using tkinter:\nWarning: There might be a bug in this code.")
        # msg.showerror("Python Message Error Box", "A Python GUI created using tkinter:\nError: Houston ~ we DO have a serius PROBLEM!")
        # answer = msg.askyesnocancel("Python Message Mul")
    
    def mainloop(self):
        self.asosiy_oyna.mainloop()


def gui_main_funksiyasi():
    my_gui = Gui()
    my_gui.mainloop()

if __name__ == "__main__":
    gui_main_funksiyasi()
