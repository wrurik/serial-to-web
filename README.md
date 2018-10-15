# serial-to-web

This project can be used to read lines from a serial port and send the data to an API.
It uses python. To get it working on a clean Raspbian Stretch you must first install Python and some extra modules:

- apt-get install python3 python3-serial python3-pip
- pip3 install pyserial
- pip3 install python-dotenv

Now copy `.env.example` to `.env` and setup the variables for your situation.

`SERIAL_PORT` => The serial port that should be read
`SERIAL_BAUDRATE` => Baudrate of the serial port 
`MESSAGE_START` => The first line of your message
`MESSAGE_LINES` => The number of lines that should be included in the API-call
`URL` => Your API endpoint

Now you can run `python3 read.py` to start sending data to your API