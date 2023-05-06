import serial
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

data = []
fig, ax = plt.subplots()
ser = serial.Serial('COM4', 9600, timeout=1)
line = ser.readline()
print(line)

def animate(i, data, ser):
    if ser.in_waiting:
        line = ser.readline()
        string = line.decode().strip()
        num = float(string)
        print(num)
        data.append(num)

    data = data[-100:]

    ax.clear()
    ax.plot(data)
    ax.set_title('Plot of Serial Data From Arduino')
    ax.set_xlabel('rads')
    ax.set_ylabel('Amplitude')

ani = FuncAnimation(fig, animate, fargs=(data, ser), interval = 100)



plt.show()