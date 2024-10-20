averb = {
    "entall1": "o",
    "entall2": "as",
    "entall3": "a",
    "flertall1": "amos",
    "flertall2": "aís",
    "flertall3": "an"
}

everb = {
    "entall1": "o",
    "entall2": "es",
    "entall3": "e",
    "flertall1": "emos",
    "flertall2": "eís",
    "flertall3": "en"
}

iverb = {
    "entall1": "o",
    "entall2": "es",
    "entall3": "e",
    "flertall1": "imos",
    "flertall2": "iaís",
    "flertall3": "en"
}

verb = input("Skriv inn et verb på spansk: ")
stamme = verb[:-2]
type_verb = None

if verb[-2] == "a":
    type_verb = averb
elif verb[-2] == "e":
    type_verb = everb
elif verb[-2] == "i":
    type_verb = iverb
else:
    print("Denne typen verb støttes ikke av programmet.")

for ending in type_verb.values():
    print(stamme + ending)





    