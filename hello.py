import random

def start_game(n):
    number = random.randint(1,n)
    count = 1
    print(str(number) + ' ���� �����')
    print('������ ���� �������')
    while True:
        user_number = int(input())
        if user_number == number:
            print('�� �������!!!')
            break
        elif user_number > number:
            print('������� �����, ���������� ��� ���')
        else:
            print('������� ����, ���������� ��� ���')
        count += 1
    print('�� ������� � ' + str(count) + ' �������')

print('������� ������ �������')
n = int(input())
while n < 1:
    print('������� ����� ��������')
    n = int(input())
while True: 
    start_game(n)
    print('��� ����� ���� �������� ������ �����')
    n = int(input())
    