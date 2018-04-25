# parkhaus.py 
# geändert

print ("Linienbus-Simulator")

personen = 0
haltestellen = int(input("wie viele Haltestellen soll es geben?"))
for x in range (1,haltestellen+1):
    personen = int(input("Haltestelle",x,"erreicht. Wie viele Personen steigen ein?")) + personen  
    personen = personen - int(input("Haltestelle",x,"erreicht. Wie viele Personen steigen aus?"))
    print("Es sind",personen,"im Bus.")
