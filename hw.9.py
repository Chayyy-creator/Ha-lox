def primer(x):
   if x > 0:
     return x - 12
   elif x == 0:
     return 5
   else:
     return x**2
x = float(input('Введите х: '))
y = primer(x)
print(f"Игрек равен: {y}")