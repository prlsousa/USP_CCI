import math

x1 = int(input("coordenada x1: "))
y1 = int(input("coordenada y1: "))
x2 = int(input("coordenada x2: "))
y2 = int(input("coordenada y2: "))

d = math.sqrt(((x1-x2)**2) + ((y1-y2)**2))

if d >= 10:
    print("longe")
else:
    print("perto")