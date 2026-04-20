import csv

P01 = ...
P02 = ...
P_atm = 1.01325

P_2_M1 = []
P_neg_2_M1 = []
P_2_M2 = []
P_neg_2_M2 = []

psi_to_bar = lambda p : p * 0.0689476
abs_p = lambda p : p + P_atm

