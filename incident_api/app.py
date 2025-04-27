from flask import Flask, request, jsonify, abort
from flask_cors import CORS
from models import db, Incident
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)
CORS(app)

with app.app_context():
    db.create_all()

VALID_SEVERITIES = ['Low', 'Medium', 'High']

@app.route('/incidents', methods=['GET'])
def get_incidents():
    incidents = Incident.query.all()
    result = [{
        'id': i.id,
        'title': i.title,
        'description': i.description,
        'severity': i.severity,
        'reported_at': i.reported_at.isoformat()
    } for i in incidents]
    return jsonify(result), 200

@app.route('/incidents', methods=['POST'])
def create_incident():
    data = request.get_json()
    if not data or 'title' not in data or 'description' not in data or 'severity' not in data:
        abort(400, description="Missing required fields.")
    if data['severity'] not in VALID_SEVERITIES:
        abort(400, description="Severity must be Low, Medium, or High.")

    incident = Incident(
        title=data['title'],
        description=data['description'],
        severity=data['severity']
    )
    db.session.add(incident)
    db.session.commit()
    return jsonify({
        'id': incident.id,
        'title': incident.title,
        'description': incident.description,
        'severity': incident.severity,
        'reported_at': incident.reported_at.isoformat()
    }), 201

@app.route('/incidents/<int:incident_id>', methods=['GET'])
def get_incident(incident_id):
    incident = Incident.query.get(incident_id)
    if not incident:
        abort(404, description="Incident not found.")
    return jsonify({
        'id': incident.id,
        'title': incident.title,
        'description': incident.description,
        'severity': incident.severity,
        'reported_at': incident.reported_at.isoformat()
    }), 200

@app.route('/incidents/<int:incident_id>', methods=['DELETE'])
def delete_incident(incident_id):
    incident = Incident.query.get(incident_id)
    if not incident:
        abort(404, description="Incident not found.")
    db.session.delete(incident)
    db.session.commit()
    return jsonify({"message": f"Incident {incident_id} deleted successfully."}), 200

if __name__ == '__main__':
    app.run(debug=True)
