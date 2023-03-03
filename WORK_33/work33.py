# Задача №33. Решение в группах

# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.

# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

array = [int(i) for i in input().split()]

def ChangeMaxtoMin(array):
    min = array[0]
    max = array[0]
    for i in array:
        if i>max:
            max = i
        if i<min:
            min = i
    for i in range(len(array)):
        if array[i] == max:
            array[i]=min
    return array
print(ChangeMaxtoMin(array))

