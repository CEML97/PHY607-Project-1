import numpy as np
import matplotlib.pyplot as plt

#Function to Integrate
def f(x):
    return np.exp(-x**2)


#Parameters
x0 = 3    #End points of internal.
N = 10000   #Number of points in interval.
Interval = np.linspace(0, x0, N) # interval
dx = x0/N   #Spacing

####Riemann Sum

#Sum = 0 # Variable for final sum

#for i in Interval:  #Sum area of rectangles under the graph of the function
#    Sum += f(i)*dx

#print(abs(np.sqrt(np.pi) - 2*Sum)) #Printing Error
#Error = np.array([0.2788055978576447, 0.060082492636618134, 0.008263823019509342,8.364115571279918e-05]) #Values computed for different x0 =  np.array([1.0, 1.5, 2.0, 3.0])





####Trapezoidal Rule
#Sum = 0.5*f(0) + 0.5*f(x0)  #Part of the sum that only depends on the end points

#for i in range(1, N):  #Sum area of trapezoids under the graph of the function
#    Sum += f(0 + i*dx)

#print(abs(np.sqrt(np.pi) - 2*dx*Sum)) #Printing Error
#Error = np.array([0.2788055865069281, 0.06007706484145903, 0.008291069869085899, 3.9154397572183086e-05]) #Values computed for different x0 =  np.array([1.0, 1.5, 2.0, 3.0])






#### Simpson's Rule
#Sum = f(0) + f(x0)  #Part of the sum that only depends on the end points

#for i in range(1, N, 2): #Adding sum over odd terms.
    #Sum += 4*f(0 + i*dx)

#for i in range(2, N, 2): #Adding sum over even terms.
#    Sum += 2*f(0 + i*dx)

#print(abs(np.sqrt(np.pi) - 2*dx*Sum/3)) #Printing Error
# Error = np.array([0.2788055852806639, 0.06007706365570642, 0.008291069380677474, 3.915438647150715e-05]) #Values computed for different x0 =  np.array([1.0, 1.5, 2.0, 3.0])


#Plotting

X0s = np.array([1.0, 1.5, 2.0, 3.0]) #Values for the end points

fig, ax = plt.subplots()
ax.scatter(X0s, Error) #Use the provided values of Error given in each integration section
ax.set(xlabel="x0 (End Point)", ylabel="Error", title="Error as a function of Interval's end point (#Integration Technique#)")
fig.savefig("#Name#.png")