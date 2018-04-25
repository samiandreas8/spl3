# zeiten.py
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
beginnZeit = input("Beginnzeit:\n")
endZeit = input("Endzeit:")
end = endZeit.split(":")
beginnSekunden = zeitInSekunden(beginnZeit)
endSekunden = zeitInSekunden(Endzeit)
print (endSekunden-beginnSekunden) 
x=0
while (wantstosubmit == true):
    submission[x] = input("UserID")
    x+=1
    submission[x] = input("Zeit")
    submission[x] = beginnSekunden-zeitInSekunden(submission[x])
    x+=1
    submission[x] = input("Correct/False")
    x+=1
for i in range(2,x+1,3):
    print(submission[i])
    