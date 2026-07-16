import json
import os

FILE_PATH = "data/reminders.json"

def load_reminders():
    if not os.path.exists(FILE_PATH):
        return []

    with open(FILE_PATH, "r") as file:
        return json.load(file)

def save_reminders(reminders):
    with open(FILE_PATH, "w") as file:
        json.dump(reminders, file, indent=4)

def add_reminder(title, time, message):
    reminders = load_reminders()

    reminder = {
        "title": title,
        "time": time,
        "message": message,
        "status": "Pending"
    }

    reminders.append(reminder)

    save_reminders(reminders)

def delete_reminder(index):
    reminders = load_reminders()

    if 0 <= index < len(reminders):
        reminders.pop(index)

    save_reminders(reminders)

def mark_completed(index):
    reminders = load_reminders()

    if 0 <= index < len(reminders):
        reminders[index]["status"] = "Completed"

    save_reminders(reminders)