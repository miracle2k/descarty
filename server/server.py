import json
from datetime import datetime
from flask import Flask
from flask import request, abort
from pymongo import Connection, json_util

app = Flask(__name__)


connection = Connection('localhost', 27017)
db = connection.descarty


@app.route("/", methods=("GET", "POST",))
def index():
	url = request.values.get('url')
	if not url:
		abort(404)
		
	# Save the request
	document = {'url': url}
	if request.values.get('star', False):
		document['starred'] = True		
	db.pages.update({'url': url}, 
					{'$set': document, '$push': {'visits': datetime.utcnow()}}, True)

	# Get current state		
	document = db.pages.find_one({'url': url})
	return json.dumps({'url': document['url'], 'starred': document.get('starred', False)})


app.run(debug=True)
