# zeiten.py
def zeitInSekunden(h, m, s):
beginnZeit = input("Beginnzeit:\n")
endZeit = input("Endzeit:")
beginn = beginnZeit.split(":")
print (beginn)
h = int (beginn[0])
m = int (beginn[1])
s = int (beginn[2])
print("Stunden: h\n",h)
print("Minuten: m\n",m)
print("Sekunden: \n",s)
beginnSekunden = s + m*60 +h*3600
print (beginnSekunden)