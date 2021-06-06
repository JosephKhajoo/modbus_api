# the DataBank is used to set values to the modbus server

from pyModbusTCP.server import ModbusServer, DataBank
from time import sleep
from random import uniform

server = ModbusServer('127.0.0.1', 12345, no_block=True)

try:
	print("Starting server...")
	server.start()

	state = [0]

	while True:

        # setting the data to random values.
		data = [int(uniform(1, 10)), int(uniform(200, 400)), int(uniform(1, 100))]
		DataBank.set_words(0, data)

        # if the state variable changes it means 
        # a new value has been written to the register and we should update it here
		if state != DataBank.get_words(1, 1):
			state = DataBank.get_words(1, 1)
			sleep(1)

except:
	print("\nServer shutdown...")
	server.stop()
