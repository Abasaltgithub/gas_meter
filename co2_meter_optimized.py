import serial
import matplotlib.pyplot as plt
import nidaqmx
from nidaqmx import constants as ni_const
import time
import sys

# Replace 'COMX' with the actual serial port of your Arduino (e.g., 'COM3' on Windows or '/dev/ttyUSB0' on Linux)
ser = serial.Serial('COM11', 115200, timeout=2)

temperature_data = []
humidity_data = []
co2_data = []

plt.ion()  # Enable interactive plotting
fig, axs = plt.subplots(3, 1, figsize=(8, 8))

# Adjust vertical spacing between subplots
plt.subplots_adjust(hspace=0.5)

# Create a Task for the NI card
with nidaqmx.Task() as task:
    task.do_channels.add_do_chan("Dev2/port1/line0")  # Assuming you're using 'Dev1' and 'line0' (PFI 0/P1.0)

    running = [True]  # Use a list to store the running flag

    def key_event(event):
        if event.key == '0':
            running[0] = False

    fig.canvas.mpl_connect('key_press_event', key_event)  # Bind the custom key event function

    try:
        while running[0]:
            line = ser.readline().decode('utf-8').strip()
            if line.startswith("Temperature:"):
                _, temp_str = line.split(":")
                temperature_data.append(float(temp_str.split("degrees C")[0]))
            elif line.startswith("Relative Humidity:"):
                _, humidity_str = line.split(":")
                humidity_data.append(float(humidity_str.split("%")[0]))
            elif line.startswith("CO2:"):
                _, co2_str = line.split(":")
                co2_percentage = float(co2_str.split("%")[0])
                co2_data.append(co2_percentage)

                # Check if CO2 percentage exceeds 3%
                if co2_percentage > 3.0:
                    task.write(True)  # Send a 5V signal
                else:
                    task.write(False)  # Turn off the signal

            if len(temperature_data) > 1000:
                # Keep the last 1000 data points for plotting
                temperature_data.pop(0)
                humidity_data.pop(0)
                co2_data.pop(0)

            # Plot the data
            axs[0].clear()
            axs[1].clear()
            axs[2].clear()
            axs[0].set_ylabel('Temperature (°C)')
            axs[0].plot(temperature_data, 'r')
            axs[1].set_ylabel('Relative Humidity (%)')
            axs[1].plot(humidity_data, 'g')
            axs[2].set_ylabel('CO2 (%)')
            axs[2].set_xlabel('Time (s)')
            axs[2].plot(co2_data, 'b')

            plt.pause(0.01)

    except KeyboardInterrupt:
        pass
    finally:
        task.write(True)  # Turn off the signal
        ser.close()

print("Plot closed. Exiting...")
sys.exit(0)  # Exit the program
