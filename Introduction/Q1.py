x = 1
job = []
while x <= 2:
    info = input().split(" ")
    info[1] = info[1].split(":")
    for i in range(0, len(info[1])):
        info[1][i] = int(info[1][i])
    info[0] = int(info[0])
    job.append(info)
    x += 1


def calc_time(job):
    if job[0][0] > job[1][0]:
        return print("Data inválida!")
    else:
        day = job[1][0] - job[0][0]
    hor = 0
    minu = 0
    sec = 0
    n = 0
    while n < 2:
        for dhm in job:
            dayy, hms = dhm
            hora, minuto, segundo = hms
            if n == 0:
                hor = hora
                minu = minuto
                sec = segundo
            else:
                if (hora - hor) < 0:
                    hor = (hora - hor) + 24
                    day -= 1
                else:
                    hor = hora - hor
                if (minuto - minu) < 0:
                    minu = (minuto - minu) + 60
                    hor -= 1
                else:
                    minu = (minuto - minu)
                if (segundo - sec) < 0:
                    sec = (segundo - sec) + 60
                    minu -= 1
                else:
                    sec = (segundo - sec)
            n += 1
    if day < 0 or (day == 0 and hor == 0 and minu == 0 and sec == 0):
        return print("Data inválida!")
    else:
        return print(f"{day} dia(s)\n{hor} hora(s)\n{minu} minuto(s)\n{sec} segundo(s)")


calc_time(job)
