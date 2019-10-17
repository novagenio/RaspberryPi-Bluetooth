# Importing the Bluetooth Socket library
import bluetooth
# Importing the GPIO library to use the GPIO pins of Raspberry pi
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)  # Using BCM numbering
host = ""
port = 1        # Raspberry Pi uses port 1 for Bluetooth Communication
###################################################
import time
from adafruit_servokit import ServoKit

# esto lo utilizamos solo para desactivar el gpo4, para cable colores
import RPi.GPIO as GPIO
GPIO.setup(4, GPIO.OUT)
GPIO.output(4, False)

#inicializa  8 cancles
kit = ServoKit(channels=8)
# Creaitng Socket Bluetooth RFCOMM communication
server = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
print('Bluetooth Socket Created')
try:
        server.bind((host, port))
        print("Bluetooth Binding Completed")
except:
        print("Bluetooth Binding Failed")

server.listen(1) # One connection at a time

# Server accepts the clients request and assigns a mac address.
client, address = server.accept()
print("Connected To", address)
print("Client:", client)
try:
        while True:
                # Receivng the data.
                data = client.recv(1024) # 1024 is the buffer size.
                data = data.decode("utf-8")                print(data)
                comando = data[0:2]
                print ("comando: " + comando)
                servo = data[1:2]
                print("servo: " + servo)
                valor = int(data[3:6])
                print("valor: " + str(valor))
                # mueve el servo, dependiendo de los valores recibidos
                kit.servo[int(servo)].angle = valor
                #time.sleep(1)

                # Sending the data.
                client.send(data)
except:
        # Making all the output pins LOW
        GPIO.cleanup()
        # Closing the client and server connection
        client.close()
        server.close()

                
