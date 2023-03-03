# Задача №31. Решение в группах

# Последовательностью Фибоначчи называется
# последовательность чисел a0, a1 , ..., an,  ..., где
#, ..., где

#a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
#f(n) = f(n - 1) + f(n - 2)

# Требуется найти N-е число Фибоначчи

# Input: 7
# Output: 21
# Задание необходимо решать через рекурсию

def GetUserNumber(message_to_user):
    flag = True
    while flag:
        try:
            print(message_to_user)
            n = int(input())
            if n or n==0:
                flag = False
                return n
            #else:
                #print('Ошибка ввода! Введено ')
        except ValueError:
            print('Ошибка ввода! Введено не число')
            
            #Без верхнего г*вна

def Fibonaci(num):
    if num<=1:
        return num
    else:
        return Fibonaci(num-1)+Fibonaci(num-2)



a = GetUserNumber('Введите число: ')
print(Fibonaci(a))

