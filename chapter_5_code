import cmath 
import math


def rlc_circuit(w,R,L,C):
   Zr = R
   if C == 0:
       Zc = 0
   else:
       Zc = complex(0, -(1/(w*C)))
       
   if L == 0:
       Zl = 0
   else:
       Zl = complex(0, w*L)
       
   Zeq = Zr + Zc + Zl
   
   I = Vs/Zeq
   print("\nThe magnitude of the current is: I =", abs(I), "Amps")
   print("and the phase is:", cmath.phase(I)*(180/math.pi), "degrees")
   
   print("\nIn rectangular coordinates, this is expressed as: I =", I)
   
   print("\nThe phases for each element are:")
   
   Vr = I*Zr
   Vc = I*Zc
   Vl = I*Zl
   
   print("Vr =", abs(Vr), "<", cmath.phase(Vr)*(180/math.pi), "degrees" )
   print("Vc =", abs(Vc), "<", cmath.phase(Vc)*(180/math.pi), "degrees" )
   print("Vl =", abs(Vl), "<", cmath.phase(Vl)*(180/math.pi), "degrees" )
   
   print("\nIn rectangular coordinates, these are expressed as: ")
   print("Vr =", Vr)
   print("Vc =", Vc)
   print("Vl =", Vl)
   
   print("\nThe total complex impedance is: Zeq =", abs(Zeq), "<", cmath.phase(Zeq)*(180/math.pi), "degrees")
   print("\nIn rectangular coordinates it is: Zeq =", Zeq)



print("The source voltage has a maximum amplitude of 10 Volts and no phase shift.")   
w = float(input("Enter an angular frequency: "))
R = float(input("Enter resistance (Ohm): "))
C = float(input("Enter capacitance (Farad): "))
L = float(input("Enter inductance (Henry): "))

Vs = complex(10, 0)

rlc_circuit(w,R,L,C)
