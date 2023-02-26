import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox as msg
from pathlib import Path

KOD = False
path_to_the_text_file = Path(".")
for i in path_to_the_text_file.iterdir():
    if i.is_file() and i.name == "file_to_activate_the_program.txt":
        with open(i, "r") as f:
            d = f.read()
            if d == "":
                KOD = False
            else:
                KOD = True

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
    ("labium","i","n","ot") : "lab",
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
    ("keras","atos","ot") : "ko'z shox pardasi",
    ("vertebra","ae","f","ot") : "umurtqa",
    ("cranium","i","n","ot"):"kalla suyagi",
    ("pectus","oris","n","ot"):"ko'krak",
    ("palma","aris","m","ot"):"kaft",
    ("fibula","ae","f","ot"):"kichik boldir suyagi",
    ("tibia","ae","f","ot"):"katta boldir suyagi",
    ("planta","ae","f","ot"):"oyoq tagi",
    ("nasus","i","m","ot"):" burun",
    ("costa","ae","f","ot"):"qovurg'a",
    ("dorsum","i","m","ot"):"orqa",
    ("femor","oris","n","ot"):"son suyagi",
    ("pulmo","onis","m","ot"):"o'pka",
    ("cerebrum","i","n","ot"):"katta miya",
    ("arcus","us","m","ot"):"yoy",
    ("cornu","us","n","ot"):"shox",
    ("processus","us","m","ot"):"o'simta",
    ("genu","us","n","ot"):"tizza",
    ("manus","us","f","ot"):"qo'l panjasi",
    ("facies","ei","f","ot"):"yuza",
    ("superficies","ei","f","ot"):"yuza",
    ("auditus","us","m","ot"):"eshituv",
    ("incus","udus","f","ot"):"sandom",
    ("visus","us","m","ot"):"ko'rish",
    ("senectus","utis","f","ot"):"qarilik",
    ("esophagus","i","m","ot"):"qizilo'ngach",
    ("ulcus","eris","n","ot"):"yara",
    ("processus","us","m","ot"):"o'simta",
    ("viscus","eris","n","ot"):"ichki a'zo",
    ("abscessus","us","m","ot"):"yorilishi",
    ("aditus","us","m","ot"):"kirish",
    ("exitus","us","m","ot"):"natija",
    ("casus","us","m","ot"):"voqea",
    ("habitus","us","m","ot"):"tashqi ko'rinish",
    ("hiatus","us","m","ot"):("yoriq","teshik"),
    ("pulsus","us","m","ot"):"puls",
    ("usus","us","m","ot"):"qo'llanish",
    ("collapsus","us","m","ot"):"yurakning o'tkir yetishmovchiligi",
    ("istus","us","m","ot"):("itarish","turtish"),
    ("caries","ei","f","ot"):"chirishlik",
    ("scabies","ei","f","ot"):"qo'tir",
    ("rabies","ai","f","ot"):"qutirish",
    ("species","ei","f","ot"):("yig'ma","to'plam"),
    ("acidum","i","n","ot"):"kislota",
    ("achillea","ae","f","ot"):"bo'ymadron", 
    ("acorus(i) colamus(i)","ot"):"oddiy igir", 
    ("acyclidinum","i","n","ot"):"atsiklidin", 
    ("adeps","ipis","m","ot"):"yog'", 
    ("addo","ere","3","fe'l"):"qo'shmoq", 
    ("adonis","idis","m","ot"):"adonis(gulizardak, safsargul)", 
    ("adonis(idis) vernalis(is)","ravish"):"bahorgi", 
    ("aethacridinum","i","n","ot"):"etakridin", 
    ("aethamidum","i","n","ot"):"etamid", 
    ("aethimizolum","i","n","ot"):"etimizol", 
    ("aethinyloestradiolum","i","n","ot"):"etinilestradiyol",
    ("aether","eris","m","ot"):"efir", 
    ("aethereus","a","um","ot"):"efir(moyli)li", 
    ("aethylicus","a","um","ot"):"etil(spirti)li", 
    ("aethylium","i","n","ot"):"etil", 
    ("alcaloidum","i","n","ot"):"yomtoq", 
    ("allium(i) sativum(i)"):"sarimsoq piyoz", 
    (" allocholum","i","n","ot"):"alloxol", 
    ("alnus","i","f","ot"):"qandag'och, olxa", 
    ("althaea","ea","f"):"gulxayri", 
    ("amidopyrinum","i","n","ot"):"amidopirin", 
    ("aminalonum","i","n","ot"):"aminalon", 
    ("aminalonum","i","n","ot"):"aminazin",
    ("ammoniates","a","um","sifat"):"ammiakli", 
    ("ampulla","ar","f","ot"):"ampula",
    ("amygdala","ar","f","ot"):"bodom", 
    ("amylaceus","a","um","sifat"):"kraxmalli", 
    ("amylum","I","n","ot"):"kraxmal", 
    ("ana"):"teng, teng miqdorda", 
    ("anaesthesinum","i","n","ot"):"anestezin", 
    ("anaesthetics","a","um"):"og'riqsizlantiruvchi", 
    ("anabasis","ahpylla","ot"):"maymunjon", 
    ("anethum","i","n","ot"):"shivit", 
    ("anisum","i","n","ot"):"arpabodiyon, oddiy Anis", 
    ("antiasthmaticus","a","um","ot"):"ich ketishiga qarshi", 
    ("aloё","ё","f"):"alloy",
    ("antidotum","i","n","ot"):"zaharga qarshi dori", 
    ("antigangraenosus","a","um","ot"):"gangrenaga qarshi", 
    ("antihaemorrhoidalis","e","ot"):"bevoailga qarshi", 
    ("antipestosus","a","um","ot"):"o'latga qarshi", 
    ("antipyreticus","a","um","ot"):"issiqni pasaytiruvchi", 
    ("antirabicus","a","um","ot"):"quturushga qarshi", 
    ("antisepticus","a","um","ot"):"antiseptik", 
    ("antitetanicus","a","um","ot"):"qoqsholga qarshi",
    ("apomorphinum","i","n","ot"):"apomorfin", 
    ("aprenalum","i","n","ot"):"aprenol", 
    ("apressinum","i","n","ot"):"apressin", 
    ("aprophenum","i","n","ot"):"apofen", 
    ("arctium","i","n","sifat"):"qariqiz", 
    ("arachis","idis","f","ot"):"yeryong'oq", 
    ("aralia","ae","f","ot"):"araliya",
    ("argentum","i","n","ot"):"kumush", 
    ("armeniaca","ae","f","ot"):"o'rik", 
    ("aromaticus","a","um","ot"):"xushbo'y", 
    ("arsenicum","i","n","ot"):"margumush",
    ("aurum","i","n","ot"):"oltin", 
    ("audio","ire","4","fe'l"):"eshitmoq",
    ('chole','es',"f","ot"):"o't",
    ("ala","ae","f","ot"):"qanot",
    ("aorta","ae","f","ot"):"aorta", 
    ("arteria","ae","f","ot"):"arteriya", 
    ("concha","ae","f","ot"):"chig'anoq", 
    ("costa","ae","f","ot"):"qovurg'a", 
    ("orbita","ae","f","ot"):"ko'z kosasi", 
    ("scapula","ae","f","ot"):"kurak", 
    ("spina","ae","f","ot"):"o'tkir qirra", 
    ("vena","ae","f","ot"):"vena", 
    ("crista","ae","f","ot"):"qirra", 
    ("lamina","ae","f","ot"):"plastinka", 
    ("lingua","ae","f","ot"):"til", 
    ("mandibula","ae","f","ot"):"pastki jag'", 
    ("maxilla","ae","f","ot"):"yuqori jag'", 
    ("patella","ae","f","ot"):"tizza qopqog'i", 
    ("sutura","ae","f","ot"):"chok", 
    ("tuba","ae","f","ot"):"nay", 
    ("vertebra","ae","f","ot"):"umurtqa",
    ("clavicula","ae","f","ot"):("o'mrov","o'mrov suyagi"),
    ("fascia","ae","f","ot"):"mushakni o'rab turuvchi yupqa parda",
    ("nucha","ae","f","ot"):"ensa",
    ("tibia","ae","f","ot"):"katta boldir suyagi",
    ("tonsilla","ae","ot"):"bodomcha",
    ("fibula","ae","f","ot"):"kichik boldir suyagi",
    ("squama","ae","f","ot"):"tangacha",
    ("ulna","ae","f","ot"):"tirsak suyagi",
    ("nasus","i","m","ot"):"burun",
    ("vestibulum","i","n","ot"):"dahliz",
    ("porus","i","m","ot"):"teshik",
    ("palatum","i","n","ot"):"tanglay",
    ("organum","i","n","ot") : ( "organ", "a'zo"),
    ("caput","itis","n","ot"):"bosh",
    ("os","oris","n","ot"):"og'iz",
    ("pterygoideus","a","um","sifat"):"qanotsimon",
    ("venosus","a","um","sifat"):"veno qon tomiriga oid",
    ("asper","a","um","sifat"):"g'adir-budur",
    ("iliacus","a","um","sifat"):("yonbosh","ichakka","oid"),
    ("niger","gra","grum","sifat"):"qora",
    ("thyr(e)","oideus","a","um","sifat"):"qalqonsimon",
    ("albus","a","um","sifat"):"oq",
    ("coronarius","a","um","sifat"):"tojsimon",
    ("liber","era","erum","sifat"):("erkin","ozod"),
    ("sacer","cra","crum","sifat"):"dumg'azaga oid",
    ("durus","a","um","sifat"):"qattiq",
    ("mylohyoideus","a","um","sifat"):"jag' til ostiga tegishli",
    ("massetericus","a","um","sifat"):"chaynovga oid",
    ("palatoglossus","a","um","sifat"):("tanglay","tilga oid"),
    ("alaris","e","sifat"):("qanotga","oid"),
    ("cervicalis","e","sifat"):"bo'yinga oid",
    ("frontalis","e","sifat"):"peshonaga oid",
    ("mandibularis","e","sifat"):"pastki jag'ga oid",
    ("occipitalis","e","sifat"):"ensaga oid",
    ("sphenoidalis","e","sifat"):"ponasimon",
    ("vertebralis","e","sifat"):"umurtqaga oid",
    ("sacralis","e","sifat"):"dumg'azaga oid",
    ("cerebralis","e","sifat"):"miyaga oid",
    ("ethmoidalis","e","sifat"):"g'alvirsimon",
    ("maxillaris","e","sifat"):"yuqori jag'ga oid",
    ("nasalis","e","sifat"):"burunga oid",
    ("orbitalis","e","sifat"):"ko'z kosasiga oid",
    ("temporalis","e","sifat"):"chakkaga oid",
    ("jugularis","e","sifat"):"bo'yinturuq",
    ("alveolaris","e","sifat"):("alveolangan","katakli","pufakli"),
    ("dentalis","e","sifat"):"tishga oid",
    ("mentalis","e","sifat"):"engakka oid",
    ("buccalis","e","sifat"):"lunju",
    ("infraorbitalis","e","sifat"):"ko'z kosasi ostiga oid",
    ("mollis","e","sifat"):"yumshoq",
    ("bacca","ae","f","ot"):("meva", "o'simlik"),
    ("barba","ae","f","ot"):"saqol", 
    ("basis","is","f","ot"):"asos", 
    ("bene","sifat"):"yaxshi", 
    ("biliaris","e","ot"):"o'tga oid", 
    ("bilifer","era","erum","ot"):"o'tga oid", 
    ("biliosus","a","um","ot"):"o't moddasiga boy", 
    ("bivalens","entis","sifat"):"ikki valentli", 
    ("biventer","tra","trum","sifat"):"ikki qorinli", 
    ("bolus","i","f","ot"):"qum", 
    ("bonum","i","n","sifat"):"yaxshilik", 
    ("bonus","a","um","sifat"):"yaxshi", 
    ("boricus","a","um","ot"):"borotga oid", 
    ("brachium","i","n","ot"):"yelka", 
    ("brevis","e","sifat"):"qisqa", 
    ("bronchialis","e","ot"):"bronxga tegishli", 
    ("bronchus","i","m","ot"):"bronx", 
    ("bucca","ae","f","sifat"):"lunj", 
    ("buccalis","e","sifat"):"lunji(si)", 
    ("bulbus","i","m","ot"):"soqqa, piyoz boshi", 
    ("bulbus oculli","ot"):"ko'z soqqasi", 
    ("bulla","ae","f","ot"):"pufakchaga", 
    ("bursa","ae","f","ot"):("sumka", "xalta") 
}



