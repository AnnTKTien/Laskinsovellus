# Tässä luodaan itse dekoraattori-funktio, jonka tarkoituksena on siistiä koodia ja tehdä uudelleen toistettava tulostus.
def printing_result(base_fn):
    def enhanced_fn(*args, **kwargs):
        result = base_fn(*args, **kwargs)
        print(f"{a} {merkki} {b} = {result}")
    return enhanced_fn

# Funktio joka summaa kaksi arvoa ja palauttaa.
@printing_result
def add(a, b):
    return a + b

# Funktio joka vähentää kaksi arvoa ja palauttaa.
@printing_result
def sub(a, b):
    return a - b

# Funktio joka kertoo kaksi arvoa ja palauttaa.
@printing_result
def mul(a, b):
    return a * b

# Funktio joka jakaa kaksi arvoa ja palauttaa. Tässä on myös huomioitu 0 jakamisen mahdottomuus.
@printing_result
def div(a, b):
    if b == 0:
        return "Nollalla ei voi jakaa!"
    return a / b

# Tämä on tulostus, joka suoritetaan ohjelman alussa
print("""---Laskin--
Valitse lasku operaatio
1.Summa
2.Erotus
3.Tulo
4.Jako""")

# While-loopin sisällä varmistetaan että valittu arvo on välillä (1-4) vain numeeriset arvot hyväksytään, mutta arvot vastaanotetaan string-muodossa.
while True:
    valinta = input("Valitse operaatio numeroilla (1-4): ")
# Jos valinta on välillä (1-4) suoritetaan funktio valinnan mukaan, tapahtuu tulostus ja sen jälkeen ohjelman suoritus lopetetaan.
#Valinnoissa myös muuttuja merkille, joka määrittää mikä laskun mukana tulostettaan.
    if valinta in ["1", "2", "3", "4"]:
        # Pyydetään käyttäjältä kaksi arvoa
        a = int(input("Anna ensimmäinen numero: "))
        b = int(input("Anna toinen numero: "))

        if valinta == "1":
            merkki = "+"
            add(a, b)

        elif valinta == "2":
            merkki = "-"
            sub(a, b)

        elif valinta == "3":
            merkki = "*"
            mul(a, b)

        elif valinta == "4":
            merkki = "/"
            div(a, b)

        break
# Jos valinta on jotain muuta kuin (1-4), valintaa ei hyväksytä ja ohjelma kysyy laskutoimituksen uudelleen.
    else:
        print("Virheellinen valinta, yritä uudelleen!")
