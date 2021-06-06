from flask_restplus import Api, Resource, fields, reqparse
from flask import Flask, request

# from models import UserModel
from pyModbusTCP.client import ModbusClient
import time

HOST = "127.0.0.1"
PORT = 12345

client = ModbusClient(host=HOST, port=PORT)

client.open()

# getting the data thats in the modbus registers
def get_data_modbus():
	while True:
	    if client.is_open():
	        regs = client.read_holding_registers(0, 4)
	    	
	        yield regs
	    time.sleep(1)


app = Flask(__name__)
api = Api(app)

app.config['RESTPLUS_MASK_SWAGGER'] = False

ns = api.namespace("data", description="The data that comes from the solar inverter")

data_field = api.model('Data', {
	"temperature" : fields.Integer(required=False, description='Temperature', example=2),
	"humidity" : fields.Integer(required=False, description='Humidity', example=220),
	"brightness" : fields.Integer(required=False, description='Brightness', example=20),
})

# data_field_parser = reqparse.RequestParser()
# data_field_parser.add_argument('Default', required=False, default='temerature')

@ns.route('/')
class User(Resource):

	# @ns.expect(data_field_parser)
	@ns.marshal_with(data_field)
	def get(self):
		"""
		Returns the data that came from the solar inverter via Modbus
		"""
		regs = next(get_data_modbus())
		print(regs)

		# args = data_field_parser.parse_args(request)
		# print(args)

		data = {
    		"temperature" : regs[0],
    		"humidity" : regs[1],
    		"brightness" : regs[2]
    	}

		return data

if __name__ == '__main__':
	app.run(debug=True)
