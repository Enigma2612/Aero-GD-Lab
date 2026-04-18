import csv
import math
import os
import numpy as np
from pprint import pprint
import matplotlib.pyplot as plt


P0_atm = 1.01325

def load_data(file):
    with open(file, 'r') as f:
        reader = csv.reader(f)
        lis1, lis2 = [],[]
        for a,b in reader:
            a.lstrip(); a.rstrip(); b.lstrip(); b.rstrip()
            lis1.append(float(a))
            lis2.append(float(b) + P0_atm) 
        return lis1,lis2


def setup():
    plt.style.use('seaborn-v0_8-whitegrid')
    plt.rcParams.update({
    "font.size": 14,
    "axes.titlesize": 16,
    "axes.labelsize": 14,
    "legend.fontsize": 12
})


setup()

#overexp

plt.figure(figsize=(8, 5))  # gives space for labels/title

x, P0 = load_data("Data/over_data.csv")

plt.plot(
    x, P0,
    linestyle=':',
    color='tab:blue',          # seaborn default blue line
    marker='o',
    markerfacecolor='white',   # clean contrast
    markeredgecolor='tab:blue',
    markeredgewidth=1.5,
    markersize=8,
    label='Data points'
)

plt.xlabel("X Position (mm)")
plt.ylabel("P0 (bar)")
plt.title("Stagnation Pressure Variation for Overexpanded Jet")
plt.legend()
plt.tight_layout()

plt.show()

#Graph 2


#overexp

plt.figure(figsize=(8, 5))  # gives space for labels/title

x, P0 = load_data("Data/under_data.csv")

plt.plot(
    x, P0,
    linestyle=':',
    color='tab:orange',          # seaborn default blue line
    marker='o',
    markerfacecolor='white',   # clean contrast
    markeredgecolor='tab:orange',
    markeredgewidth=1.5,
    markersize=8,
    label='Data points'
)

plt.xlabel("X Position (mm)")
plt.ylabel("P0 (bar)")
plt.title("Stagnation Pressure Variation for Underexpanded Jet")
plt.legend()
plt.tight_layout()

plt.show()
