import numpy as np
import matplotlib.pyplot as plt

P_atm = 1.01325
psi_to_bar = lambda p : p * 0.0689476 if not isinstance(p, list) else [psi_to_bar(i) for i in p]
abs_p = lambda p : p + P_atm if not isinstance(p, list) else [abs_p(i) for i in p]
conv = lambda p: abs_p(psi_to_bar(p))
cp = lambda p, p_inf, m : 2/(1.4 * m**2) * (p/p_inf - 1) if not isinstance(p, list) else [cp(i,p_inf,m) for i in p]

xpos = [0.07613, 0.09578, 0.19303, 0.37623, 0.49607, 0.59479, 0.69400, 0.79224]

P02 = conv(-0.5)
P01 = conv(-2.38)

P2_free_pos = conv(-0.8)
P1_free_pos = conv(-3.9)

m1 = (((P01/P1_free_pos)**(2/7)-1)*5)**0.5
m2 = (((P02/P2_free_pos)**(2/7)-1)*5)**0.5

print(m1, m2)

#just copying the pressures cuz I don't like file handling lol

P_2_M2 = conv([-1,-1,-0.9,-0.7,-0.6,-0.7,-0.6,-0.6])


P_2_M1 = conv([-5.1,-5,-4.7,-3.9,-3.6,-3.4,-3.2,-3])
P_2_n_M1 = conv([-3.6,-3.7,-4,-3.6,-3.4,-3.3,-3.2,-3])
P_4_M1 = conv([-5.6,-5.4,-4.9,-4,-3.6,-3.4,-3.2,-3])
P_4_n_M1 = conv([-3.3,-3.5,-3.9,-3.6,-3.4,-3.3,-3.2,-3])
P_0_M1 = conv([-4.3,-4.3,-4.3,-3.7,-3.5,-3.3,-3.1,-3])



plot_lis_1 = [P_0_M1, P_2_M1, P_2_n_M1, P_4_M1, P_4_n_M1]
leg_lis = ['α = 0˚', 'α = 2˚', 'α = -2˚', 'α = 4˚', 'α = -4˚']

tab_lis_1 = list(zip(*cp(plot_lis_1, P1_free_pos, m1)))

r = lambda x,n: round(x, n) if not isinstance(x, list) else [r(i,n) for i in x]

# print("| x/c | α = 0˚ | α = 2˚ | α = -2˚ | α = 4˚ | α = -4˚|")
# for i,lis in enumerate(tab_lis_1):
#     a = r' & '.join([str(x) for x in [xpos[i]] + r(list(lis),3)]) + r' \\'
#     print(a)

cp_pos_1 = np.array(cp(P_2_M1, P1_free_pos, m1))
cp_pos_2 = np.array(cp(P_2_M2, P2_free_pos, m2))


ratio = ((1-m2**2)/(1-m1**2))**0.5

e = lambda a,b : abs((a-b)/a * 100)

for i in range(len(xpos)):
    cpratio = (cp_pos_1[i]/cp_pos_2[i])
    s = fr'{xpos[i]} & {cpratio:.3f} & {ratio:.3f} & {e(ratio, cpratio):.3f} \\'
    print(s)


plt.style.use('seaborn-v0_8-whitegrid')

# ---- Plot 1 ----

plt.figure()

for i,lis in enumerate(plot_lis_1):
    plt.plot(xpos, cp(lis, P1_free_pos, m1), marker='o', linestyle=':', label=leg_lis[i])
# plt.plot(xpos, cp_pos_2, marker='d', linestyle='--', label='Cp for M2')

plt.xlabel('X/C')

plt.ylabel('Coefficient of Pressure')

plt.title('CP Variation along the airfoil (Top Surface)')

plt.legend(frameon=True)
plt.savefig('cp_values', dpi=400, bbox_inches='tight')
plt.show()

# ---- Plot 2 ----

cpratio = (cp_pos_1) / (cp_pos_2)

plt.figure()

plt.plot(xpos, cpratio, marker='o', linestyle='', markersize=5, markeredgewidth=2, label='Cp Ratio')
plt.axhline(y=ratio, linestyle=':', label='Mach No. Ratio', color='tab:orange')  # horizontal dotted line

plt.xlabel('xpos')

plt.ylabel('Cp (M1) / Cp (M2)')
plt.legend(frameon=True)

plt.title('Cp Ratio Variation over the airfoil')
plt.savefig('ratio_comparison', dpi=400, bbox_inches='tight')
plt.show()
