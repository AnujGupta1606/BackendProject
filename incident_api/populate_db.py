from app import app, db, Incident

sample_data = [
    {"title": "AI Misclassification", "description": "An AI system misclassified an image leading to incorrect decisions.", "severity": "Medium"},
    {"title": "Data Privacy Breach", "description": "Sensitive user data was leaked by an AI application.", "severity": "High"},
    {"title": "Bias in Recruitment AI", "description": "AI recruitment tool showed gender bias during screening.", "severity": "Low"}
]

with app.app_context():
    for item in sample_data:
        incident = Incident(**item)
        db.session.add(incident)
    db.session.commit()
    print("Sample data added successfully!")
