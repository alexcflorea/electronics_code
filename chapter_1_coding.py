def volt_div(vs, r1, r2, rl):
    req = 1 / ((1/r2)+(1/rl))
    
    vout = req/ (req + r1)
    
    print("The output voltage is",vout,"volts.")
    

print("Welcome to the Voltage Divider Calculator!")
volt_div(int(input("Please enter a source voltage in volts: ")), int(input("Enter a value for R1 in Ohms: ")), int(input("Enter a value for R2 in Ohms: ")), int(input("Enter a value for the load resistance in Ohms: ")))
    

extre = input("Would you like to view how load resistance affects output voltage? [Y/N]:")
extre = extre.upper()

if extre == "Y":
    print("For a source voltage of 10 V, R1 of 10 Ohms, R2 of 10 Ohms, and load resistance of 0.001 Ohm:")
    volt_div(10, 10, 10, 0.001)
    
    print("\n")
    
    print("For a source voltage of 10 V, R1 of 10 Ohms, R2 of 10 Ohms, and load resistance of 100,000 Ohms:")
    volt_div(10, 10, 10, 100000)
    
elif extre == "N":
    print("Goodbye")
    
