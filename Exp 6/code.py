area_ratio = lambda m: 1/m * (2/2.4 * (1 + 0.2*m**2))**3
def find_mach(ar, thresh=1e-15, regime='sub'):
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

#pressure ratio from area ratio:
p_ratio = lambda ar, reg: (1 + 0.2*(find_mach(ar, regime = reg)**2))**(-3.5)
                           

print(a:=area_ratio(1.5))
print(find_mach(a))