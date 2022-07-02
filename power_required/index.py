from matplotlib import markers
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("./Database/T7-VLM2-EF1(g1)-EF2(g1)-Inviscid+Drag-Final.csv")

W = 400*9.81
RHO = 1.225
S = 9.180

Cl = df[" CL"].to_numpy()
Cd = df[" CD"].to_numpy()

V = np.sqrt(2*W/RHO/S/Cl)

Pn = RHO/2*V**3*S*Cd

PnMin = np.min(Pn)
PnMinIndex = np.where(P == PnMin for P in Pn)
Vmin = V[PnMinIndex]

GAMin = np.arctan(PnMin/Vmin)

print("finetea maxima", np.tan(GAMin))

plt.figure(figsize=(8, 5))
plt.grid()
plt.title("Puterea necesara")
plt.xlabel("V [m/s]")
plt.ylabel("Pn [W]")
plt.xlim(20,50)
plt.ylim(1500,5000)
plt.plot(V, Pn, marker="o")
plt.show()