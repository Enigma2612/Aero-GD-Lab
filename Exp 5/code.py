import numpy as np
import matplotlib.pyplot as plt
import math

#CONSTANTS
M = 1.8



#FUNCTIONS

def cos(theta): return math.cos(math.radians(theta))
def sin(theta): return math.sin(math.radians(theta))

p1_mat = lambda alpha: np.arra([-cos(5-alpha), sin(5-alpha)])
p2_mat = lambda alpha: np.arra([-sin(5+alpha), -cos(5+alpha)])
p3_mat = lambda alpha: np.arra([cos(5+alpha), cos(5+alpha)])
p4_mat = lambda alpha: np.arra([-sin(5-alpha), cos(5-alpha)])

def get_forces_and_coeffs(p1,p2,p3,p4,alpha):
    f = p1_mat(alpha)*p1 + p2_mat(alpha)*p2 + p3_mat(alpha)*p3 + p4_mat(alpha)*p4

    drag, lift = f[0], f[1]

