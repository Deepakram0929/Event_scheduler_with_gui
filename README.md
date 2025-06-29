# Event Scheduler System

## Features
- Create, view, update, and delete events
- Events sorted by start time
- Data persistence using JSON file
  
## Project Structure
```
event_scheduler_with_gui/
├── templates/          # HTML pages (GUI)
├── static/             # CSS files
├── app.py              # Main Flask App
├── events.json         # Persistent event storage
├── requirements.txt    # Python dependencies
└── README.md           # Instructions
```
## API Endpoints
- `POST /events` - Create event
- `GET /events` - List events
- `PUT /events/:id` - Update event
- `DELETE /events/:id` - Delete event

## Installation Steps

### Step 1 : Clone the Repository
```
https://github.com/Deepakram0929/Event_scheduler_with_gui.git
cd Event_scheduler
```
### Step 2 : Create a Virtual Environment
```
python -m venv venv
```
### Step 3 : Activate the Virtual Environment
```
.\venv\Scripts\activate
```
### Step 4 : Install Dependencies
```
pip install -r requirements.txt
```
### Step 5 : Run the Application
```
python app.py
```
### Step 5 : Open in Browser
```
http://127.0.0.1:5000/
```
## Screenshot
1. Home Page
![image](https://github.com/user-attachments/assets/a8bd81e1-cb62-4363-9115-5c4520dc664e)

2. Create Event
![image](https://github.com/user-attachments/assets/4304334f-21dc-4b43-9c93-916c8e5afd93)

3. View Events
![image](https://github.com/user-attachments/assets/8d63f3b5-51eb-41c3-aa3f-8d51ad3cd2fc)

4. Update Event
![image](https://github.com/user-attachments/assets/ba823eba-aaaf-4d4d-90cf-c6727db7e511)

5. Delete Event
DELETE /events/<event_id>
![image](https://github.com/user-attachments/assets/44218a90-57e0-4078-903a-b51ec57c3487)





