# RPi_Pico_Communication
Communication implementations for Raspberry Pi Pico W/WH

##UART
Communication through UART from your RPi Pico and computer is already established if you have it connected through USB.

The communication port can only be used by one device at a time, so your RPi Pico has to run its program through main.py

print() - function in your micropython has UART communication with your PC

###How to save to file:
On Pico:
Write your code that you whant to send, save as a main.py file

On PC:
run your reading/saving script connected to the port the RPi pico is connected to

