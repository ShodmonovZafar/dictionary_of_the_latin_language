from lugat import LUGAT
OT = {}
for i in LUGAT.keys():
    for j in i:
        if j == "ot":
            OT[i] = LUGAT[i]

with open("./OT.txt", "w") as f:
    for i in OT.keys():
        if type(OT[i]) == str:
            s = '{} : "{}", '.format(i, OT[i])
        else:
            s = '{} : {}, '.format(i, OT[i])
        f.write(s)