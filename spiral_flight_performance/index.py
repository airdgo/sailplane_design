# ============================================================================
# Spiral Flight Performance / Performanțe la zborul în spirală
# ============================================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("./Date/T7-VLM2-EF1(g1)-EF2(g1)-Inviscid+Drag-Final.csv")

g = 9.81 # m/s2
rho = 1.225 # kg/m3
W = 400 * g # N
S = 9.180 # m2
a = df["alpha"].to_numpy()
Cl = df[" CL"].to_numpy()
Cd = df[" CD"].to_numpy()
phi = np.radians(np.arange(20, 70, 10))

Vx = np.sqrt(2*W/rho/Cl/S)

Vz = np.sqrt(2*Cd**2*W/rho/Cl**3/S)

# Calculate secante
def sec(phi):
    cos_value = np.cos(phi)
    sec_value = 1/cos_value
    return sec_value

def Vxphi(phi):
    return Vx*sec(phi)**(1/2)

def Vzphi(phi):
    return Vz*sec(phi)**(3/2)

def plot_spiral_flight_performance():
    VminDive = []
    rminDive = []
    for i in phi:
        r = Vxphi(i)**2/np.tan(i)/g
        plt.plot(r, Vzphi(i), marker="o", label=f"{round(i*180/np.pi)}$^\circ$")
        minV = min(Vzphi(i))
        VzphiIndex = np.where(Vzphi(i) == minV)
        rminV = Vxphi(i)[VzphiIndex]**2/np.tan(i)/g
        VminDive.append(minV)
        rminDive.append(rminV)
    plt.plot(rminDive, VminDive, marker="o", label=r"$V_{zmin}$")
    plt.xlim(0,300)
    plt.ylim(0,3)
    plt.gca().invert_yaxis()

plt.figure(figsize=(8,5))

plt.title("Zbor în spirală")
plt.grid()
plt.xlabel("r [m]")
plt.ylabel(r"$V_{z\phi}$ [m/s]")
plot_spiral_flight_performance()
plt.legend()
plt.show()
