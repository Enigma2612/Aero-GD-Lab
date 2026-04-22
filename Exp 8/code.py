import numpy as np
import matplotlib.pyplot as plt

P_atm = 1.01325
psi_to_bar = lambda p : p * 0.0689476 if not isinstance(p, list) else [i * 0.0689476 for i in p]
abs_p = lambda p : p + P_atm if not isinstance(p, list) else [i + P_atm for i in p]
conv = lambda p: abs_p(psi_to_bar(p))
cp = lambda p, p_inf, m : 2/(1.4 * m**2) * (p/p_inf - 1) if not isinstance(p, list) else [cp(i,p_inf,m) for i in p]

xpos = [0.07613, 0.09578, 0.19303, 0.37623, 0.49607, 0.59479, 0.69400, 0.79224]

P01 = conv(-0.5)
P02 = conv(-2.38)

P1_free_pos = conv(-0.7)
P1_free_neg = conv(-0.8)
P2_free_pos = conv(-3.9)
P2_free_neg = conv(-3.8)

m1 = (((P01/P1_free_pos)**(2/7)-1)*5)**0.5
m2 = (((P02/P2_free_pos)**(2/7)-1)*5)**0.5

print(m1, m2)

#just copying the pressures cuz I don't like file handling lol

P_neg_2_M1 = conv([-0.7,-0.7,-0.8,-0.7,-0.7,-0.7,-0.6,-0.7])
P_2_M1 = conv([-1,-1,-0.9,-0.7,-0.6,-0.7,-0.6,-0.6])
P_neg_2_M2 = conv([-3.6,-3.7,-4,-3.6,-3.4,-3.3,-3.2,-3])
P_2_M2 = conv([-5.1,-5,-4.7,-3.9,-3.6,-3.4,-3.2,-3])


cp_neg_1 = np.array(cp(P_neg_2_M1, P1_free_neg, m1))
cp_pos_1 = np.array(cp(P_2_M1, P1_free_pos, m1))
cp_neg_2 = np.array(cp(P_neg_2_M2, P2_free_neg, m2))
cp_pos_2 = np.array(cp(P_2_M2, P2_free_pos, m2))


ratio = ((1-m2**2)/(1-m1**2))**0.5


plt.style.use('seaborn-v0_8-whitegrid')

# ---- Plot 1 ----

plt.figure()

plt.plot(xpos, cp_neg_1, marker='o', linestyle='--', label='Cp lower M1')

plt.plot(xpos, cp_pos_1, marker='s', linestyle='--', label='Cp upper M1')

plt.plot(xpos, cp_neg_2, marker='^', linestyle='--', label='Cp lower M2')

plt.plot(xpos, cp_pos_2, marker='d', linestyle='--', label='Cp upper M2')

plt.xlabel('X/C')

plt.ylabel('Coefficient of Pressure')

plt.title('CP Variation along the airfoil')

plt.legend()

plt.show()

# ---- Plot 2 ----

cpratio = (cp_pos_1 - cp_neg_1) / (cp_pos_2 - cp_neg_2)

plt.figure()

plt.plot(xpos, cpratio, marker='o', linestyle='--', label='Cp Ratio')
plt.axhline(y=ratio, linestyle=':', label='Mach No. Ratio', color='tab:orange')  # horizontal dotted line

plt.xlabel('xpos')

plt.ylabel('Cp (M1) / Cp (M2)')

plt.title('Cp Ratio Variation over the airfoil')

plt.show()
