time = float(input('Сколько сейчас времени? '))
if (time < 8) or (time >= 22) or (10 <= time <= 12) or (14 <= time <= 15) or (18 <= time <= 20):
    print('Посылку получить нельзя ')
else:
    print('Можно получить посылку')