import numpy as np
import cupy as cp
import argparse
import sys


# Функция для прямого преобразования
def direct_bwt(string):
    # Перевод строки в список чисел по юникоду
    str_list = [ord(i) for i in string]

    # Переход к массиву на GPU
    s_arr = cp.array(str_list)
    # Создание матрицы со сдвигом
    # Пояснение:
    # сдвиг матрицы происходит на устройстве, потом переводится в список на
    # хост и затем снова в массив на устройстве (делается из-за проблем с
    # отсутствием поддержки типа списков с нечисловыми элементами)
    s_mat = cp.array([cp.roll(s_arr, i).tolist() for i
                     in range(0, len(s_arr))])
    # Сортировка по индексам столбцов
    # Пояснение: аналогично вышенаписанному
    i = cp.lexsort(cp.array(
        [s_mat[:, i].tolist() for i in range(len(s_arr)-1, -1, -1)]))
    s_mat = s_mat[i]

    # Обратный перевод чисел в симвлы по юникоду
    str_list = [chr(i) for i in s_mat[:, -1].tolist()]
    return (''.join(str_list),
            cp.where(cp.all(s_arr == s_mat, axis=1))[0].item())


# Функция для обратного преобразования
def inverse_bwt(string, ind):
    # Перевод строки в список чисел по юникоду
    str_list = [ord(i) for i in string]

    # Переход к массиву на GPU
    # Массив с последовательностью введенной строки
    s_arr = cp.array(str_list)
    # отсортированная последовательность
    sorted_s = cp.array(sorted(str_list))
    # Просто слияние двух предыдущих массивов
    tab_s = cp.vstack((s_arr, sorted_s))
    for i in range(1, len(s_arr)-1):
        # Сортировка, с получением индексов
        # массива tab_s для новой строки, хотя фактически - столбца
        # (метод .T меняет оси массива местами)
        j = cp.lexsort(cp.array([tab_s.T[:, i].tolist() for i
                                in range(i, -1, -1)]))
        # Добавление отсортированной по j строки к массиву
        tab_s = cp.vstack((s_arr, tab_s.T[j].T))
    # Сортировка последней строки
    j = cp.lexsort(cp.array([tab_s.T[:, i].tolist() for i
                            in range(len(s_arr)-1, -1, -1)]))

    # Обратный перевод чисел в симвлы по юникоду
    str_list = [chr(i) for i in tab_s.T[j][ind]]
    return ''.join(str_list)

# Получаем аргументы из командной строки и добавляем немножко описания.
parser = argparse.ArgumentParser(
        prog='Burrows-Wheeler transform',
        description='Use index value "-1" to do direct transform',
        epilog='Thanks for using this program!'
        )
parser.add_argument('str')
parser.add_argument('index', type=int)
args = parser.parse_args()

# Проверяем входные данные и выводим ответ, если всё ок.
if args.index < -1:
    print('Please, use correct index value ')
    sys.exit()
elif args.index == -1:
    print(direct_bwt(args.str))
else:
    print(inverse_bwt(args.index, args.str))
