import csv
psi_to_bar = lambda p : p * 0.0689476
abs_p = lambda p : p + P_atm

P01 = abs_p(psi_to_bar(-0.5))
P02 = abs_p(psi_to_bar(-2.38))
P_atm = 1.01325

P_2_M2 = []
P_neg_2_M2 = []

m1_free = []



with open('Data/5psi/-2_M1.csv') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        m1_free.append(row[1])
        needed = row[2:4] + row[5:6] + row[6:]

