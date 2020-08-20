import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import serial

reply = ''

ser= serial.Serial(
    port='/dev/ttyUSB0', #serial port the object should read
    baudrate= 19200,      #rate at which information is transfered over comm channel
    parity=serial.PARITY_NONE, #no parity checking
    stopbits=serial.STOPBITS_ONE, #pattern of bits to expect which indicates the end of a character
    bytesize=serial.EIGHTBITS, #number of data bits
    timeout=1
)

# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []
y2 = []

# Begin H2M data mode
ser.write(b'mode0001\r')

timestr = str(time.strftime("%Y%m-%d_%H-%M-%S"))

file_name = "./OXYBASE" + timestr

file = open(file_name,"a+")

file.write(file_name + "\r\n")

start_time = dt.datetime.now().strftime('%H:%M:%S.%f')

# This function is called periodically from FuncAnimation
def animate(i, xs, ys, y2):

    ser.flushInput()
    ser.flushOutput()

    # Read data
    ser.write(b'data\r')

    reply = ser.read_until('\r')

    reply = '\n' + reply

    file.write(reply)

    #print(reply)

    # Parse Message for graph

    reply = reply.split(';',5)

    temp = reply[3]
    temp = temp.replace('T','')
    oxy = reply[4]
    oxy = oxy.replace('O','')

    temp = float(temp)/100
    oxy = float(oxy)/1000

    print('O2%: {0:.3f}'.format(oxy))
    print('Temp: {0:.2f}'.format(temp))

    # Add x and y to lists
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(oxy)
    y2.append(temp)

    # Limit x and y lists to 200 items
    xs = xs[-200:]
    ys = ys[-200:]
    y2 = y2[-200:]

    # Draw x and y lists
    ax.clear()
    ax.plot(xs, ys, y2)

    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Oxybase Dissolved O2 (Start:' + start_time + ')')
    plt.ylabel('O2 (%)')

# Set up plot to call animate() function periodically


ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys, y2), interval=500)
plt.show()

ser.write(b'mode0000\r')

ser.flushInput()
ser.flushOutput()