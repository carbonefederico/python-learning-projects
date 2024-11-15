from flask import Flask,request, redirect
from flask_cors import CORS
import string
import random
import os
from db_handler import DatabaseHandler


BASE_URL = os.environ.get("BASE_URL","http://localhost:5000/s/") 


app = Flask(__name__)
CORS(app)
db = DatabaseHandler(db_path="data.db")

@app.route('/api/v1/urls', methods=['POST'])
def create_url():
    data = request.get_json ()
    print (f"create url, with data {data}")
    if "url" not in data:
        return {"error":"url is required"}, 400

    url = data['url']
    url_id = generate_url_id()
    shortened_url = BASE_URL + url_id
    db.add_record (url_id=url_id, full_url=url, user="")
    return {"shortened_url": shortened_url,"url": url}, 201


@app.route('/s/<url_id>')
def redirect_to_full_url(url_id):
    record = db.get_record_by_url_id(url_id)
    if record:
        print (f"Redirecting to {record['full_url']}")
        return redirect (record["full_url"])
    else:
        return {"error":"url not found"}, 404


def generate_url_id():
    chars = random.choices(string.ascii_lowercase+"0123456789",k=6)
    return ''.join(chars)

if __name__ == '__main__':
    app.run(debug=True)
