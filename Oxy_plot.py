import matplotlib.pyplot as plt
import time
import sys

if __name__ == "__main__":

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    xs = []
    ys = []
    y2 = []

    oxyM = []
    temp = []

    fname = sys.argv[1]

    f = open(fname,'r')
    lines = f.readlines()[1:]
    f.close()

    for reply in lines:
        # Create figure for plotting

        if reply != '\n':

            reply = reply.rstrip('\r\n')

            print(reply)

            reply = reply.split(';',5)
            temp = reply[3]
            temp = temp.replace('T','')
            oxy = reply[4]
            oxy = oxy.replace('O','')

            if '-' in oxy:
                oxy = oxy.replace('-','0')
                oxy = float(oxy)/-1000

            else:
                oxy = float(oxy)/1000

            temp = float(temp)/100
            

            print('O2%: {0:.3f}'.format(oxy))
            print('Temp: {0:.2f}'.format(temp))
            print('----------------------------')

            # Add x and y to lists
            ys.append(oxy)
            y2.append(temp)

    xs = range(0,len(ys))

    print(oxy)

    # Limit x and y lists to 200 items (This is about the sweet spot without overloading my laptop)
    xs = xs[-200:]
    ys = ys[-200:]
    y2 = y2[-200:]

    print()

    # Draw x and y lists
    ax.clear()
    ax.plot(xs, ys, y2)

    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Oxybase Dissolved O2')
    plt.ylabel('O2 (%)')

    plt.show()
