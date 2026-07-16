import streamlit as st
from reminder_manager import add_reminder, load_reminders, delete_reminder

st.set_page_config(
    page_title="Scheduled Notification System",
    page_icon="🔔",
    layout="wide"
)

st.title("🔔 Python Scheduled Notification System")

st.markdown("---")

reminders = load_reminders()

col1, col2 = st.columns(2)

with col1:
    st.metric("Total Reminders", len(reminders))

with col2:
    st.metric("Application Status", "Running")

st.markdown("---")

st.header("➕ Add Reminder")

title = st.text_input("Reminder Title")

time = st.time_input("Reminder Time")

message = st.text_area("Reminder Message")

if st.button("Add Reminder"):

    reminder_time = time.strftime("%H:%M")

    if title and message:

        add_reminder(
            title,
            reminder_time,
            message
        )

        st.success("Reminder Added Successfully!")

        st.rerun()

    else:

        st.error("Please fill all fields.")

st.markdown("---")

st.header("📋 Saved Reminders")

reminders = load_reminders()

if reminders:

    for i, reminder in enumerate(reminders):

        st.subheader(reminder["title"])

        st.write("⏰ Time :", reminder["time"])

        st.write("📝 Message :", reminder["message"])

        st.write("📌 Status :", reminder["status"])

        if st.button("Delete", key=i):

            delete_reminder(i)

            st.rerun()

        st.markdown("---")

else:

    st.info("No reminders available.")

st.header("📜 Notification Logs")

try:

    with open("logs/notification.log", "r") as file:

        logs = file.read()

        st.text_area(
            "Logs",
            logs,
            height=250
        )

except:

    st.info("No logs available.")