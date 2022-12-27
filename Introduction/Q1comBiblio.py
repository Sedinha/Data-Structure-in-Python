dia, info = input().split()
dia_i = int(dia)
info = info.split(":")
for i in range(0, len(info)):
    info[i] = int(info[i])
hor, minu, sec = info

dia, info = input().split()
day = int(dia)
info = info.split(":")
for i in range(0, len(info)):
    info[i] = int(info[i])
hora, minuto, segundo = info

dias = day - dia_i
horas = hora - hor
minutos = minuto - minu
segundos = segundo - sec

if segundos < 0:
    segundos += 60
    minutos -= 1

if minutos < 0:
    minutos += 60
    horas -= 1

if horas < 0:
    horas += 24
    dias -= 1

if dias < 0 or (dias == 0 and horas == 0 and minutos == 0 and segundos == 0):
    print('Data inválida!')
else:
    print(f"{dias} dia(s)\n{horas} hora(s)\n{minutos} minuto(s)\n{segundos} segundo(s)")
