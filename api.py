from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  
global_data = []

@app.route('/api/data', methods=['POST'])
def receive_data():
    data = request.get_json()
    global_data.append(data)  
    return jsonify({'message': 'Données reçues avec succès'})

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify(global_data)  

if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0")
