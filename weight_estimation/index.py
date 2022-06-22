# ============================================================================
# Sailplane Empty and Gross weight Estimation / 
# Estimarea greutății planorului gol și maxim echipat
# ============================================================================

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Read aerodynamic characteristics form the Database
df = pd.read_excel("./Date/Database.xlsx")

b = df["b"].to_numpy()
me = df["We"].to_numpy()
m0 = df["W0"].to_numpy()

sailplane = np.array([15, 170])

plt.figure(figsize=(8,5))
plt.title("Estimarea masei planorului gol")
plt.xlabel("b [m]")
plt.ylabel("m [kg]")
plt.scatter(b, me, label="Planoare din baza de date")
plt.scatter(sailplane[0], sailplane[1], c="black", label="Planorul proiectat")
z = np.polyfit(b, me, 1)
p = np.poly1d(z)
plt.plot(b, p(b), "r", label="Interpolare")
plt.legend()
plt.show()