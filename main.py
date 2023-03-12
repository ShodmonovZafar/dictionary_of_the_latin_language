import json
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as msg
from pathlib import Path


# functions
def ozbek_lotin(my_list: list, s: str, lotin=False) -> dict or int:
    if lotin:
        for item in my_list:
            for j in item["lotincha"]:
                if s == j:
                    return item
        return 0
    for item in my_list:
        for j in item["o'zbekcha"]:
            if s == j:
                return item
    return 0

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

ot = """[
  {
    "gen": "inis",
    "lotincha": [
      "homo"
    ],
    "o'zbekcha": [
      "odam"
    ],
    "rod": "m"
  },
  {
    "gen": "ae",
    "lotincha": [
      "vesica"
    ],
    "o'zbekcha": [
      "pufak"
    ],
    "rod": "f"
  },
  {
    "gen": "i",
    "lotincha": [
      "fundus"
    ],
    "o'zbekcha": [
      "tub"
    ],
    "rod": "m"
  },
  {
    "gen": "i",
    "lotincha": [
      "dorsum"
    ],
    "o'zbekcha": [
      "orqa"
    ],
    "rod": "n"
  },
  {
    "gen": "is",
    "lotincha": [
      "auris"
    ],
    "o'zbekcha": [
      "quloq"
    ],
    "rod": "f"
  },
  {
    "gen": "i",
    "lotincha": [
      "bronchus"
    ],
    "o'zbekcha": [
      "bronx"
    ],
    "rod": "m"
  },
  {
    "gen": "this",
    "lotincha": [
      "coccyx"
    ],
    "o'zbekcha": [
      "quyruq",
      "dum"
    ],
    "rod": "m"
  },
  {
    "gen": "i",
    "lotincha": [
      "cerebrum"
    ],
    "o'zbekcha": [
      "katta miya"
    ],
    "rod": "m"
  },
  {
    "gen": "dentis",
    "lotincha": [
      "dens"
    ],
    "o'zbekcha": [
      "tish"
    ],
    "rod": "m"
  },
  {
    "gen": "floris",
    "lotincha": [
      "flos"
    ],
    "o'zbekcha": [
      "gul"
    ],
    "rod": "m"
  },
  {
    "gen": "tris",
    "lotincha": [
      "gaster"
    ],
    "o'zbekcha": [
      "oshqozon",
      "me'da"
    ],
    "rod": "f"
  },
  {
    "gen": "i",
    "lotincha": [
      "humerus"
    ],
    "o'zbekcha": [
      "yelka suyagi"
    ],
    "rod": "m"
  },
  {
    "gen": "i",
    "lotincha": [
      "ileum"
    ],
    "o'zbekcha": [
      "ichak"
    ],
    "rod": "n"
  },
  {
    "gen": "i",
    "lotincha": [
      "jejunum"
    ],
    "o'zbekcha": [
      "ingichka ichak"
    ],
    "rod": "n"
  },
  {
    "gen": "i",
    "lotincha": [
      "labium"
    ],
    "o'zbekcha": [
      "lab"
    ],
    "rod": "n"
  },
  {
    "gen": "i",
    "lotincha": [
      "musculus"
    ],
    "o'zbekcha": [
      "mushak",
      "muskul"
    ],
    "rod": "m"
  },
  {
    "gen": "i",
    "lotincha": [
      "nasus"
    ],
    "o'zbekcha": [
      "burun"
    ],
    "rod": "m"
  },
  {
    "gen": "ae",
    "lotincha": [
      "orbita"
    ],
    "o'zbekcha": [
      "ko'z kosasi"
    ],
    "rod": "f"
  },
  {
    "gen": "ae",
    "lotincha": [
      "patella"
    ],
    "o'zbekcha": [
      "tizza qopqog'i"
    ],
    "rod": "f"
  },
  {
    "gen": "a",
    "lotincha": [
      "quadratus"
    ],
    "o'zbekcha": [
      "kvadrat"
    ],
    "rod": "um"
  },
  {
    "gen": "renis",
    "lotincha": [
      "ren"
    ],
    "o'zbekcha": [
      "buyrak"
    ],
    "rod": "m"
  },
  {
    "gen": "ae",
    "lotincha": [
      "scapula"
    ],
    "o'zbekcha": [
      "kurak"
    ],
    "rod": "f"
  },
  {
    "gen": "acis",
    "lotincha": [
      "thorax"
    ],
    "o'zbekcha": [
      "ko'krak"
    ],
    "rod": "m"
  },
  {
    "gen": "is",
    "lotincha": [
      "unguis"
    ],
    "o'zbekcha": [
      "tirnoq"
    ],
    "rod": "m"
  },
  {
    "gen": "ae",
    "lotincha": [
      "vertebra"
    ],
    "o'zbekcha": [
      "umurtqa"
    ],
    "rod": "f"
  },
  {
    "gen": "yngis",
    "lotincha": [
      "larynx"
    ],
    "o'zbekcha": [
      "hiqildoq"
    ],
    "rod": "m"
  },
  {
    "gen": "a",
    "lotincha": [
      "hyoideus"
    ],
    "o'zbekcha": [
      "til osti"
    ],
    "rod": "um"
  },
  {
    "gen": "atis",
    "lotincha": [
      "zygoma"
    ],
    "o'zbekcha": [
      "yonoq",
      "bet suyagi"
    ],
    "rod": "n"
  },
  {
    "gen": "atos",
    "lotincha": [
      "keras"
    ],
    "o'zbekcha": [
      "ko'z shox pardasi"
    ],
    "rod": "ot"
  },
  {
    "gen": "i",
    "lotincha": [
      "cranium"
    ],
    "o'zbekcha": [
      "kalla suyagi"
    ],
    "rod": "n"
  },
  {
    "gen": "oris",
    "lotincha": [
      "pectus"
    ],
    "o'zbekcha": [
      "ko'krak"
    ],
    "rod": "n"
  },
  {
    "gen": "aris",
    "lotincha": [
      "palma"
    ],
    "o'zbekcha": [
      "kaft"
    ],
    "rod": "m"
  },
  {
    "gen": "ae",
    "lotincha": [
      "fibula"
    ],
    "o'zbekcha": [
      "kichik boldir suyagi"
    ],
    "rod": "f"
  },
  {
    "gen": "ae",
    "lotincha": [
      "tibia"
    ],
    "o'zbekcha": [
      "katta boldir suyagi"
    ],
    "rod": "f"
  },
  {
    "gen": "ae",
    "lotincha": [
      "planta"
    ],
    "o'zbekcha": [
      "oyoq tagi"
    ],
    "rod": "f"
  },
  {
    "gen": "ae",
    "lotincha": [
      "costa"
    ],
    "o'zbekcha": [
      "qovurg'a"
    ],
    "rod": "f"
  },
  {
    "gen": "i",
    "lotincha": [
      "dorsum"
    ],
    "o'zbekcha": [
      "orqa"
    ],
    "rod": "m"
  },
  {
    "gen": "oris",
    "lotincha": [
      "femor"
    ],
    "o'zbekcha": [
      "son suyagi"
    ],
    "rod": "n"
  },
  {
    "gen": "onis",
    "lotincha": [
      "pulmo"
    ],
    "o'zbekcha": [
      "o'pka"
    ],
    "rod": "m"
  },
  {
    "gen": "i",
    "lotincha": [
      "cerebrum"
    ],
    "o'zbekcha": [
      "katta miya"
    ],
    "rod": "n"
  },
  {
    "gen": "us",
    "lotincha": [
      "arcus"
    ],
    "o'zbekcha": [
      "yoy"
    ],
    "rod": "m"
  },
  {
    "gen": "us",
    "lotincha": [
      "cornu"
    ],
    "o'zbekcha": [
      "shox"
    ],
    "rod": "n"
  },
  {
    "gen": "us",
    "lotincha": [
      "processus"
    ],
    "o'zbekcha": [
      "o'simta"
    ],
    "rod": "m"
  },
  {
    "gen": "us",
    "lotincha": [
      "genu"
    ],
    "o'zbekcha": [
      "tizza"
    ],
    "rod": "n"
  },
  {
    "gen": "us",
    "lotincha": [
      "manus"
    ],
    "o'zbekcha": [
      "qo'l panjasi"
    ],
    "rod": "f"
  },
  {
    "gen": "ei",
    "lotincha": [
      "facies"
    ],
    "o'zbekcha": [
      "yuza"
    ],
    "rod": "f"
  },
  {
    "gen": "ei",
    "lotincha": [
      "superficies"
    ],
    "o'zbekcha": [
      "yuza"
    ],
    "rod": "f"
  },
  {
    "gen": "us",
    "lotincha": [
      "auditus"
    ],
    "o'zbekcha": [
      "eshituv"
    ],
    "rod": "m"
  },
  {
    "gen": "udus",
    "lotincha": [
      "incus"
    ],
    "o'zbekcha": [
      "sandom"
    ],
    "rod": "f"
  },
  {
    "gen": "us",
    "lotincha": [
      "visus"
    ],
    "o'zbekcha": [
      "ko'rish"
    ],
    "rod": "m"
  },
  {
    "gen": "utis",
    "lotincha": [
      "senectus"
    ],
    "o'zbekcha": [
      "qarilik"
    ],
    "rod": "f"
  },
  {
    "gen": "i",
    "lotincha": [
      "esophagus"
    ],
    "o'zbekcha": [
      "qizilo'ngach"
    ],
    "rod": "m"
  },
  {
    "gen": "eris",
    "lotincha": [
      "ulcus"
    ],
    "o'zbekcha": [
      "yara"
    ],
    "rod": "n"
  },
  {
    "gen": "eris",
    "lotincha": [
      "viscus"
    ],
    "o'zbekcha": [
      "ichki a'zo"
    ],
    "rod": "n"
  },
  {
    "gen": "us",
    "lotincha": [
      "abscessus"
    ],
    "o'zbekcha": [
      "yorilishi"
    ],
    "rod": "m"
  },
  {
    "gen": "us",
    "lotincha": [
      "aditus"
    ],
    "o'zbekcha": [
      "kirish"
    ],
    "rod": "m"
  },
  {
    "gen": "us",
    "lotincha": [
      "exitus"
    ],
    "o'zbekcha": [
      "natija"
    ],
    "rod": "m"
  },
  {
    "gen": "us",
    "lotincha": [
      "casus"
    ],
    "o'zbekcha": [
      "voqea"
    ],
    "rod": "m"
  },
  {
    "gen": "us",
    "lotincha": [
      "habitus"
    ],
    "o'zbekcha": [
      "tashqi ko'rinish"
    ],
    "rod": "m"
  },
  {
    "gen": "us",
    "lotincha": [
      "hiatus"
    ],
    "o'zbekcha": [
      "yoriq",
      "teshik"
    ],
    "rod": "m"
  },
  {
    "gen": "us",
    "lotincha": [
      "pulsus"
    ],
    "o'zbekcha": [
      "puls"
    ],
    "rod": "m"
  },
  {
    "gen": "us",
    "lotincha": [
      "usus"
    ],
    "o'zbekcha": [
      "qo'llanish"
    ],
    "rod": "m"
  },
  {
    "gen": "us",
    "lotincha": [
      "collapsus"
    ],
    "o'zbekcha": [
      "yurakning o'tkir yetishmovchiligi"
    ],
    "rod": "m"
  },
  {
    "gen": "us",
    "lotincha": [
      "istus"
    ],
    "o'zbekcha": [
      "itarish",
      "turtish"
    ],
    "rod": "m"
  },
  {
    "gen": "ei",
    "lotincha": [
      "caries"
    ],
    "o'zbekcha": [
      "chirishlik"
    ],
    "rod": "f"
  },
  {
    "gen": "ei",
    "lotincha": [
      "scabies"
    ],
    "o'zbekcha": [
      "qo'tir"
    ],
    "rod": "f"
  },
  {
    "gen": "ai",
    "lotincha": [
      "rabies"
    ],
    "o'zbekcha": [
      "qutirish"
    ],
    "rod": "f"
  },
  {
    "gen": "ei",
    "lotincha": [
      "species"
    ],
    "o'zbekcha": [
      "yig'ma",
      "to'plam"
    ],
    "rod": "f"
  },
  {
    "gen": "i",
    "lotincha": [
      "acidum"
    ],
    "o'zbekcha": [
      "kislota"
    ],
    "rod": "n"
  },
  {
    "gen": "ae",
    "lotincha": [
      "achillea"
    ],
    "o'zbekcha": [
      "bo'ymadron"
    ],
    "rod": "f"
  },
  {
    "gen": "i",
    "lotincha": [
      "acyclidinum"
    ],
    "o'zbekcha": [
      "atsiklidin"
    ],
    "rod": "n"
  },
  {
    "gen": "ipis",
    "lotincha": [
      "adeps"
    ],
    "o'zbekcha": [
      "yog'"
    ],
    "rod": "m"
  },
  {
    "gen": "idis",
    "lotincha": [
      "adonis"
    ],
    "o'zbekcha": [
      "adonis(gulizardak, safsargul)"
    ],
    "rod": "m"
  },
  {
    "gen": "i",
    "lotincha": [
      "aethacridinum"
    ],
    "o'zbekcha": [
      "etakridin"
    ],
    "rod": "n"
  },
  {
    "gen": "i",
    "lotincha": [
      "aethamidum"
    ],
    "o'zbekcha": [
      "etamid"
    ],
    "rod": "n"
  },
  {
    "gen": "i",
    "lotincha": [
      "aethimizolum"
    ],
    "o'zbekcha": [
      "etimizol"
    ],
    "rod": "n"
  },
  {
    "gen": "i",
    "lotincha": [
      "aethinyloestradiolum"
    ],
    "o'zbekcha": [
      "etinilestradiyol"
    ],
    "rod": "n"
  },
  {
    "gen": "eris",
    "lotincha": [
      "aether"
    ],
    "o'zbekcha": [
      "efir"
    ],
    "rod": "m"
  },
  {
    "gen": "a",
    "lotincha": [
      "aethereus"
    ],
    "o'zbekcha": [
      "efir(moyli)li"
    ],
    "rod": "um"
  },
  {
    "gen": "a",
    "lotincha": [
      "aethylicus"
    ],
    "o'zbekcha": [
      "etil(spirti)li"
    ],
    "rod": "um"
  },
  {
    "gen": "i",
    "lotincha": [
      "aethylium"
    ],
    "o'zbekcha": [
      "etil"
    ],
    "rod": "n"
  },
  {
    "gen": "i",
    "lotincha": [
      "alcaloidum"
    ],
    "o'zbekcha": [
      "yomtoq"
    ],
    "rod": "n"
  },
  {
    "gen": "i",
    "lotincha": [
      " allocholum"
    ],
    "o'zbekcha": [
      "alloxol"
    ],
    "rod": "n"
  },
  {
    "gen": "i",
    "lotincha": [
      "alnus"
    ],
    "o'zbekcha": [
      "qandag'och, olxa"
    ],
    "rod": "f"
  },
  {
    "gen": "i",
    "lotincha": [
      "amidopyrinum"
    ],
    "o'zbekcha": [
      "amidopirin"
    ],
    "rod": "n"
  },
  {
    "gen": "i",
    "lotincha": [
      "aminalonum"
    ],
    "o'zbekcha": [
      "aminazin"
    ],
    "rod": "n"
  },
  {
    "gen": "ar",
    "lotincha": [
      "ampulla"
    ],
    "o'zbekcha": [
      "ampula"
    ],
    "rod": "f"
  },
  {
    "gen": "ar",
    "lotincha": [
      "amygdala"
    ],
    "o'zbekcha": [
      "bodom"
    ],
    "rod": "f"
  },
  {
    "gen": "I",
    "lotincha": [
      "amylum"
    ],
    "o'zbekcha": [
      "kraxmal"
    ],
    "rod": "n"
  },
  {
    "gen": "i",
    "lotincha": [
      "anaesthesinum"
    ],
    "o'zbekcha": [
      "anestezin"
    ],
    "rod": "n"
  },
  {
    "gen": "ahpylla",
    "lotincha": [
      "anabasis"
    ],
    "o'zbekcha": [
      "maymunjon"
    ],
    "rod": "ot"
  },
  {
    "gen": "i",
    "lotincha": [
      "anethum"
    ],
    "o'zbekcha": [
      "shivit"
    ],
    "rod": "n"
  },
  {
    "gen": "i",
    "lotincha": [
      "anisum"
    ],
    "o'zbekcha": [
      "arpabodiyon, oddiy Anis"
    ],
    "rod": "n"
  },
  {
    "gen": "a",
    "lotincha": [
      "antiasthmaticus"
    ],
    "o'zbekcha": [
      "ich ketishiga qarshi"
    ],
    "rod": "um"
  },
  {
    "gen": "i",
    "lotincha": [
      "antidotum"
    ],
    "o'zbekcha": [
      "zaharga qarshi dori"
    ],
    "rod": "n"
  },
  {
    "gen": "a",
    "lotincha": [
      "antigangraenosus"
    ],
    "o'zbekcha": [
      "gangrenaga qarshi"
    ],
    "rod": "um"
  },
  {
    "gen": "e",
    "lotincha": [
      "antihaemorrhoidalis"
    ],
    "o'zbekcha": [
      "bevoailga qarshi"
    ],
    "rod": "ot"
  },
  {
    "gen": "a",
    "lotincha": [
      "antipestosus"
    ],
    "o'zbekcha": [
      "o'latga qarshi"
    ],
    "rod": "um"
  },
  {
    "gen": "a",
    "lotincha": [
      "antipyreticus"
    ],
    "o'zbekcha": [
      "issiqni pasaytiruvchi"
    ],
    "rod": "um"
  },
  {
    "gen": "a",
    "lotincha": [
      "antirabicus"
    ],
    "o'zbekcha": [
      "quturushga qarshi"
    ],
    "rod": "um"
  },
  {
    "gen": "a",
    "lotincha": [
      "antisepticus"
    ],
    "o'zbekcha": [
      "antiseptik"
    ],
    "rod": "um"
  },
  {
    "gen": "a",
    "lotincha": [
      "antitetanicus"
    ],
    "o'zbekcha": [
      "qoqsholga qarshi"
    ],
    "rod": "um"
  },
  {
    "gen": "i",
    "lotincha": [
      "apomorphinum"
    ],
    "o'zbekcha": [
      "apomorfin"
    ],
    "rod": "n"
  },
  {
    "gen": "i",
    "lotincha": [
      "aprenalum"
    ],
    "o'zbekcha": [
      "aprenol"
    ],
    "rod": "n"
  },
  {
    "gen": "i",
    "lotincha": [
      "apressinum"
    ],
    "o'zbekcha": [
      "apressin"
    ],
    "rod": "n"
  },
  {
    "gen": "i",
    "lotincha": [
      "aprophenum"
    ],
    "o'zbekcha": [
      "apofen"
    ],
    "rod": "n"
  },
  {
    "gen": "idis",
    "lotincha": [
      "arachis"
    ],
    "o'zbekcha": [
      "yeryong'oq"
    ],
    "rod": "f"
  },
  {
    "gen": "ae",
    "lotincha": [
      "aralia"
    ],
    "o'zbekcha": [
      "araliya"
    ],
    "rod": "f"
  },
  {
    "gen": "i",
    "lotincha": [
      "argentum"
    ],
    "o'zbekcha": [
      "kumush"
    ],
    "rod": "n"
  },
  {
    "gen": "ae",
    "lotincha": [
      "armeniaca"
    ],
    "o'zbekcha": [
      "o'rik"
    ],
    "rod": "f"
  },
  {
    "gen": "a",
    "lotincha": [
      "aromaticus"
    ],
    "o'zbekcha": [
      "xushbo'y"
    ],
    "rod": "um"
  },
  {
    "gen": "i",
    "lotincha": [
      "arsenicum"
    ],
    "o'zbekcha": [
      "margumush"
    ],
    "rod": "n"
  },
  {
    "gen": "i",
    "lotincha": [
      "aurum"
    ],
    "o'zbekcha": [
      "oltin"
    ],
    "rod": "n"
  },
  {
    "gen": "es",
    "lotincha": [
      "chole"
    ],
    "o'zbekcha": [
      "o't"
    ],
    "rod": "f"
  },
  {
    "gen": "ae",
    "lotincha": [
      "ala"
    ],
    "o'zbekcha": [
      "qanot"
    ],
    "rod": "f"
  },
  {
    "gen": "ae",
    "lotincha": [
      "aorta"
    ],
    "o'zbekcha": [
      "aorta"
    ],
    "rod": "f"
  },
  {
    "gen": "ae",
    "lotincha": [
      "arteria"
    ],
    "o'zbekcha": [
      "arteriya"
    ],
    "rod": "f"
  },
  {
    "gen": "ae",
    "lotincha": [
      "concha"
    ],
    "o'zbekcha": [
      "chig'anoq"
    ],
    "rod": "f"
  },
  {
    "gen": "ae",
    "lotincha": [
      "spina"
    ],
    "o'zbekcha": [
      "o'tkir qirra"
    ],
    "rod": "f"
  },
  {
    "gen": "ae",
    "lotincha": [
      "vena"
    ],
    "o'zbekcha": [
      "vena"
    ],
    "rod": "f"
  },
  {
    "gen": "ae",
    "lotincha": [
      "crista"
    ],
    "o'zbekcha": [
      "qirra"
    ],
    "rod": "f"
  },
  {
    "gen": "ae",
    "lotincha": [
      "lamina"
    ],
    "o'zbekcha": [
      "plastinka"
    ],
    "rod": "f"
  },
  {
    "gen": "ae",
    "lotincha": [
      "lingua"
    ],
    "o'zbekcha": [
      "til"
    ],
    "rod": "f"
  },
  {
    "gen": "ae",
    "lotincha": [
      "mandibula"
    ],
    "o'zbekcha": [
      "pastki jag'"
    ],
    "rod": "f"
  },
  {
    "gen": "ae",
    "lotincha": [
      "maxilla"
    ],
    "o'zbekcha": [
      "yuqori jag'"
    ],
    "rod": "f"
  },
  {
    "gen": "ae",
    "lotincha": [
      "sutura"
    ],
    "o'zbekcha": [
      "chok"
    ],
    "rod": "f"
  },
  {
    "gen": "ae",
    "lotincha": [
      "tuba"
    ],
    "o'zbekcha": [
      "nay"
    ],
    "rod": "f"
  },
  {
    "gen": "ae",
    "lotincha": [
      "clavicula"
    ],
    "o'zbekcha": [
      "o'mrov",
      "o'mrov suyagi"
    ],
    "rod": "f"
  },
  {
    "gen": "ae",
    "lotincha": [
      "fascia"
    ],
    "o'zbekcha": [
      "mushakni o'rab turuvchi yupqa parda"
    ],
    "rod": "f"
  },
  {
    "gen": "ae",
    "lotincha": [
      "nucha"
    ],
    "o'zbekcha": [
      "ensa"
    ],
    "rod": "f"
  },
  {
    "gen": "ae",
    "lotincha": [
      "tonsilla"
    ],
    "o'zbekcha": [
      "bodomcha"
    ],
    "rod": "ot"
  },
  {
    "gen": "ae",
    "lotincha": [
      "squama"
    ],
    "o'zbekcha": [
      "tangacha"
    ],
    "rod": "f"
  },
  {
    "gen": "ae",
    "lotincha": [
      "ulna"
    ],
    "o'zbekcha": [
      "tirsak suyagi"
    ],
    "rod": "f"
  },
  {
    "gen": "i",
    "lotincha": [
      "vestibulum"
    ],
    "o'zbekcha": [
      "dahliz"
    ],
    "rod": "n"
  },
  {
    "gen": "i",
    "lotincha": [
      "porus"
    ],
    "o'zbekcha": [
      "teshik"
    ],
    "rod": "m"
  },
  {
    "gen": "i",
    "lotincha": [
      "palatum"
    ],
    "o'zbekcha": [
      "tanglay"
    ],
    "rod": "n"
  },
  {
    "gen": "i",
    "lotincha": [
      "organum"
    ],
    "o'zbekcha": [
      "organ",
      "a'zo"
    ],
    "rod": "n"
  },
  {
    "gen": "itis",
    "lotincha": [
      "caput"
    ],
    "o'zbekcha": [
      "bosh"
    ],
    "rod": "n"
  },
  {
    "gen": "oris",
    "lotincha": [
      "os"
    ],
    "o'zbekcha": [
      "og'iz"
    ],
    "rod": "n"
  },
  {
    "gen": "ae",
    "lotincha": [
      "bacca"
    ],
    "o'zbekcha": [
      "meva",
      "o'simlik"
    ],
    "rod": "f"
  },
  {
    "gen": "ae",
    "lotincha": [
      "barba"
    ],
    "o'zbekcha": [
      "saqol"
    ],
    "rod": "f"
  },
  {
    "gen": "is",
    "lotincha": [
      "basis"
    ],
    "o'zbekcha": [
      "asos"
    ],
    "rod": "f"
  },
  {
    "gen": "e",
    "lotincha": [
      "biliaris"
    ],
    "o'zbekcha": [
      "o'tga oid"
    ],
    "rod": "ot"
  },
  {
    "gen": "era",
    "lotincha": [
      "bilifer"
    ],
    "o'zbekcha": [
      "o'tga oid"
    ],
    "rod": "erum"
  },
  {
    "gen": "a",
    "lotincha": [
      "biliosus"
    ],
    "o'zbekcha": [
      "o't moddasiga boy"
    ],
    "rod": "um"
  },
  {
    "gen": "i",
    "lotincha": [
      "bolus"
    ],
    "o'zbekcha": [
      "qum"
    ],
    "rod": "f"
  },
  {
    "gen": "a",
    "lotincha": [
      "boricus"
    ],
    "o'zbekcha": [
      "borotga oid"
    ],
    "rod": "um"
  },
  {
    "gen": "i",
    "lotincha": [
      "brachium"
    ],
    "o'zbekcha": [
      "yelka"
    ],
    "rod": "n"
  },
  {
    "gen": "e",
    "lotincha": [
      "bronchialis"
    ],
    "o'zbekcha": [
      "bronxga tegishli"
    ],
    "rod": "ot"
  },
  {
    "gen": "i",
    "lotincha": [
      "bulbus"
    ],
    "o'zbekcha": [
      "soqqa, piyoz boshi"
    ],
    "rod": "m"
  },
  {
    "gen": "ae",
    "lotincha": [
      "bulla"
    ],
    "o'zbekcha": [
      "pufakchaga"
    ],
    "rod": "f"
  },
  {
    "gen": "ae",
    "lotincha": [
      "bursa"
    ],
    "o'zbekcha": [
      "sumka",
      "xalta"
    ],
    "rod": "f"
  }
]
"""

