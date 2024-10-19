import random
def guess_the_number(): 
    global number_to_guess
    global guess
    number_to_guess = random.randint(1, 100)
    guess = None
    while guess != number_to_guess:
        guess = int(input('Введите число от 1 до 100: '))
        if guess < number_to_guess:
            (print('Маленькое число,попробуйте больше:'))
        elif guess > number_to_guess:
            (print('Большое число,попробуйте меньше:'))
    print('Вы угадали число!')
def mainMenu():
    (print('Добро пожаловать на главное меню! Выберите игру:(Выбирать нужно c помощью цифр: "Камень,ножницы,бумага" - 1, "Угадай число" - 2, выйти из главного меню - 3)'))
    global chouse
    global result
    chouse = int(input('Вводить сюда: '))
def rock_paper_scissors():
    rock = "Камень"
    paper = "Бумага"
    scissors = "Ножницы"
    stop = "Стоп"
    print(f'Выберите: {rock}, {paper}, {scissors}.Когда вы захотите закончить игру, напишите {stop} ')
    user_choise = input('Введите сюда: ')
    while user_choise != stop:
        ai_choise = random.choice([rock, paper, scissors])
        if  user_choise == paper and ai_choise == rock or user_choise == scissors and ai_choise == paper or user_choise == rock and ai_choise == scissors:
            print(f'Вы выйграли! {user_choise} бьёт {ai_choise}')
        elif ai_choise == user_choise:
            print('Ничья!')
        else:
            print(f'Вы проиграли! {ai_choise} бьёт {user_choise}')
        user_choise = input('Введите сюда: ')
    print('Спасибо за игру!')
mainMenu()
while chouse != 3:
    if chouse == 2:
        guess_the_number()
    elif chouse == 1:
        rock_paper_scissors()
    mainMenu()
print('Вы вышли из главного меню!')