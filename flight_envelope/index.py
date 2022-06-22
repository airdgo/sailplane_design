# ============================================================================
# Flight Envelope / Anvelopa de zbor
# ============================================================================

import numpy as np
import matplotlib.pyplot as plt

MANEUVER_DIAGRAM_COLOR = "steelblue"
POSITIVE_GUST = "green"
NEGATIVE_GUST = "red"

# Constants
rho = 1.225 # kg/m3
g = 9.81
W = 350 * g # N Maximum takeoff weight
m = W/g # kg plane mass
CLmax = 1.483828 # maximum lift coefficient of the wing
CLmaxNeg = -0.8 # maximum negative lift coefficient 
CDmin = 0.008472 # lowest possible drag coefficient of the sailplane
S = 9.180 # m2 wing area
b = 15 # m wing span
MGC = 0.61 # mean geometric chord

# Limit manoeuvring load factors
n1 = 6
n2 = 4
n3 = -2
n4 = -3

# air speed function
def V(n, CL):
    return np.sqrt(2*np.abs(n)*W/rho/np.abs(CL)/S)

# Design air speeds m/s

# Estimated stalling speed at design maximum weight
VSp = V(1, CLmax)
VSn = V(1, CLmaxNeg)

# Design manoeuvring speed
VA = V(n1, CLmax)

# Design Gust Speed VB. VB must not be less than VA.
VB = 65

# Design Maximum Speed chosen by the applicant:
VD = (9*W/S/10*0.2084+78)*0.514444
VE = VD

# VG
VG = V(n4, CLmaxNeg)

A = [VA, n1]
D = [VD, n2]
E = [VE, n3]
G = [VG, n4]

Vel = [A[0], D[0], E[0], G[0]]
n = [A[1], D[1], E[1], G[1]]

positive_factors = np.linspace(0, n1)
negative_factors = np.linspace(0, n4)
pf_velocities = V(positive_factors, CLmax)
nf_velocities = V(negative_factors, CLmaxNeg)

def n_stall(Vst, CL):
    return Vst**2*rho*CL*S/W/2

def plotManeuverDiagram():
    plt.plot(Vel, n, marker="o", label="Diagrama de manevră", color=MANEUVER_DIAGRAM_COLOR)
    plt.plot(pf_velocities, positive_factors, color=MANEUVER_DIAGRAM_COLOR)
    plt.plot(nf_velocities, negative_factors, color=MANEUVER_DIAGRAM_COLOR)

    plt.plot([VSp, VSp], [0, n_stall(VSp, CLmax)], color=MANEUVER_DIAGRAM_COLOR)
    plt.plot([VSn, VSn], [0, n_stall(VSn, CLmaxNeg)], color=MANEUVER_DIAGRAM_COLOR)

    plt.annotate(r"$V_S^+$", (VSp, n_stall(VSp, CLmax)), textcoords="offset points",  xytext=(10,-10), ha="center")
    plt.annotate(r"$V_S^-$", (VSn, n_stall(VSn, CLmaxNeg)), textcoords="offset points",  xytext=(10,5), ha="center")
    plt.annotate("A", (VA, n1), textcoords="offset points",  xytext=(-6,8), ha="center")
    plt.annotate("D", (VD, n2), textcoords="offset points",  xytext=(5,5), ha="center")
    plt.annotate("E", (VE, n3), textcoords="offset points",  xytext=(5,5), ha="center")
    plt.annotate("G", (VG, n4), textcoords="offset points",  xytext=(-5,-15), ha="center")

# Gust diagram

U = np.array([-15, -7.5, 7.5, 15]) # m/s gust speed
w0 = np.array([VB, VD, VD, VB]) # m/s air speed

# slope of wing lift curve calculus
# ========================
k = 0.9
l = b*b/S

a = (2*k*np.pi)*np.pi*l/(2*k*np.pi+np.pi*l) # slope of wing lift curve / rad
#=========================

miu = 2*m/S/(rho*MGC*a) # non-dimensional sailplane mass ratio
k = 0.88*miu/(5.3+miu) # gust alleviation factor

def nGust(U, V):
    return 1 + k/2*rho*U*V*a/(m*g/S)

def plotGustDiagram(U, V):
    for i in range(len(U)):
        color = NEGATIVE_GUST if (i < 2) else POSITIVE_GUST
        gf = nGust(U[i], V[i])
        xCoords = np.linspace(0, V[i], 5)
        yCoords = np.linspace(1, gf, 5)
        plt.plot(xCoords, yCoords, "--", color=color)

    plt.plot([w0[0], w0[1]], [nGust(U[0], w0[0]), nGust(U[1], w0[1])], "--", color=NEGATIVE_GUST, label="Rafală negativă")
    plt.plot([w0[0], w0[1]], [nGust(U[3], w0[3]), nGust(U[2], w0[2])], "--", color=POSITIVE_GUST, label="Rafală pozitivă")
    plt.plot([w0[1], w0[2]], [nGust(U[1], w0[1]), nGust(U[2],w0[2])], color=MANEUVER_DIAGRAM_COLOR)
    plt.plot([w0[0], w0[3]], [nGust(U[0], w0[0]), nGust(U[3],w0[3])], color="gray")
    plt.annotate(r"$V_B$", (VB, 0), textcoords="offset points",  xytext=(10,0), ha="center")

plt.figure(figsize=(8, 5))
plt.title("Anvelopa de zbor")
plt.grid()
plotManeuverDiagram()
plotGustDiagram(U,w0)
plt.xlabel("V [m/s]")
plt.ylabel("n")
plt.legend()
plt.show()

