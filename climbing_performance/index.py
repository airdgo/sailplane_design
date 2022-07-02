# ============================================================================
# Climbing Performance / Performanțe la zborul în urcare
# ============================================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def sec(phi):
    cos_value = np.cos(phi)
    sec_value = 1/cos_value
    return sec_value

def calculateSpeeds(i):
    Vx = np.sqrt(2*W/rho/Cl[i]/S)
    Vz = np.sqrt(2*Cd[i]**2*W/rho/Cl[i]**3/S)
    return Vx, Vz

def annotate():
    labs = np.around(np.rad2deg(phi)).astype(int)
    degree_sign = u'\N{DEGREE SIGN}'
    for i, txt in enumerate(labs):
        plt.annotate(str(txt)+degree_sign, (r[i], -Vzphi[i]), textcoords="offset points",  xytext=(-7,8), ha="center")
        plt.annotate(str(txt)+degree_sign, (r[i], (VzTp-Vzphi)[i]), textcoords="offset points",  xytext=(-7,8), ha="center")

df = pd.read_csv("./Database/T7-VLM2-EF1(g1)-EF2(g1)-Inviscid+Drag-Final.csv")

g = 9.81 # m/s2
rho = 1.225 # kg/m3
W = 400 * g # N
S = 9.180 # m2
a = df["alpha"].to_numpy()
Cl = df[" CL"].to_numpy()
Cd = df[" CD"].to_numpy()

phi = np.radians(np.arange(20, 70, 10))

Vx, Vz = calculateSpeeds(10)

Vxphi = Vx*sec(phi)**(1/2)

Vzphi = Vz*sec(phi)**(3/2)

r = Vxphi**2/np.tan(phi)/g

rT = np.arange(10, 300, 10)
VzT = 2.3*(1-(rT/300)**2)
VzTp = 2.3*(1-(r/300)**2)

plt.figure(figsize=(8,5))
plt.title("Zbor în urcare")
plt.grid()
plt.xlabel("r [m]")
plt.ylabel(r"$V_z$ [m/s]")
plt.plot(rT, VzT, marker="o", label="Termica", color="darkorange")
plt.plot(r, VzTp-Vzphi, marker="o", label=r"$V_a$", color="green")
plt.plot(r, -Vzphi, marker="o", label=r"$V_{z\phi}$")
annotate()
plt.legend()
plt.show()