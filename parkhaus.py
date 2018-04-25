# parkhaus.py 
# geändert

print ("Linienbus-Simulator")

personen = 0
haltestellen = int(input("wie viele Haltestellen soll es geben?\n"))

for x in range (1,haltestellen+1):
    est = "Haltestelle "+ str(x)+ " erreicht. Wie viele Personen steigen ein?\n"
    ast = "Wie viele Personen steigen aus?\n"
    einsteiger = int(input(est))
    if (personen + einsteiger <= 60):
        personen =  einsteiger + personen
    else:
        print("Es können",Personen+einsteiger-60," nicht einsteigen.") 
        personen = 60
    aussteiger =  int(input(ast))
    if (personen - aussteiger >= 0):
        personen = personen - aussteiger
    else:
        print("Es sind zu wenig Personen im Bus")
        personen = 0
    print("Es sind",personen,"im Bus.",einsteiger,"sind eingestiegen,",aussteiger,"sind ausgestiegen")
