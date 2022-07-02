# ======================================================================
# Gliding Flight / Zbor planat
# ======================================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read aerodynamic characteristics exported from XFLR5
df = pd.read_csv("./Database/T7-VLM2-EF1(g1)-EF2(g1)-Inviscid+Drag-Final.csv")

g = 9.81 # m/s2
rho = 1.225 # kg/m3
W = 400 * g # N
S = 9.180 # m2
a = df["alpha"].to_numpy()
Cl = df[" CL"].to_numpy()
Cd = df[" CD"].to_numpy()
phi = np.radians(np.arange(0, 70, 10))

Vx = np.sqrt(2*W/rho/Cl/S)

Vz = np.sqrt(2*Cd**2*W/rho/Cl**3/S)

def sec(phi):
    cos_value = np.cos(phi)
    sec_value = 1/cos_value
    return sec_value

def Vxphi(phi):
    return Vx*sec(phi)**(1/2)

def Vzphi(phi):
    return Vz*sec(phi)**(3/2)

# Plot flight performance for different bank angles
def plot_flight_performance():
    for i in phi:
        plt.plot(Vxphi(i), Vzphi(i), marker="o", label=f"{np.rint(np.rad2deg(i))}$^\circ$")

def calculate_gamma_min():
    VzMin = np.min(Vz)
    VzMinIndex = np.where(V == VzMin for V in Vz)
    Vmin = Vx[VzMinIndex]
    GAMin = np.arctan(VzMin/Vmin)
    return GAMin
print(Vz[0])
plt.figure(figsize=(8,5))
plt.title("Zbor planat")
plt.grid()
plt.xlabel(r"$V_x$ [km/h]")
plt.ylabel(r"$V_z$ [m/s]")
plt.plot(Vxphi(0)*3.6, Vzphi(0), marker="o")
plt.plot(Vx[0]*3.6, Vz[0], "o", label="Viteza minimă de zbor")
plt.gca().invert_yaxis()
plt.legend()
plt.show()
