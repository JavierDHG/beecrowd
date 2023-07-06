dia,date1=input().split()
date1 = int(date1)
h1,m1,s1=map(int,input().split(":"))

dia,date2=input().split()
date2 = int(date2)
h2,m2,s2=map(int,input().split(":"))

s = s2 - s1
m = m2 - m1
h = h2 - h1
d = date2 - date1

if(s<0):
	s+=60
	m-=1


if(m<0):
	m+=60
	h-=1

if(h<0):
	h+=24
	d-=1

print(f"{d} dia(s)")
print(f"{h} hora(s)")
print(f"{m} minuto(s)")
print(f"{s} segundo(s)")



'''Mi intento
dia,dato1=input().split()
daton1=int(dato1)
h1,m1,s1=map(int,input().split(":"))

dia2,dato2=input().split()
daton2=int(dato2)
h2,m2,s2=map(int,input().split(":"))

dif_dias=((daton2*1440)+h2*60)-((daton1*1440)+h1*60)
if dif_dias<=0:
    dif_dias+=1440*60
else: 
    time=dif_dias//1440

dif_horas=((h2*60)+m2)-((h1*60)+m1)
if dif_horas<0:
    horas=dif_horas//60
    horas=24+horas
else:
    horas=dif_horas//60
    
dif_minutos=((m2*60)+s2)-((m1*60)+s1)
if dif_minutos<0:
    minutos=dif_minutos//60
else:
    minutos=dif_minutos//60

dif_segundos=(s2*60)-(s1*60)
print(dif_segundos)
if dif_segundos<0:
    segundos=dif_segundos//60
else:
    segundos=dif_segundos//60


print(f"{time} dia(s)"
      f"{horas} hora(s) "
      f"{minutos} minutos(s)"
      f"{segundos} segundos(s)")'''