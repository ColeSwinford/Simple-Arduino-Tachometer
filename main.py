import serial
import time

#### Create .txt file ####
current_time = time.strftime("%m/%d/%Y_%H.%M.%S")
graph_data = open('data_{}.txt'.format(time.strftime("%m.%d.%Y-%H.%M.%S")), 'w+')
graph_data.write('Format: rpm, time(seconds)\n\n')

#### Arduino Data ####
arduinoData = serial.Serial('com3', 115200)
while True:
    ### Receive data from Arduino ###
    while arduinoData.inWaiting() == 0: # do nothing while there's no data
        pass # do nothing

    dataPacket = arduinoData.readline().decode('ascii') # read the data from the arduino
    graph_data.write(dataPacket)
    graph_data.flush()
