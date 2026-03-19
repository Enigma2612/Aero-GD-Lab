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

    drag, lift = f[0], f[1]

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
    Real_Cds[alpha] = float(cd)
    Real_Cls[alpha] = float(cl)

print("CD")
print(Real_Cds)
print("CL")
print(Real_Cls)
