# Reminder App

A simple reminder application that allows users to set, view, and delete reminders. The app supports different types of reminders such as birthdays, special events, chores, and classes. Once the reminder time is reached, an alert is triggered, and the reminder is marked as expired.

## Features

- **Add Reminder**: Set reminders with a specific message and time.
- **View Reminders**: View all the set reminders with their types and times.
- **Delete Reminder**: Remove reminders that are no longer needed.
- **Reminder Alert**: The app triggers an alert when a reminder's time is reached and marks it as expired.

### Version Differences

- **Version 1**: After the reminder alert, the reminder is deleted.
- **Version 2**: After the reminder alert, the reminder is marked as expired.


## Technologies Used

- Python 3.x
- `datetime` for managing reminder times.
- `threading` for handling reminder alerts asynchronously.

## How to Run the Project

1. Clone the repository to your local machine:

   git clone https://github.com/erfnkrm/reminder-App.git


2. Navigate to the project directory:
    cd reminder-App/reminder

3. Run the Python script:

    python reminder-v2.py

