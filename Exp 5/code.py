import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd
from math import sqrt

#CONSTANTS
M = 1.8
T0 = 298 #K
T = T0/(1 + 0.2 * M**2)
U = M * sqrt(1.4 * 287 * T)
rho = 1.225 / (1 + 0.2 * M**2)**(1/0.4)
P0 = 1.01325
P = P0 / (1 + 0.2*M**2)**(7/2)
q = 0.5 * rho * U**2

#FUNCTIONS

def cos(theta): return math.cos(math.radians(theta))
def sin(theta): return math.sin(math.radians(theta))

p1_mat = lambda alpha: np.array([sin(5-alpha), -cos(5-alpha)])
p2_mat = lambda alpha: np.array([-sin(5+alpha), -cos(5+alpha)])
p3_mat = lambda alpha: np.array([sin(5+alpha), cos(5+alpha)])
p4_mat = lambda alpha: np.array([-sin(5-alpha), cos(5-alpha)])

def get_forces_and_coeffs(p1,p2,p3,p4,alpha):
    f = p1_mat(alpha)*p1 + p2_mat(alpha)*p2 + p3_mat(alpha)*p3 + p4_mat(alpha)*p4

    cd = f[0] / (q * 2 * cos(5))
    cl = f[1] / (q * 2 * cos(5))

    return f,cd,cl


def get_data(alpha):
    df = pd.read_excel(f"Readings/{alpha}deg.xlsx")
    df2 = pd.read_excel(f"Readings/{-alpha}deg.xlsx")
    p1 = df.iloc[4,4+26]
    p2 = df.iloc[4,4+27]
    p3 = df2.iloc[4,4+26]
    p4 = df2.iloc[4,4+27]

    return np.round((np.array([p1,p2,p3,p4]) + P0)*1e5,5)

Real_Cds = {}
Real_Cls = {}

for alpha in [0,2,4]:
    f,cd,cl = get_forces_and_coeffs(*get_data(alpha), alpha)
    Real_Cds[alpha] = round(float(cd),4)
    Real_Cls[alpha] = round(float(cl),4)

# print("CD")
# print(Real_Cds)
# print("CL")
# print(Real_Cls)

Theoretical_Cls = {}
Theoretical_Cds = {}
Theoretical_Ps = {0:np.array([1.29, 0.77, 1.29, 0.77])*P*1e5,
                  2:np.array([1.17, 0.7, 1.43, 0.84])*P*1e5,
                  4:np.array([1.05, 0.599, 1.58, 0.948])*P*1e5,
                  }

for alpha in Theoretical_Ps:
    ps = Theoretical_Ps[alpha]
    _,cd,cl = get_forces_and_coeffs(*ps, alpha)
    Theoretical_Cls[alpha] = round(float(cl),4)
    Theoretical_Cds[alpha] = round(float(cd),4)


print(f"{Theoretical_Cds=}")
print(f"{Real_Cds=}")
print()
print(f"{Theoretical_Cls=}")
print(f"{Real_Cls=}")

alphas = [0,2,4]
colors = ['#1f77b4',  # blue
          '#d62728',  # red
          '#2ca02c',  # green
          '#ff7f0e',  # orange
          '#9467bd',  # purple
          "#1693a1"]  # cyan

plt.plot(alphas, Theoretical_Cds.values(), label="Theory CD Values", marker='o', color=colors[2])
plt.plot(alphas, Real_Cds.values(), label="Experimental CD Values", marker='o', color=colors[3])
plt.legend()
plt.xlabel("Angle of attack (in degrees)")
plt.ylabel("Coefficient of Drag")
plt.title("Coefficient of Drag vs Angle of Attack for Diamond Wedge")
plt.savefig(fname='cd', dpi=300, bbox_inches='tight')
plt.show()
plt.plot(alphas, Theoretical_Cls.values(), label="Theory CL Values", marker='o', color=colors[1])
plt.plot(alphas, Real_Cls.values(), label="Experimental CL Values", marker='o', color=colors[5])
plt.legend()
plt.xlabel("Angle of attack (in degrees)")
plt.ylabel("Coefficient of Lift")
plt.title("Coefficient of Lift vs Angle of Attack for Diamond Wedge")
plt.savefig(fname='cl', dpi=300, bbox_inches='tight')
plt.show()