import csv
import matplotlib.pyplot as plt


with open('data.csv', newline='\n') as f:
    r = csv.reader(f)
    pressures = []
    for line in r:
        pres = []
        for i,p in enumerate(line):
            pres.append(int(p))
        pressures.append(pres)
    
    pressures = pressures[:-1]

P0 = 1013.25 #mbar

positions = [33, 54, 78, 114, 168]
dias = [12, 14.2, 17.6, 22.6, 30.2]
areas = [d**2 for d in dias]
throat_area = 12**2

area_ratios = [a/throat_area for a in areas]

area_ratio = lambda m: 1/m * (2/2.4 * (1 + 0.2*m**2))**3
def find_mach(ar, thresh, regime='sub'):
    if regime == 'sub':
        l,r = 0.01, 1
        ans = l
    else:
        r,l = 1,1000
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

machs_down = [(find_mach(area_ratios[0], 1e-10, 'sub'), positions[0])] \
+ [(find_mach(area_ratios[i], 1e-10, 'sup'), positions[i]) for i in range(len(area_ratios))] \

machs_up = [(find_mach(area_ratios[0], 1e-10, 'sub'), positions[0])] \
+ [(find_mach(area_ratios[i], 1e-10, 'sub'), positions[i]) for i in range(len(area_ratios))] 


p_ratio_from_mach = lambda m: (1 + 0.2*m**2)**(-3.5)

ideal_pratios_up = [(p_ratio_from_mach(m[0]), m[1])[::-1] for m in machs_up]
ideal_pratios_down = [(p_ratio_from_mach(m[0]), m[1])[::-1] for m in machs_down]

p_ratio = lambda p : (p + P0) / P0

p_ratios = [[p_ratio(p) for p in line] for line in pressures]

markers = ['s', 'o', '^']
colors = ['#1f77b4',  # blue
          '#d62728',  # red
          '#2ca02c',  # green
          '#ff7f0e',  # orange
          '#9467bd',  # purple
          '#17becf']  # cyan

plt.figure(figsize=(9,6))
plt.grid()
for i, p in enumerate(p_ratios):
    plt.scatter(positions, p, label=f'Data Set {i+1}', marker=markers[i%3], facecolors='none', edgecolors=colors[i], s=50, linewidths=1.5)
    plt.plot(positions, p, color=colors[i])

control_colors = ['#000000',  # black
                  "#eb18ac"]  # magenta/pink
plt.scatter(*zip(*ideal_pratios_up), color=control_colors[0])
plt.plot(*zip(*ideal_pratios_up), color=control_colors[0], label='Ideal Subsonic Recovery')
plt.scatter(*zip(*ideal_pratios_down), color=control_colors[1])
plt.plot(*zip(*ideal_pratios_down), color=control_colors[1], label='Ideal Supersonic Flow')
plt.legend()
plt.xlabel('Tapping Positions (mm)')
plt.ylabel('Pressure Ratios (P/P0)')
plt.title("Graph of Pressure Ratio vs Tapping Position")
plt.savefig(fname='graph', bbox_inches='tight', dpi=300)
plt.show()