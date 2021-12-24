def sort(array):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

def binary_search(array, element, left, right):
    if left > right:
        return False
    middle = (left +right) // 2
    if element == array[middle]:
        return middle
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)

s = list(map(int, input("Введите последовательность чисел через пробел: ").split()))
number = int(input("Введите любое число: "))
print(sort(s))
index = binary_search(s, number, 0, len(s))
if index == False:
   s.append(number)
   sort(s)
   index = binary_search(s, number, 0, len(s))
   print("Число отсутсвует в списке")
else:
   print("Индекс числа =", index)
