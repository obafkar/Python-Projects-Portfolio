import math

# Define the parameters for the Navier-Stokes equations
viscosity = 998 # viscosity of the fluid in cP
radius = 0.05 # radius of the pipe in m
length = 0.1 # length of the pipe in m
flow_rate = 0.0003 # flow rate of the fluid in mL/min

# Calculate the average velocity of the fluid in the pipe
area = math.pi*radius**2 # cross-sectional area of the pipe in m^2
velocity = flow_rate/area # average velocity of the fluid in m/s

# Calculate the Reynolds number of the fluid in the pipe
reynolds_number = velocity*radius/viscosity # Reynolds number of the fluid

# Use the Navier-Stokes equations to calculate the velocity and pressure profile of the fluid in the pipe
if reynolds_number < 2300:
    # Laminar flow
    # Calculate the pressure drop across the pipe using Poiseuille's equation
    pressure_drop = (128*viscosity*length*flow_rate)/(math.pi*radius**4)
else:
    # Turbulent flow
    # Calculate the friction factor using the Moody chart
    friction_factor = 0.25 / ((math.log10(reynolds_number) - 2) ** 2)

    # Calculate the pressure drop across the pipe using the Darcy-Weisbach equation
    pressure_drop = friction_factor * length * velocity ** 2 / (2 * radius)

# Print the velocity and pressure profile of the fluid in the pipe
print("The average velocity of the fluid in the pipe is {:.2f} m/s".format(velocity))
print("The pressure drop across the pipe is {:.2f} Pa".format(pressure_drop))
