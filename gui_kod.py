from pathlib import Path

x = Path(".")
for i in x.iterdir():
    if i.is_file() and i.name == "kod.txt":
        with open(i, "r") as f:
            d = f.read()
            if d == "":
                KOD = False
            else:
                KOD = True


