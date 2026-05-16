import matplotlib.pyplot as plt
import numpy as np

psi20 = [-3.9,-5.0,-5.0,-4.6,-3.9,-3.6,-3.4,-3.2,-3.0]
psi25 = [-4.6,-6.1,-6.1,-5.5,-4.6,-4.3,-4.0,-3.8,-3.6]
psi30 = [-5.4,-7.0,-7.2,-6.7,-5.3,-5.0,-4.7,-4.5,-4.2]
psi35 = [-6.1,-7.5,-7.8,-8.4,-6.0,-5.6,-5.4,-5.2,-4.8]
psi40 = [-6.9,-7.9,-8.2,-9.8,-7.6,-6.3,-6.0,-5.7,-5.4]
xpos = [0.07613, 0.09578, 0.19303, 0.37623, 0.49607, 0.59479, 0.69400, 0.79224]
full_data = [psi20, psi25, psi30, psi35, psi40]

gamma = 1.4

psi_to_bar = lambda p : p * 0.0689476 if not isinstance(p, list) else [psi_to_bar(i) for i in p]
abs_p = lambda p : p + P_atm if not isinstance(p, list) else [abs_p(i) for i in p]
conv = lambda p: abs_p(psi_to_bar(p))
cp = lambda p, p_inf, m : 2/(1.4 * m**2) * (p/p_inf - 1) if not isinstance(p, list) else [cp(i,p_inf,m) for i in p]
P_atm = psi_to_bar(14.6)
M = lambda P: ((2 / (gamma - 1)) * (((P0 / P) ** ((gamma - 1) / gamma)) - 1)) ** 0.5 if not isinstance(P, list) else [M(i) for i in P]
pratio = lambda m: (1 + (gamma-1)/2 * m**2)**(-(gamma)/(gamma-1)) if not isinstance(m, list) else [pratio(i) for i in m]
pg = lambda cp,m: cp/(abs(1-m**2))**0.5 if not isinstance(m, list) else [pg(cp,i) for i in m]
P0 = P_atm
print(P0)

full_data = conv(full_data)
legend_lis = [20, 25, 30, 35, 40]


plt.style.use('seaborn-v0_8-whitegrid')  # clean modern style

plt.rcParams.update({
    'font.size': 14,          # base size
    'axes.titlesize': 18,     # title
    'axes.labelsize': 16,     # x/y labels
    'xtick.labelsize': 14,
    'ytick.labelsize': 14,
    'legend.fontsize': 14     # legend text
})

#GRAPH 1 : P VS X/C

plt.figure(figsize=(10,6))
for i,lis in enumerate(full_data):
    p_free = lis[0]
    mach = M(p_free)
    plt.plot(xpos, lis[1:], marker='o', label=f"{legend_lis[i]} psi | M∞ = {mach:.2f}")


plt.legend(frameon=True)
plt.xlabel("x/c Position on Airfoil")
plt.ylabel("Absolute Pressure (bar)")
plt.title("Pressure Variation Along NACA0012 Airfoil")
plt.savefig(fname='pressure_variation', dpi=600, bbox_inches='tight')
plt.show()

#GRAPH 2 : MACH VS X/C

plt.figure(figsize=(10,6))
for i,lis in enumerate(full_data):
    p_free = lis[0]
    mach = M(p_free)
    plt.plot(xpos, M(lis[1:]), marker='o', label=f"{legend_lis[i]} psi | M∞ = {mach:.2f}")

plt.axhline(y=1, linestyle='--', color='magenta')
plt.legend(frameon=True)
plt.xlabel("x/c Position on Airfoil")
plt.ylabel("Local Mach Number")
plt.title("Local Mach Number Variation Along NACA0012 Airfoil")
plt.savefig(fname='mach_variation', dpi=600, bbox_inches='tight')
plt.show()

#GRAPH 3 : P/P0 VS M
x1 = list(np.linspace(0,2,300))
x2 = list(np.linspace(0,0.9,300))

if 1 in x1: x1.remove(1)
y1 = pratio(x1)
Cp_inc = -0.414
y2 = pg(Cp_inc, x2)

plt.figure(figsize=(10,6))
plt.xlabel("Mach Number")
plt.plot(x1,y1, label='Pressure Ratio P/P0')
plt.plot(x2,np.abs(y2), label='Compressible CP')
plt.axvline(x=0.783761, ymax=(0.6), linestyle='--', color='green')
plt.scatter([0.783761], [0.6666], color='green', marker='o', label=f'Critical Mach Number\nMcr = 0.783761')
plt.legend(frameon=True)
plt.title("Theoretical Critical Mach Number Estimation")
plt.savefig(fname='critical_mach', dpi=600, bbox_inches='tight')
plt.show()

