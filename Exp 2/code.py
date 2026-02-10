import matplotlib.pyplot as plt

#bar (gage)
pressures = [
    -0.172, -0.266, -0.275, -0.322, -0.383,
    -0.450, -0.513, -0.581, -0.625, -0.657,
    -0.682, -0.696, -0.709, -0.708, -0.718,
    -0.696, -0.706, -0.719, -0.704, -0.695,
    -0.707, -0.700, -0.693, -0.698, -0.687
]

#mm
positions = [
    19.5, 44.5, 69.5, 94.5, 119.5, 144.5, 169.5, 194.5,
    219.5, 244.5, 269.5, 294.5, 319.5, 344.5, 369.5, 394.5,
    419.5, 444.5, 469.5, 494.5, 519.5, 544.5, 569.5, 594.5, 619.5
]

#mm
heights = [
    112.10, 94.94, 86.30, 81.15, 78.86, 78.25, 79.37, 81.47,
    83.86, 86.26, 88.46, 90.36, 91.91, 93.16, 94.17, 95.01,
    95.80, 96.55, 97.30, 98.05, 98.80, 99.55, 100.06, 100.55, 101.05
]

width = 25.4 #mm
P0 = 6.2 #bar
h_throat = 78.24 #mm

area_ratios = [h/h_throat for h in heights]

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

regimes = ['sub']*6 + ['sup']*19
mach = lambda p: (((P0/p)**(2/7) - 1)*5)**0.5
mach_nos = [mach(P0+p) for p in pressures]

calc_mach_nos = [find_mach(area_ratios[i], 10e-10, regime=regimes[i]) for i in range(len(area_ratios))]

print(mach_nos)

# for i in range(len(pressures)):
#     s = fr"{i+1} & {positions[i]} & {pressures[i]} & {heights[i]} \\"
#     print(s)

# for i in range(len(pressures)):
#     s = fr"{i+1} & {positions[i]} & {round(mach_nos[i],3)} & {round(calc_mach_nos[i],3)}\\"
#     print(s)

plt.figure(figsize=(10,6))
plt.scatter(positions[:25], mach_nos, label='Mach Nos. (From Pressure)', color='red', marker='o', facecolors='none', s=100, linewidths=2)
plt.plot(positions[:25], mach_nos, color='red')
plt.scatter(positions[:25], calc_mach_nos, label='Mach Nos. (From Area Ratio)', color='blue')
plt.plot(positions[:25], calc_mach_nos, color='blue')
# plt.scatter([positions[5]], [mach_nos[5]], label='Throat Mach No.', color='darkorange', marker='s', s=70)
# plt.hlines(y=mach_nos[5], xmin=-1, xmax=positions[5], color='darkorange', linestyle='dashed')
# plt.scatter([positions[5]], [calc_mach_nos[5]], label='Throat Mach No.', color='blue', marker='s', s=70)
plt.xlabel("Tapping Position (mm)")
plt.ylabel("Mach Number")
plt.legend()
plt.grid()
plt.title("Mach Number vs Position")
plt.savefig(fname='graph2', dpi=300, bbox_inches='tight')
plt.show()