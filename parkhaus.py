# parkhaus.py 
# geändert

print ("Linienbus-Simulator")

personen = 0
haltestellen = int(input("wie viele Haltestellen soll es geben?"))
for x in range (1,haltestellen+1):
    einsteiger = int(input("Haltestelle",x,"erreicht. Wie viele Personen steigen ein?"))
    if (personen + einsteiger > 60):
        personen =  einsteiger + personen
    else:
        print("Es können",-60+personen+einsteiger,"einsteigen.") 
        personen = 60
    aussteiger =  int(input("Haltestelle",x,"erreicht. Wie viele Personen steigen aus?"))
    if (personen - aussteiger >= 0):
        personen = personen - aussteiger
    else:
        print("Es sind zu wenig Personen im Bus")
        personen = 0
    print("Es sind",personen,"im Bus.")
