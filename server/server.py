from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/", methods=("GET", "POST",))
def index():
	print request.values.get('url'),  request.values.get('star')
	import time
	time.sleep(0.2)
	return '{"starred": true}'

app.run(debug=True)