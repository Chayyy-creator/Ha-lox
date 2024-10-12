def guess_number():
    low = 1
    high = 100
    tries = 0
    print("Загадай число от 1 до 100, а я его угадаю!")
    while low <= high:
        mid = (low + high) // 2 
        tries += 1 
        print(f"Ваше число равно, меньше или больше, чем {mid}?") 
        response = input("Введите 1 (равно), 2 (больше), 3 (меньше): ") 
        if response == '1': 
            print(f"Ура! Я угадала ваше число {mid} за {tries} попыток.") 
            return 
        elif response == '2': low = mid + 1 
        elif response == '3': high = mid - 1 
        else: print("Пожалуйста, введите 1, 2 или 3.") 
        print("Что-то пошло не так, я не смогла угадать число.") 
guess_number()
