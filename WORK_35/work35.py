# Задача №35. Решение в группах

# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)

# Input: 5
# Output: yes 

num = int(input('Введите число: '))
def IsSimple(num):
    for i in range(2,num):
        if num%i == 0:
            print('Число не простое')
            break
    else:
        print('Число простое')
IsSimple(num)

#ИЛИ ТАК

num = int(input('Введите число: '))
def IsSimple(num):
   
        
    for i in range(2,num):
        if num%i == 0:
            print('Число не простое')
            break
    else:
        if num <=1:
            print('Число ни простое ни составное ')
        else:
            print('Число простое')
IsSimple(num)

#ИЛИ ТАК

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
