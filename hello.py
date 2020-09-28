import random

def start_game(n):
    number = random.randint(1,n)
    count = 1
    print(str(number) + ' Само число')
    print('Пишите ваши догадки')
    while True:
        user_number = int(input())
        if user_number == number:
            print('Вы угадали!!!')
            break
        elif user_number > number:
            print('Слишком много, попробуйте еще раз')
        else:
            print('Слишком мало, попробуйте еще раз')
        count += 1
    print('Вы угадали с ' + str(count) + ' попытки')

print('Введите правую границу')
n = int(input())
while n < 1:
    print('Введите число побольше')
    n = int(input())
while True: 
    start_game(n)
    print('Для новой игры выберете другое число')
    n = int(input())
    