class Sozlamalar:

    def __init__(self):

        # GUI sozlamalari
        self.asosiy_oyna_nomi = " Lotin-O'zbek lug'ati"
        self.asosiy_oyna_balandligi = 300
        self.asosiy_oyna_kengligi = 370

        # Orqa fon sozlamalari.
        self.asosiy_oyna_orqa_fon_rangi = "#32E424"  #"#1B1C21"

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
        
        # frame-lar sozlamalari.
        self.frame1_nomi = "Lotin -> O'zbek"
        self.frame2_nomi = "O'zbek -> Lotin"
        

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
        self.frame1_style1.configure("BM.TFrame", background="#CF4AC6")
        ## notebook
        self.notebook1_style1 = ttk.Style()
        self.notebook1_style1.configure("BM.TNotebook", background="#32E4ED") #"#343A37"
        ## label
        self.label1_style1 = ttk.Style()
        self.label1_style1.configure("BW.TLabel", foreground="black", background="#ffffff", textcollor="#000000")
        ## button
        self.button1_style1 = ttk.Style()
        self.button1_style1.configure("BW.TButton", background="#050503", foreground="black")
        
        # Notebook
        ## notebook1
        self.notebook1 = ttk.Notebook(self.asosiy_oyna, padding=10, style="BM.TNotebook")
        
        # Frame
        ## frame1
        self.frame1 = ttk.Frame(self.notebook1, padding=10, style="BM.TFrame")
        self.notebook1.add(self.frame1, text=soz.frame1_nomi)
        ## frame2
        self.frame2 = ttk.Frame(self.notebook1, padding=10, style="BM.TFrame")
        self.notebook1.add(self.frame2, text=soz.frame2_nomi)
        self.notebook1.pack(expand=1, fill="both")

        # Label
        ## label1
        self.label1 = ttk.Label(self.frame1, width=50, text="", style="BW.TLabel")
        self.label1.grid(column=0, row=2, columnspan=2, padx=4, pady=4)
        ## label1
        self.label2 = ttk.Label(self.frame2, width=50, text="", style="BW.TLabel")
        self.label2.grid(column=0, row=2, columnspan=2, padx=4, pady=4)
  
        # Button
        ## button1
        self.button1 = ttk.Button(self.frame1, text="OK", command=self.button1_command1, style="BW.TButton")
        self.button1.grid(column=0, row=3, columnspan=2, padx=4, pady=4, sticky="W")
        ## button2
        self.button2 = ttk.Button(self.frame2, text="OK", command=self.button2_command1, style="BW.TButton")
        self.button2.grid(column=0, row=3, columnspan=2, padx=4, pady=4, sticky="W")
   
        # Entry
        ## entry1
        self.entry1_string_var1 = tk.StringVar()
        self.entry1 = ttk.Entry(self.frame1, width=50, textvariable=self.entry1_string_var1)
        self.entry1.grid(column=0, row=1, columnspan=2)
        ### entry1-ga focus-ni o'ratish.
        self.entry1.focus()
        ## entry2
        self.entry2_string_var1 = tk.StringVar()
        self.entry2 = ttk.Entry(self.frame2, width=50, textvariable=self.entry2_string_var1)
        self.entry2.grid(column=0, row=1, columnspan=2)
        ### entry2-ga focus-ni o'ratish.
        self.entry2.focus()
     
        # Radiobutton
        self.radiobutton_var = tk.IntVar()
        ## radiobutton1
        self.radiobutton1 = tk.Radiobutton(self.frame1, text="Anatomik Terminlar", foreground="#322424",activebackground="#4BF23A", background="#CF4AC6", variable=self.radiobutton_var, value=1, command=self.radiobutton_command1)
        self.radiobutton1.grid(column=0, row=4, sticky="W")
        ## radiobutton2
        self.radiobutton2 = tk.Radiobutton(self.frame1, text="Klinik Terminlar",foreground="#322424",activebackground="#4BF23A", background="#CF4AC6", variable=self.radiobutton_var, value=2, command=self.radiobutton_command1)
        self.radiobutton2.grid(column=0, row=5, sticky="W")
        ## radiobutton3
        self.radiobutton3 = tk.Radiobutton(self.frame1, text="Farmatsevtik Terminlar", foreground="#322424",activebackground="#4BF23A",background="#CF4AC6", variable=self.radiobutton_var, value=3, command=self.radiobutton_command1)
        self.radiobutton3.grid(column=0, row=6, sticky="W")
        ## radiobutton4
        self.radiobutton4 = tk.Radiobutton(self.frame1, text="Anotomik Terminlar",foreground="#322424", activebackground="#4BF23A",background="#CF4AC6", variable=self.radiobutton_var, value=4, command=self.radiobutton_command1)
        self.radiobutton4.grid(column=0, row=7, sticky="W")

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
 
    def radiobutton_command1(self):
        x = self.radiobutton_var.get()
        if x == 1:
            pass
        elif x == 2:
            pass
        elif x == 3:
            pass
        elif x == 4:
            pass
        else:
            pass

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
            if type(kod2) == str and type(int(kod1)) == int and self.radiobutton_var.get() == 4:
                path_to_the_text_file2 = "./file_to_activate_the_program.txt"
                with open(path_to_the_text_file2, "w") as text_file2:
                    text_file2.write("{}{}".format(kod2, kod1))
            
                  
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
