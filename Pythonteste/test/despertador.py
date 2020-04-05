import time
alarm = (int(input('Digite a hora desejada: ')), int(input('Digite os minutos: ')))
desp = 'Alarme'
while True:
    hora = (time.localtime().tm_hour, time.localtime().tm_min, time.localtime().tm_sec)
    time.sleep(1)
    if hora[0] == alarm[0] and hora[1] == alarm[1]:
        print(desp)
        desp += 'e'
    if hora[0] == alarm[0] and hora[1] == alarm[1] + 1:
        break
