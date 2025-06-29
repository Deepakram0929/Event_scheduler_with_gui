# Event Scheduler System

## Features
- Create, view, update, and delete events
- Events sorted by start time
- Data persistence using JSON file

## How to Run
```bash
pip install -r requirements.txt
python app.py
```
Server runs at `http://127.0.0.1:5000/`

## API Endpoints
- `POST /events` - Create event
- `GET /events` - List events
- `PUT /events/:id` - Update event
- `DELETE /events/:id` - Delete event

## Run Tests
```bash
pytest
```

## Postman
Import the `postman_collection.json` for API testing.
