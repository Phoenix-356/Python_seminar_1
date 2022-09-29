""" Напишите программу, которая принимает на вход координаты точки (X и Y), 
причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
в которой находится эта точка (или на какой оси она находится). 
Пример: - x=34; y=-30 -> 4 - x=2; y=4-> 1 - x=-34; y=-30 -> 3  """


def inputKoord(x):
    a = [0] * x
    for i in range(x):
        coordinate = False
        while not coordinate:
            try:
                number = float(input(f"Введите {i+1} координату: "))
                a[i] = number
                coordinate = True
                if a[i] == 0:
                    coordinate = False
                    print("Координата не должна быть равна 0 ")
            except ValueError:
                print("Не число!")
    return a


def checkCoordinates(xy):
    quarter = 4
    if xy[0] > 0 and xy[1] > 0:
        quarter = 1
    elif xy[0] < 0 and xy[1] > 0:
        quarter = 2
    elif xy[0] < 0 and xy[1] < 0:
        quarter = 3
    print(f"Точка находится в {quarter} четверти плоскости")


koordinate = inputKoord(2)
checkCoordinates(koordinate)