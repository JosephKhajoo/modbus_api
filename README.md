This is a task to read data from a dummy MODBUS server and present it in json format with Swagger UI.
For running the python scripts you need to install requirements

$ pip3 install -r requirements.txt

First you need to start the dummy MODBUS server`

$ python3 modbus_server.py

Next, you have to run the Rest API to see the data.

$ python3 app.py

To test out and see the description of the API, open http://127.0.0.1:5000 in your browser.
