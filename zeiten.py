# zeiten.py
import sys
def zeitInSekunden(Zeit):
    gesamt = 0
    zeit = Zeit.split(":")
    h = int (zeit[0])
    m = int (zeit[1])
    s = int (zeit[2])
    gesamt += h*3600
    gesamt += m*60
    gesamt += s
    return gesamt
p = sys.argv
beginnSekunden = zeitInSekunden(p[1])
endSekunden = zeitInSekunden(p[2])
print (endSekunden-beginnSekunden) 
