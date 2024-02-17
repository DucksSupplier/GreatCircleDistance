from flask import Flask, render_template, jsonify, request
from geopy.distance import great_circle
from flask_cors import CORS

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate_path', methods=['POST'])
def calculate_path():
    coords_1 = (request.json['lat1'], request.json['lon1'])
    coords_2 = (request.json['lat2'], request.json['lon2'])
    distance = great_circle(coords_1, coords_2).kilometers
    # Here, you could also calculate the intermediate points for the great-circle path
    return jsonify({'distance': distance})

if __name__ == '__main__':
    app.run(debug=True)

CORS(app)