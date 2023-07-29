from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  
vitesse_data = []

@app.route('/api/data', methods=['POST'])
def receive_data():
    data = request.get_json()
    vitesse_data.append(data)  
    return jsonify({'message': 'Données reçues avec succès'})

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify(vitesse_data[len(vitesse_data)-1])  

casque_data = []
@app.route('/api/casque', methods=['POST'])
def receive_casque_data():
    data = request.get_json()
    vitesse_data.append(data)  
    return jsonify({'message': 'Données reçues avec succès'})

@app.route('/api/casque', methods=['GET'])
def get_casque_data():
    return jsonify(casque_data[len(casque_data)-1]) 

if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0")
