import math


kind = input("Are you calculateing dB for a Power reference or Voltage reference; Type \"P\" for Power, or \"V\" for voltage: ")


if kind == "P":
    reference = float(input("Enter your reference value in Watts now: "))
    actual = float(input("Enter your actual value in Watts now: "))
    dBp = 10*math.log10(actual/reference)
    print("A value of", actual, "is" ,dBp, "dB relative to" ,reference)
    
if kind == "V":
    reference = float(input("Enter your reference value in Volts now: "))
    actual = float(input("Enter your actual value in Volts now: "))    
    dBv = 20*math.log10(actual/reference)
    print("A value of", actual, "is" ,dBv, "dB relative to" ,reference)

