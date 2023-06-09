# Simple-Arduino-Tachometer
Simple Arduino tachometer and Python script that saves data in a .txt file. This code is designed for a hall effect sensor with a HIGH voltage that changes to LOW when near a magnet. However, it should work with any sensor, just use RISING or FALLING appropriately

## Arduino
- Created with Arduino Uno R3
- Uses interrupts for sensor reading and uses micros() for the highest data accuracy.
- Designed to be used with a hall effect sensor connected to Digital Pin 2, where the sensor has a default state of HIGH and goes to a LOW state when a magnet nears it

## Python
- Creates a .txt file in the format data_month.day.year-hour.minute,second.txt (Note: hour is in 24 hour format, so 0-24)
- Writes data to the .txt file, continuously saving it
- Automatically selects the com port if there is only one detected
- Warns user that there are no ports detected and gives the option to scan again for ports
- Gives user option to select port if there are multiple detected
