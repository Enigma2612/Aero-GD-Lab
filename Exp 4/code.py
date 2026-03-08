import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os


pos = [
19.5, 44.5, 69.5, 94.5, 119.5, 144.5, 169.5,
194.5, 219.5, 244.5, 269.5, 294.5, 319.5,
344.5, 369.5, 394.5, 419.5, 444.5, 469.5,
494.5, 519.5, 544.5, 569.5, 594.5, 619.5
]

heights = [
112.18, 94.19, 82.19, 73.34, 67.78, 64.65, 63.50,
66.09, 71.06, 76.08, 80.75, 84.93, 88.53,
91.41, 93.69, 95.44, 96.72, 97.51, 98.08,
98.57, 99.07, 99.56, 100.06, 100.55, 101.05
]

throat_pos = 172.97
throat_height = 63.45

def get_pressures(file):
    df = pd.read_excel(f'data/{file}')

    row_index = 0
    value = 'Pressures (bar)'
    row = df.iloc[row_index]
    col_index = row[row == value].index[0]

    col_pos = df.columns.get_loc(col_index)
    return (np.array(df.iloc[i, col_pos : col_pos+25].to_list()) + P0)

P0 = 1.01325

lis = os.listdir('data/')
lis = sorted(lis, key=lambda i: float(i.rstrip('bar.xlsx')))

colors = ['#1f77b4',  # blue
          '#d62728',  # red
          '#2ca02c',  # green
          '#ff7f0e',  # orange
          '#9467bd',  # purple
          '#17becf']  # cyan

markers = ['s', '*', 'o', '^', 's']

plt.figure(figsize=(12,8))
for x,file_name in enumerate(lis):
    fname = file_name.rstrip('bar.xlsx')
    for i in range(5,9):
        pressures = get_pressures(file_name)
        plt.scatter(pos, pressures, color=colors[x])
        plt.plot(pos, pressures, color=colors[x], linewidth=1.6)
    plt.scatter(pos[-1], pressures[-1], color=colors[x], label=f"Poj = {fname} bar")
plt.legend()
plt.title("Pressure Distribution for different Total Jet Pressures")
plt.xlabel("Tapping Position (mm)")
plt.ylabel("Absolute Pressure (bar)")
plt.show()


