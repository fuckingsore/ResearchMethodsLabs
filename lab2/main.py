import numpy as np
from prettytable import PrettyTable
import math
import sys

# 1 пункт
print("1.Запишемо лінійне рівняння регресії: \n y = b0 + b1 * x1 + b2 * x2")
print()

# 2-3 пункти
m = 5
x1_min = -30
x1_max = 0
x2_min = 10
x2_max = 60
y_min = 120
y_max = 220
y_array = np.random.randint(y_min, y_max, size=(3, m))

table1 = PrettyTable()

table1.field_names = ["№", "X1", "X2", "Y1", "Y2", "Y3", "Y4", "Y5"]
table1.add_rows([
    ['1', x1_min, x2_min, y_array[0][0], y_array[0][1], y_array[0][2], y_array[0][3], y_array[0][4]],
    ['2', x1_max, x2_min, y_array[1][0], y_array[1][1], y_array[1][2], y_array[1][3], y_array[1][4]],
    ['3', x1_min, x2_max, y_array[2][0], y_array[2][1], y_array[2][2], y_array[2][3], y_array[2][4]]
])
print("2.Нормована матриця планування експерименту:")
print(table1)
print()

print("3.Знайдемо середнє значення функції відгуку в рядку та дисперсії по рядках:")
print()

y_average = [np.mean(y_array[0]), np.mean(y_array[1]), np.mean(y_array[2])]

deviation1 = []  # відхилення
deviation2 = []
deviation3 = []
for i in range(len(y_array[0])):
    deviation1.append((y_array[0][i] - y_average[0]) ** 2)
    deviation2.append((y_array[1][i] - y_average[1]) ** 2)
    deviation3.append((y_array[2][i] - y_average[2]) ** 2)
    i += 1

dispersion = [round(np.mean(deviation1), 2),
              round(np.mean(deviation2), 2),
              round(np.mean(deviation3), 2)]

table2 = PrettyTable()
table2.field_names = ["", "[0]", "[1]", "[2]"]
table2.add_row(["Y average", y_average[0], y_average[1], y_average[2]])
table2.add_row(["Dispersion", dispersion[0], dispersion[1], dispersion[2]])
print(table2)
print()

print("4.Обчислимо основне відхилення:")
deviation_main = round(math.sqrt((2 * (2 * m - 2)) / (m * (m - 4))), 3)
print("Основне відхилення дорівнює ", deviation_main)
print()

print("5.Обчислимо Fuv, TETAuv, Ruv:")
f_uv = [round(dispersion[0] / dispersion[1], 3),
        round(dispersion[2] / dispersion[0], 3),
        round(dispersion[2] / dispersion[1], 3)]

teta_uv = [round((m - 2 / m) * f_uv[0], 3),
           round((m - 2 / m) * f_uv[1], 3),
           round((m - 2 / m) * f_uv[2], 3)]

r_uv = [round(abs(teta_uv[0] - 1) / deviation_main, 3),
        round(abs(teta_uv[1] - 1) / deviation_main, 3),
        round(abs(teta_uv[2] - 1) / deviation_main, 3)]

table3 = PrettyTable()
table3.field_names = ["", "[0]", "[1]", "[2]"]
table3.add_row(["Fuv", f_uv[0], f_uv[1], f_uv[2]])
table3.add_row(["TETAuv", teta_uv[0], teta_uv[1], teta_uv[2]])
table3.add_row(["Ruv", r_uv[0], r_uv[1], r_uv[2]])
print(table3)
print()

print("6.Перевірка дисперсії на однорідність:")
r_kr = 2.16  # для m=6 і довірчою ймовірністю р=0.9
for i in range(len(r_uv)):
    if r_uv[i] > r_kr:
        print("Неоднорідна дисперсія, повторіть експеримент.")
        sys.exit()
print("Дисперсія однорідна, можна продовжити експеримент.")
print()