OT = json.loads(ot)

class Sozlamalar:

    def __init__(self):

        # GUI sozlamalari
        self.asosiy_oyna_nomi = " Lotin-O'zbek lug'ati"
        self.asosiy_oyna_balandligi = 250
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
        else:
            pass
    
    def button1_command1(self):
        if KOD:
            x = ozbek_lotin(OT, self.entry1_string_var1.get(), True)
            if type(x) == dict:
                self.label1.configure(text="{}".format(x))
            else:
                self.label1.configure(text="Siz kiritgan so'z topilmadi!")
        else:
            msg.showinfo("Eslatma!", "Dasturdan foydalanish uchun 'Litsenziya' olish kerak.\n 'Litsenziya' olish uchun +998-99-772-33-28 nomer bilan yoki uzbekdasturchisiman@gmail.com pochta manzili bilan bo'glaning.")
               
    def button2_command1(self):
        if KOD:
            x = ozbek_lotin(OT, self.entry2_string_var1.get())
            if type(x) == dict:
                self.label2.configure(text="{}".format(x))
            else:
                self.label2.configure(text="Siz kiritgan so'z topilmadi!")
            pass
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
            if type(kod2) == str and type(int(kod1)) == int and self.radiobutton_var.get() == 1:
                path_to_the_text_file2 = "./file_to_activate_the_program.txt"
                with open(path_to_the_text_file2, "w") as text_file2:
                    text_file2.write("{}{}".format(kod2, kod1))
            
                  
    def _chiqish(self):
        self.asosiy_oyna.quit()
        self.asosiy_oyna.destroy()
        exit()
    
    def _msgBox(self):
        msg.showinfo("Lotin-O'zbek lug'ati ", " Dastur yaratuvchisi: Shodmonov Zafar\n 2023-yilda yaratildi.\n Elektron pochta: uzbekdasturchisiman@gmail.com \n Telefon nomer: +998-99-772-33-28\n Dastur versiyasi 1.0.0 \n")
      
    def mainloop(self):
        self.asosiy_oyna.mainloop()


def gui_main_funksiyasi():
    my_gui = Gui()
    my_gui.mainloop()

if __name__ == "__main__":
    gui_main_funksiyasi()
