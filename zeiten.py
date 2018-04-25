# zeiten.py
def zeitInSekunden(h, m, s):
    gesamt = 0
    gesamt += h*3600
    gesamt += m*60
    gesamt += s
    return gesamt
beginnZeit = input("Beginnzeit:\n")
endZeit = input("Endzeit:")
beginn = beginnZeit.split(":")
end = endZeit.split(":")
h1 = int (end[0])
m1 = int (end[1])
s1 = int (end[2])
print (beginn)
h = int (beginn[0])
m = int (beginn[1])
s = int (beginn[2])
print("Stunden: h\n",h)
print("Minuten: m\n",m)
print("Sekunden: \n",s)
beginnSekunden = zeitInSekunden(h, m, s)
endSekunden = zeitInSekunden(h1, m1, s1)
print (endSekunden-beginnSekunden)