print("7.Розрахунок нормованих коефіцієнтів рівняння регресії.")
xn = [[-1, -1], [1, -1], [-1, 1]]
mx1 = round((xn[0][0] + xn[1][0] + xn[2][0]) / 3, 4)
mx2 = round((xn[0][1] + xn[1][1] + xn[2][1]) / 3, 4)
my = round((y_average[0] + y_average[1] + y_average[2]) / 3, 4)
a1 = round((xn[0][0] ** 2 + xn[1][0] ** 2 + xn[2][0] ** 2) / 3, 4)
a2 = round((xn[0][0] * xn[0][1] + xn[1][0] * xn[1][1] + xn[2][0] * xn[2][1]) / 3, 4)
a3 = round((xn[0][1] ** 2 + xn[1][1] ** 2 + xn[2][1] ** 2) / 3, 4)
a11 = round((xn[0][0] * y_average[0] + xn[1][0] * y_average[1] + xn[2][0] * y_average[2]) / 3, 4)
a22 = round((xn[0][1] * y_average[0] + xn[1][1] * y_average[1] + xn[2][1] * y_average[2]) / 3, 4)

matrix = [[1, mx1, mx2],
          [mx1, a1, a2],
          [mx2, a2, a3]]
vector = [my, a11, a22]
solution = np.linalg.solve(matrix, vector)
b0 = round(solution[0], 4)
b1 = round(solution[1], 4)
b2 = round(solution[2], 4)

table4 = PrettyTable()
table4.field_names = ["mx1", "mx2", "my", "a1", "a2", "a3", "a11", "a22", "b0", "b1", "b2"]
table4.add_row([mx1, mx2, my, a1, a2, a3, a11, a22, b0, b1, b2])
print(table4)
print()

print("Отже, нормоване рівняння регресії:")
print("y = ", b0, " + (", b1, ") * x1 + (", b2, ") * x2")
y1_norm = round(b0 + b1 * xn[0][0] + b2 * xn[0][1], 1)
y2_norm = round(b0 + b1 * xn[1][0] + b2 * xn[1][1], 1)
y3_norm = round(b0 + b1 * xn[2][0] + b2 * xn[2][1], 1)

table5 = PrettyTable()
table5.field_names = ["Y1", "Y2", "Y3"]
table5.add_row([y1_norm, y2_norm, y3_norm])
print(table5)

if y1_norm == y_average[0] and y2_norm == y_average[1] and y3_norm == y_average[2]:
    print("Результати збігаються з середніми значеннями Y. \nОтже, коефіцієнти нормованого рівняння регресії вірні.")
else:
    print("Результати не збіглись або округлення неправильно вплинуло на результат.")
print()

print("8.Проведемо натуралізацію коефіцієнтів:")
delta_x1 = abs(x1_max - x1_min) / 2
delta_x2 = abs(x2_max - x2_min) / 2
x10 = (x1_max + x1_min) / 2
x20 = (x2_max + x2_min) / 2

aa0 = b0 - (b1 * x10 / delta_x1) - (b2 * x20 / delta_x2)
aa1 = b1 / delta_x1
aa2 = b2 / delta_x2

table6 = PrettyTable()
table6.field_names = ["Delta X1", "Delta X2", "X10", "X20", "a0", "a1", "a2"]
table6.add_row([delta_x1, delta_x2, x10, x20, aa0, aa1, aa2])
print(table6)
print()

print("Запишемо натуралізоване рівняння регресії:")
print("у = ", aa0, "+ (", aa1, ") * x1 + )", aa2, ") * x2")

y1_natur = round(aa0 + aa1 * x1_min + aa2 * x2_min, 1)
y2_natur = round(aa0 + aa1 * x1_max + aa2 * x2_min, 1)
y3_natur = round(aa0 + aa1 * x1_min + aa2 * x2_max, 1)

table7 = PrettyTable()
table7.field_names = ["Y1", "Y2", "Y3"]
table7.add_row([y1_natur, y2_natur, y3_natur])
print(table7)

if y1_natur == y1_norm and y2_natur == y2_norm and y3_natur == y3_norm:
    print("Результат збігається з середніми значеннями. \nОтже, коефіцієнти натуралізованого рівняння регресії вірні.")
else:
    print("Результати не збіглись або округлення неправильно вплинуло на результат.")
