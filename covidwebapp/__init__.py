from flask import Flask
#from waitress import serve

app = Flask(__name__)
#serve(app, host='127.0.0.1', port=8080, threads=1)

from covidwebapp import routes