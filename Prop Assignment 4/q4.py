import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
import csv

#constants
T04 = 1130
T06 = 2000
T = 225
P = 26.5e3
QR = 41.4e6
GAMMA = 1.4
PI_C = 7.2
CP = 1005
R = 287

TAU_C = PI_C ** ((GAMMA - 1)/(GAMMA))
THETA_B = T04 / T
A_INF = sqrt(GAMMA * R * T)

def get_variables(m_inf):
    theta_inf = 1 + (GAMMA - 1)/2 * m_inf**2

    tau_t = 1 - theta_inf/THETA_B * (TAU_C - 1)

    tau_b = THETA_B / (theta_inf * TAU_C)
    fb = CP/QR * T * (THETA_B - theta_inf * TAU_C)
    fb = max(fb,1e-10)
    me = sqrt((TAU_C * tau_t * theta_inf - 1)/(GAMMA-1) * 2)

    tau_ab = T06/(T04 * tau_t)
    fab = CP/QR * (T06 - tau_t * T04)
    fab = max(fab, 1e-10)

    t_ratio_without_ab = tau_b
    t_ratio_with_ab = tau_b * tau_ab

    return (fb, fab, me, t_ratio_without_ab, t_ratio_with_ab)


def get_specs(m_inf, ab = False):
    if not ab:
        f,_,me,t_ratio,_ = get_variables(m_inf)
    else:
        fb,fab,me,_,t_ratio = get_variables(m_inf)
        f = fb + fab


    Thrust_ND = ((1+f) * me * sqrt(t_ratio) - m_inf)
    tsfc = f / (Thrust_ND * A_INF)

    #efficiencies
    m_inf += 1e-10
    m_ratio = me/m_inf
    n_th = (m_inf**2 * A_INF**2 * (m_ratio**2 * t_ratio - 1))/(2 * f * QR)
    n_p = 2/(m_ratio * sqrt(t_ratio) + 1)
    n_o = n_th * n_p

    return (Thrust_ND, tsfc, n_th, n_p, n_o)


#Without AB
TND_no_ab, TSFC_no_ab, N_TH_no_ab, N_P_no_ab, N_O_no_ab = non_ab_specs = [[],[],[],[],[]]
TND_ab, TSFC_ab, N_TH_ab, N_P_ab, N_O_ab = ab_specs = [[],[],[],[],[]]
specs_gen = []
M_vals = []
M_vals2 = []

for m in range(51):
    m /= 10
    s = get_specs(m, False)
    if s[0] >= 0:
        M_vals.append(m)
        for i,e in enumerate(s):
            non_ab_specs[i].append(e)
    else:
        break

for m in range(51):
    m /= 10
    sab = get_specs(m, True)
    theta_inf = 1 + (GAMMA - 1)/2 * m**2
    if theta_inf * T * TAU_C >= T04:
        break
    if sab[0] >= 0:
        M_vals2.append(m)
        for i,e in enumerate(sab):
            ab_specs[i].append(e)
    else:
        break

#non ab plot
plt.plot(M_vals, TND_no_ab, marker='o', markersize=4, label='Without Afterburner')
plt.plot(M_vals2, TND_ab, marker='o', markersize=4, label='With Afterburner')
plt.legend()
plt.title("Non Dimensional Thrust vs M inf")
plt.xlabel("M inf")
plt.ylabel("Non Dimensional Thrust")
plt.savefig(fname='NDT', dpi=500, bbox_inches='tight')
plt.show()

plt.plot(M_vals, TSFC_no_ab , marker='o', markersize=4, label="Without Afterburner")
plt.plot(M_vals2, TSFC_ab , marker='o', markersize=4, label='With Afterburner')
plt.legend()
plt.title("TSFC vs M inf")
plt.xlabel("M inf")
plt.ylabel("TSFC")
plt.savefig(fname='TSFC', dpi=500, bbox_inches='tight')
plt.show()

plt.plot(M_vals, N_TH_no_ab , label='Thermal Efficiency', marker='o', markersize=4)
plt.plot(M_vals, N_P_no_ab , label = 'Propulsive Efficiency', marker='o', markersize=4)
plt.plot(M_vals, N_O_no_ab , label = 'Overall Efficiency', marker='o', markersize=4)
plt.title("Efficiency vs M inf (Without Afterburner)")
plt.legend()
plt.xlabel("M inf")
plt.ylabel("Efficiency")
plt.savefig(fname='Eff_no_ab', dpi=500, bbox_inches='tight')
plt.show()

plt.plot(M_vals2, N_TH_ab , label='Thermal Efficiency', marker='o', markersize=4)
plt.plot(M_vals2, N_P_ab , label = 'Propulsive Efficiency', marker='o', markersize=4)
plt.plot(M_vals2, N_O_ab , label = 'Overall Efficiency', marker='o', markersize=4)
plt.title("Efficiency vs M inf (With Afterburner)")
plt.legend()
plt.xlabel("M inf")
plt.ylabel("Efficiency")
plt.savefig(fname='Eff_ab', dpi=500, bbox_inches='tight')
plt.show()

    