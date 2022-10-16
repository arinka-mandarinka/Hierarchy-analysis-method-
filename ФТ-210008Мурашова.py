import math

# Проверка на ввод числа.
def input_int(text):
    while True:
        try:
            n = int(input(text))
        except:
            print('Ошибка: введено неверное значение! Попробуйте ещё раз...')
            continue
        return n

countOfCriteria = input_int('Введите количество критериев: ')

matrix = []

# Строим единичную матрицу.
for i in range(countOfCriteria):
    line = []
    for j in range(countOfCriteria):
        if i == j:
            line.append(1)
        else:
            line.append(0)
    matrix.append(line)

# Пользователь заполняет матрицу с одной стороны от единиц, другая сторона зеркалится в виде 1 / matrix[i][j].
for i in range(countOfCriteria):
    for j in range(countOfCriteria):
        if matrix[i][j] == 1:
            break
        matrix[i][j] = input_int(f'Введите числовой элемент для ячейки [{i + 1}][{j + 1}] : ')
        matrix[j][i] = matrix[0][0] / matrix[i][j]

mults = []
for row in matrix:
    # Перемножение чисел.
    multiLine = 1
    for column in row:
        multiLine *= column
    # Находим корень произведений всех чисел строки.
    mults.append(math.pow(multiLine, 1 / countOfCriteria))
    
# Находим сумму всех значений.
sumAllMult = 0
for element in mults:
    sumAllMult += element

# Рассчитываем весовые коэффициенты.
coefficients = [round(mults[i] / sumAllMult, 2) for i in range(len(mults))]

# Выводим результаты.
for i in range(len(coefficients)):
    print(f'Весовой коэффициент для {i + 1}-го критерия: {coefficients[i]}')

