import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import time

#### Graphing ####
# style.use('fiverThirtyEight')
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

current_time = time.strftime("%m/%d/%Y_%H.%M.%S")
graph_data = open('data_{}.txt'.format(time.strftime("%m.%d.%Y-%H.%M.%S")), 'w+')
# graph_data = open('data_{}.txt'.format(current_time), 'w+')
graph_data.write('Format: rpm, time(seconds)\n\n')
####

#### Arduino Data ####
arduinoData = serial.Serial('com3', 115200)
while True:
    ### Send data to Arduino ###
    # cmd = input("Enter command: ")
    # cmd = cmd + "\r"
    # arduinoData.write(cmd.encode())
    ###

    ### Receive data from Arduino
    while arduinoData.inWaiting() == 0: # wait here until there is data
        pass # do nothing

    dataPacket = arduinoData.readline().decode('ascii') # read the data from the arduino
    graph_data.write(dataPacket)
    graph_data.flush()
    print("data is:", dataPacket) # print the received data
####