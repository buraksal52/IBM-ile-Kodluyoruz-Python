import math
print("İki nokta olan A ve B arasındaki mesafeyi ölçme.")
apsis1 = int(input("Lütfen A noktasının apsisini giriniz: "))
apsis2 = int(input("Lütfen B noktasının apsisini giriniz: "))
ordinat1 = int(input("Lütfen A noktasının ordinatını giriniz: "))
ordinat2 = int(input("Lütfen B noktasının ordinatını giriniz: "))
sumofx = apsis1-apsis2
sumofy = ordinat1-ordinat2
innersquare = (sumofx**2 + sumofy**2)**0.5
strinner = str(innersquare)
xf=str(apsis1)
yf=str(ordinat1)
xl=str(apsis2)
yl=str(ordinat2)
print("A("+ xf +","+ yf +")")
print("B("+ xl +","+ yl +")")
print("İki nokta arası mesafe: "+strinner)