#params.py
import sys
#z1 = int(input("Zahl1:\n"))
#z2 = int(input("Zahl2:\n"))
#z3 = int(input("Zahl3:\n"))
p = sys.argv
print(p)
sum=0
for i in range(1,len(p)):
    sum=sum+int(p[i])

print(sum)









