import matplotlib

matplotlib.use('TkAgg')  # Use the 'TkAgg' backend for interactive plotting

import matplotlib.pyplot as plt
from Phidget22.PhidgetException import *
from Phidget22.Phidget import *
from Phidget22.Devices.VoltageRatioInput import *
import traceback
import time
from datetime import datetime

# Define a global variable for pressure_data and ax
pressure_data = []
ax = None

# Delay (in seconds) between plot updates
plot_update_delay = 2.0  # Adjust this as needed


# Declare event handler for VoltageRatioInput0
def onVoltageRatioInput0_VoltageRatioChange(self, voltageRatio):
    global ax
    current_time = datetime.now()
    pressure_data.append((current_time, voltageRatio))

    if ax:
        # Update the plot periodically
        if current_time.second % plot_update_delay == 0:
            x_data, y_data = zip(*pressure_data)
            ax.clear()
            ax.plot(x_data, y_data)
            ax.set_xlabel('Time')
            ax.set_ylabel('Pressure (Voltage Ratio)')


try:
    # Create a VoltageRatioInput object for channel 0
    voltageRatioInput0 = VoltageRatioInput()
    voltageRatioInput0.setChannel(0)

    # Set the event handler for voltage ratio change
    voltageRatioInput0.setOnVoltageRatioChangeHandler(onVoltageRatioInput0_VoltageRatioChange)

    # Open the Phidget and wait for attachment
    voltageRatioInput0.openWaitForAttachment(5000)

    # Initialize Matplotlib plot
    fig, ax = plt.subplots()

    try:
        input("Press Enter to Stop and Close the Phidget\n")
    except (Exception, KeyboardInterrupt):
        pass

    # Close the Phidget
    voltageRatioInput0.close()

except PhidgetException as ex:
    traceback.print_exc()
    print("PhidgetException " + str(ex.code) + " (" + ex.description + "): " + ex.details)

