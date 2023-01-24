lugat = {
    ("homo", "inis", "m") : "odam",
    ("vesica", "ae", "f") : "pufak",
    ("fundus", "i", "m") : "tub",
    ("dorsum", "i", "n") : "orqa"
}




def lotinchadan_ozbekchaga(lotincha: str, lugat: dict):
    for key in lugat.keys():
        if key[0] == lotincha:
            return lugat[key]
    return 0

def ozbekchadan_lotinchaga(ozbekcha: str, lugat: dict):
    for key in lugat:
        if ozbekcha == lugat[key]:
            return key
    return 0

status = False

if status:
    izlanayotgan_lotincha_soz = input("Lotincha so'zni kiriting: ")
    print(lotinchadan_ozbekchaga(izlanayotgan_lotincha_soz, lugat))
else:
    izlanayotgan_ozbekcha_soz = input("O'zbekcha so'zni kiriting: ")
    print(ozbekchadan_lotinchaga(izlanayotgan_ozbekcha_soz, lugat))
    