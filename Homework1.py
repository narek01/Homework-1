#import numpy as np
#import cupy as cp
import argparse
import sys

#Функция для прямого
def direct_bwt(str):
    return 0


def inverse_bwt(index, str):
    return 0


#Получаем аргументы из командной строки и добавляем немножко описания.
parser = argparse.ArgumentParser(
        prog='Burrows-Wheeler transform',
        description='Use index value "-1" to do direct transform',
        epilog='Thanks for using this program!'
        )
parser.add_argument('string')
parser.add_argument('index', type=int)
args = parser.parse_args()

#Проверяем входные данные и выводим ответ, если всё ок.
if args.index < -1:
    print('Please, use correct index value ')
    sys.exit()
elif args.index == -1:
    print(direct_bwt(args.string))
else:
    print(inverse_bwt(args.index, args.string))
