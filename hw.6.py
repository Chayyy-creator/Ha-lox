stul1 = float(input('Стоимость товара №1: '))
stul2 = float(input('Стоимость товара №2: '))
stul3 = float(input('Стоимость товара №3: '))
stoimost = stul1+stul2+stul3
if stoimost >= 10000:
    stoimost * 10 / 100
else: print('Нету скидки')
print ('Общая сумма составила:')
print (stoimost)