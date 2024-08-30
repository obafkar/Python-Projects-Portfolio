import math

# Define the parameters for the Hagen-Poiseuille equation
viscosity = float(input("Enter viscosity in cP: ")) # viscosity of the fluid in cP
flow_rate = float(input("Enter the inlet flow rate in uL/min: ")) # flow rate of the fluid in μL/min
length = float(input("Enter length of the channel in cm: ")) # length of the channel in cm
width = float(input("Enter the width of channel in um: ")) # width of the channel in μm
height = float(input("Enter the height of channel in um: ")) # height of the channel in μm

# Calculate the hydraulic diameter of the channel
area = width * height # cross-sectional area of the channel in μm^2
perimeter = 2 * (width + height) # wetted perimeter of the channel in μm
hydraulic_diameter = 4 * area/perimeter # hydraulic diameter of the channel in μm

# Use the Hagen-Poiseuille equation to calculate the pressure drop across the channel
pressure_drop = (128 * viscosity * length * flow_rate)/(math.pi * hydraulic_diameter ** 4)

# Print the pressure drop
print("############")
print("  ")
print("Pressure drop across the channel is:\n {:.2f} Pa".format(pressure_drop))
print("  ")
print("########################")
print("Calculation Was Successful :) \nThanks you!")
