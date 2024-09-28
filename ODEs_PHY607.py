import numpy as np
import matplotlib.pyplot as plt

#Numerical Parameters
t = 10   #Total time
N = 10000   #Number of points in interval.
Interval = np.linspace(0, t, N) # interval
dx = t/N   #Spacing

#Initial Conditions
v0 = 1  #Some initial velocity
x0 = 0  #Starting at rest
omega = 1   #Frequency

#Storing variables
Variables = np.array([x0,v0], float) #For updating variables
x = [] #For storing positions x
v = [] #For storing velocities v
E = [] #For storing energy


#Vector field driving the dynamics
def f(r, omega):   
    x = r[0]    #Position
    v = r[1]    #Velocity
    fx = v
    fv = -omega**2*x
    return np.array([fx, fv], float)

#Energy
def Energy(r, omega):
    x = r[0]    #Position
    v = r[1]    #Velocity
    return v**2/2 + omega**2*x**2/2
    

####Euler's Method
#for i in Interval:
#    x.append(Variables[0])  #Store previous position
#    v.append(Variables[1])  #Store previous velocity
#    E.append(Energy(Variables, omega))
#    Variables += dx*f(Variables, omega)

####4th-order Runge-Kutta Method
for i in Interval:
    x.append(Variables[0])  #Store previous position
    v.append(Variables[1])  #Store previous velocity
    E.append(Energy(Variables, omega))
    k1 = dx*f(Variables, omega)
    k2 = dx*f(Variables + 0.5*k1, omega)
    k3 = dx*f(Variables + 0.5*k2, omega)
    k4 = dx*f(Variables + k3, omega)
    Variables+= (k1 + 2*k2 + 2*k3 + k4)/6




#Plotting Position vs time
#fig, ax = plt.subplots()
#ax.plot(Interval, x)
#ax.set(xlabel="t (time)", ylabel="x (position)", title="Position vs time (Runge-Kutta)")
#fig.savefig("position_time_runge.png")

#Comparing to analytical solution
#fig2, ax2 = plt.subplots()
#ax2.plot(Interval, x, label = "Numerical")
#ax2.plot(Interval, v0/omega*np.sin(omega*Interval), label = "Analytical")
#ax2.set(xlabel="t (time)", ylabel="x (position)", title="Position vs time (Runge-Kutta)")
#ax2.legend()
#fig2.savefig("Comparison_Runge.png")



#Plotting Energy vs time
#fig3, ax3 = plt.subplots()
#ax3.plot(Interval, E)
#ax3.set_ylim([0, 1])
#ax3.set(xlabel="t (time)", ylabel="E (Energy)", title="Energy vs time (Runge-Kutta)")
#fig3.savefig("Energy_time_runge.png")
