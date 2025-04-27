# HumanChain AI Safety Incident Log API

## 📦 Tech Stack
- Python 3.x
- Flask
- SQLAlchemy
- SQLite
- flask-cors

## 📑 Setup Instructions

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the app:
   ```
   python app.py
   ```

3. (Optional) Populate sample data:
   ```
   python populate_db.py
   ```

## 📌 API Endpoints

### GET /incidents
```
curl -X GET http://localhost:5000/incidents
```

### POST /incidents
```
curl -X POST http://localhost:5000/incidents -H "Content-Type: application/json" -d '{"title": "Test", "description": "Test desc", "severity": "Low"}'
```

### GET /incidents/{id}
```
curl -X GET http://localhost:5000/incidents/1
```

### DELETE /incidents/{id}
```
curl -X DELETE http://localhost:5000/incidents/1
```

## 📓 Notes
- Severity must be one of Low, Medium, High.
- Errors return appropriate HTTP status codes.
- Database file is database.db (auto-created).
