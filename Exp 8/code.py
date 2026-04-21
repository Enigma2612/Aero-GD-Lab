import csv

P_atm = 1.01325
psi_to_bar = lambda p : p * 0.0689476 if not isinstance(p, list) else [i * 0.0689476 for i in p]
abs_p = lambda p : p + P_atm if not isinstance(p, list) else [i + P_atm for i in p]
conv = lambda p: abs_p(psi_to_bar(p))

P01 = conv(-0.5)
P02 = conv(-2.38)

P1_free = -0.8
P2_free = -3.9



#just copying the pressures cuz I don't like file handling lol

P_neg_2_M1 = conv([-0.7,-0.7,-0.8,-0.7,-0.7,-0.7,-0.6,-0.7])
P_2_M1 = conv([-1,-1,-0.9,-0.7,-0.6,-0.7,-0.6,-0.6])
P_neg_2_M2 = conv([-3.6,-3.7,-4,-3.6,-3.4,-3.3,-3.2,-3])
P_2_M2 = conv([-5.1,-5,-4.7,-3.9,-3.6,-3.4,-3.2,-3])

