import matplotlib.pyplot as plt
import math

area_ratio = lambda m: 1/m * (2/2.4 * (1 + 0.2*m**2))**3
def find_mach(ar, thresh, regime='sub'):
    if regime == 'sub':
        l = 0.01
        r = 1
        ans = l
    else:
        r = 1
        l = 1000
        while area_ratio(l) < ar: l *= 10
        
    while abs(r-l) >= thresh:
        mid = l + (r-l)/2
        calc = area_ratio(mid)
        if calc > ar:
            l = mid
            ans = l
        else:
            r = mid
            ans = r
    return ans


rho = 1.225 #kg/m^3
Din = 0.034
De = 0.034
Dt = 0.012
A = math.pi * Din**2 / 4
P0 = 1013.25 #mbar

Vels = [10, 13.5, 16, 19, 22.6, 23.5, 24.4, 24.8, 25.0, 25.2, 25.3, 25.4, 25.44, 25.44, 25.44]
Pb = [-7, -11, -16, -24, -39, -46, -54, -61, -65, -71, -78, -97, -112, -158, -185]
Pt = [-38, -78, -110, -161, -251, -304, -343, -372, -394, -410, -430, -452, -456, -457, -457]


mass_flow = lambda v: v * rho * A
Pb_by_P0 = lambda p: (p+P0)/P0

mdot = [mass_flow(v) for v in Vels]
pratio = [Pb_by_P0(p) for p in Pb]


for i in range(len(Vels)):
    s = fr"{i+1} & {round(mdot[i],4)} & {round(pratio[i],3)} & {Pt[i]}\\"
    print(s)

plt.figure(figsize=(10,6))
plt.plot(pratio, mdot, color='blue')
plt.scatter(pratio, mdot, color='red', label='Calculated Values')
# plt.hlines(y=mdot[-1], xmin=pratio[-1], xmax=pratio[0], linewidth=1.5, linestyle='dashed', color='darkorange')
plt.legend()
plt.title("Graph between Mass Flow Rate and Pressure Ratio")
plt.xlabel("Pressure Ratio (Pb / P0)")
plt.ylabel("Mass Flow Rate (kg/s)")
plt.savefig(fname='graph', dpi=300, bbox_inches='tight')
plt.show()
