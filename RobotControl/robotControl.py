import serial

ser = serial.Serial('COM5', 9600, timeout=1)
ser.flush()

while(1):
    hold = input("Left, Right, Stop: ")
    if(hold.lower() == "left"):
        print(hold)
        buf = str(-1)
        print(buf)
        ser.write(buf.encode()) # Send -1 to turn left on robot
    elif(hold.lower() == "right"):
        print(hold)
        buf = str(1)
        print(buf)
        ser.write(buf.encode()) # Send 1 to turn right on robot
    else:
        print(hold)
        buf = str(0)
        print(buf)
        ser.write(buf.encode()) # Send 0 to stop robot

ser.close