import time
from datetime import datetime
from reminder_manager import load_reminders, mark_completed
from notification import show_notification
import logging

logging.basicConfig(
    filename="logs/notification.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

shown_notifications = set()

while True:

    current_time = datetime.now().strftime("%H:%M")

    reminders = load_reminders()

    for index, reminder in enumerate(reminders):

        reminder_key = reminder["title"] + reminder["time"]

        if (
            reminder["time"] == current_time
            and reminder["status"] == "Pending"
            and reminder_key not in shown_notifications
        ):

            show_notification(
                reminder["title"],
                reminder["message"]
            )

            logging.info(f'Notification Sent: {reminder["title"]}')

            mark_completed(index)

            shown_notifications.add(reminder_key)

    if datetime.now().strftime("%S") == "00":
        shown_notifications.clear()

    time.sleep(1)