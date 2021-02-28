from prettytable import PrettyTable
import numpy as np

a_values = np.random.randint(1, 20, 4)
x1_values = np.random.randint(1, 20, 8)
x2_values = np.random.randint(1, 20, 8)
x3_values = np.random.randint(1, 20, 8)

x0_list = [(max(x1_values) + min(x1_values)) / 2,
           (max(x2_values) + min(x2_values)) / 2,
           (max(x3_values) + min(x3_values)) / 2]

dx_list = [x0_list[0] - min(x1_values),
           x0_list[1] - min(x2_values),
           x0_list[2] - min(x3_values)]

y_list = []
for i in range(len(x1_values)):
    y_list.append(
        a_values[0] + a_values[1] * x1_values[i] + a_values[2] * x2_values[i] + a_values[3] * x3_values[i])
    i += 1

y_etalon = a_values[0] + a_values[1] * x0_list[0] + a_values[2] * x0_list[1] + a_values[3] * x0_list[2]

xn1_list = []
xn2_list = []
xn3_list = []

for i in range(len(x1_values)):
    xn1_list.append('%.1f' % ((x1_values[i] - x0_list[0]) / dx_list[0]))
    xn2_list.append('%.1f' % ((x2_values[i] - x0_list[1]) / dx_list[1]))
    xn3_list.append('%.1f' % ((x3_values[i] - x0_list[2]) / dx_list[2]))
    i += 1

y_average = sum(y_list) / len(y_list)
answer = min(y_list)
for i in y_list:
    if i < y_average:
        if abs(y_average - i) < abs(y_average - answer):
            if i < y_average:
                answer = i

table1 = PrettyTable()

table1.field_names = ["a0", "a1", "a2", "a3"]
table1.add_row(a_values)

table2 = PrettyTable()

table2.add_column("№", [1, 2, 3, 4, 5, 6, 7, 8])
table2.add_column("X1", x1_values)
table2.add_column("X2", x2_values)
table2.add_column("X3", x3_values)
table2.add_column("Y", y_list)
table2.add_column("Xn1", xn1_list)
table2.add_column("Xn2", xn2_list)
table2.add_column("Xn3", xn3_list)

table3 = PrettyTable()

table3.add_column("№", ["X1", "X2", "X3"])
table3.add_column("X0", x0_list)
table3.add_column("Dx", dx_list)

table4 = PrettyTable()

table4.field_names = ["Y etalon", "Y average", "Answer on a task"]
table4.add_row([y_etalon, y_average, answer])

print(table1)
print(table2)
print(table3)
print(table4)
