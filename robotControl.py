import serial

ser = serial.Serial('COM5', 9600, timeout=1)
ser.flush()

while(1):
    hold = input("Left, Right, Stop: ")
    if(hold.lower() == "left"):
        print(hold)
        buf = str(-1)
        print(buf)
        ser.write(buf.encode())
    elif(hold.lower() == "right"):
        print(hold)
        buf = str(1)
        print(buf)
        ser.write(buf.encode())
    else:
        print(hold)
        buf = str(0)
        print(buf)
        ser.write(buf.encode())

ser.close