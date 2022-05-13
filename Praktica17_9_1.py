left_1=0       #  левая граница
right_1=10     #  правая граница 

def elem():
    element=int(input('Введите число: '))
    print('-----------------------------')
    return element

def sort(list_s):
    for i in range(1,len(list_s)):
        x = list_s[i]
        indx = i
        while indx > 0 and list_s[indx - 1] > x:
            list_s[indx] = list_s[indx - 1]
            indx -= 1
        list_s[indx] = x
    return list_s

def list_array():
    global left_1,right_1
    str_n = list(input('Введите числа через побел: ').split())
    list_n = list(map(int, str_n))
    for i in range(len(list_n)):
        if list_n[i]<left_1 or list_n[i]>right_1:
            print('Ошибка!')
            print(f'Введите числа в диапазоне от {left_1} до {right_1}')
            print('-----------------------------')
            return list_array()
    return list_n

def binary_search(array, element, left, right):
    global left_1, right_1
    if element < left_1 or element > right_1:
        print(f'Число {element} не удовлетворяет условиям задачи')
        print('-----------------------------')
        print(f'Введите число в диапазоне от {left_1} до {right_1}')
        return binary_search(array, elem(), left,right)
    elif left_1<element<right_1 and element not in array:
        print(f'Числа {element} нет в списке {array}')
        print('-----------------------------')
        return binary_search(array, elem(), left,right)
    else:
        if left > right:  # если левая граница превысила правую,
            print('если левая граница превысила правую')
            return False  # значит элемент отсутствует
        middle = (right + left) // 2  # находим середину
        if array[middle] == element:
            if array[middle-1] != element:  # если элемент в середине,
                return middle  # возвращаем этот индекс
            else:
                return middle-1
        if element < array[middle]:  # если элемент меньше элемента в середине
            # рекурсивно ищем в левой половине
            return binary_search(array, element, left, middle - 1)
        else:  # иначе в правой
            return binary_search(array, element, middle + 1, right)

print('Индекс числа =',binary_search(sort(list_array()), elem(), left_1, right_1))
