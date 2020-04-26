# Домашнее задание 1 (№45)

ФИ: Енгибарян Нарек


Напишите реализацию прямого и обратного преобразования Барроуза-Уилера (https://neerc.ifmo.ru/wiki/index.php?title=%D0%9F%D1%80%D0%B5%D0%BE%D0%B1%D1%80%D0%B0%D0%B7%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5_%D0%91%D0%B0%D1%80%D1%80%D0%BE%D1%83%D0%B7%D0%B0-%D0%A3%D0%B8%D0%BB%D0%B5%D1%80%D0%B0) с расчетами на видеокарте через CUDA. Алфавит используйте латинский, только большие буквы.

Входные данные:
Строка и номер строки в отсортированной матрице. Если номер не равен -1, то происходит обратное преобразование, иначе прямое.

Выходные данные: преобразованная строка и ее номер в случае прямого преобразования, только строка в случае обратного преобразования.

Для работы с матрицами используйте cupy (https://cupy.chainer.org/). Если нет cuda-совместимой видеокарты, используйте Google Colab (https://colab.research.google.com/). В этом случае использование argparse не требуется.
