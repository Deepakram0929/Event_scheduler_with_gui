from flask import Flask, request, jsonify, render_template, redirect, url_for
import uuid
import json
import os

app = Flask(__name__)

DATA_FILE = 'events.json'

def load_events():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return []

def save_events(events):
    with open(DATA_FILE, 'w') as file:
        json.dump(events, file, indent=4)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/events')
def list_events():
    events = load_events()
    events = sorted(events, key=lambda x: x['start_time'])
    return render_template('events.html', events=events)

@app.route('/create', methods=['GET', 'POST'])
def create_event():
    if request.method == 'POST':
        event = {
            "id": str(uuid.uuid4()),
            "title": request.form['title'],
            "description": request.form['description'],
            "start_time": request.form['start_time'],
            "end_time": request.form['end_time']
        }
        events = load_events()
        events.append(event)
        save_events(events)
        return redirect(url_for('list_events'))
    return render_template('create_event.html')

@app.route('/update/<event_id>', methods=['GET', 'POST'])
def update_event(event_id):
    events = load_events()
    event = next((e for e in events if e['id'] == event_id), None)
    if not event:
        return "Event not found", 404
    if request.method == 'POST':
        event['title'] = request.form['title']
        event['description'] = request.form['description']
        event['start_time'] = request.form['start_time']
        event['end_time'] = request.form['end_time']
        save_events(events)
        return redirect(url_for('list_events'))
    return render_template('update_event.html', event=event)

@app.route('/delete/<event_id>')
def delete_event(event_id):
    events = load_events()
    events = [e for e in events if e['id'] != event_id]
    save_events(events)
    return redirect(url_for('list_events'))

if __name__ == '__main__':
    app.run(debug=True)
