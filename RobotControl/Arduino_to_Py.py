import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animate(i, data, ser): 
    if ser.in_waiting:
        line = ser.readline()
        string = line.decode().rstrip()
        try:
            num = float(string)
            print(num)
            data.append(num)
        except:
            pass
    else:
        pass
    data = data[-360:]

    ax.clear()
    ax.plot(data)
    ax.set_ylim([-11, 11])
    ax.set_xlim([0, 360])
    ax.set_title('Plot of Serial Data From Arduino')
    ax.set_xlabel('deg')
    ax.set_ylabel('Amplitude')

data = []
fig, ax = plt.subplots()
ser = serial.Serial('COM10', 9600, timeout=1)
ser.flush()

ani = animation.FuncAnimation(fig, animate, fargs=(data, ser), interval = 1, cache_frame_data=False)

plt.show()
