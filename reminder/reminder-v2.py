import time
import threading
from datetime import datetime, timedelta


def display_menu():
    print("\n==== Reminder App ====")
    print("1. Add Reminder")
    print("2. View Reminders")
    print("3. Delete Reminder")
    print("4. Exit")


class Reminder:
    def __init__(self, message, remind_time, reminder_type):
        self.message = message
        self.remind_time = remind_time
        self.reminder_type = reminder_type
        self.expired = False  # Track whether the reminder has expired

    def __repr__(self):
        status = " (Expired)" if self.expired else ""
        return f"[{self.reminder_type}] Reminder: '{self.message}' at {self.remind_time.strftime('%Y-%m-%d %H:%M:%S')}{status}"


reminders = []


def safe_input(prompt, fallback=""):
    """Simulate input in non-interactive environments with fallback."""
    user_input = input(prompt)
    return user_input if user_input.strip() else fallback


def add_reminder(previous_step):
    try:
        print("Select reminder type:")
        print("1. Birthday\n2. Special Events\n3. Chores\n4. Class")
        type_choice = safe_input("Enter choice (1-4): ", fallback="1")
        reminder_types = {"1": "Birthday", "2": "Special Events", "3": "Chores", "4": "Class"}
        reminder_type = reminder_types.get(type_choice, "General")

        message = safe_input("Enter reminder message: ", fallback="Default Reminder")
        date_input = safe_input("Enter date and time (YYYY-MM-DD HH:MM:SS): ",
                                fallback=(datetime.now() + timedelta(minutes=1)).strftime("%Y-%m-%d %H:%M:%S"))

        remind_time = datetime.strptime(date_input, "%Y-%m-%d %H:%M:%S")
        if remind_time < datetime.now():
            print("You cannot set a reminder in the past. Try again.")
            return

        reminder = Reminder(message, remind_time, reminder_type)
        reminders.append(reminder)
        print("Reminder added successfully!")
        threading.Thread(target=reminder_alert, args=(reminder,), daemon=True).start()
    except ValueError:
        print("Invalid date/time format. Use YYYY-MM-DD HH:MM:SS")


def view_reminders(previous_step):
    if not reminders:
        print("No reminders set.")
    else:
        print("\nYour Reminders:")
        for i, reminder in enumerate(reminders):
            print(f"{i + 1}. {reminder}")


def delete_reminder(previous_step):
    if not reminders:
        print("No reminders to delete.")
        return

    print("\nYour Reminders:")
    for i, reminder in enumerate(reminders):
        print(f"{i + 1}. {reminder}")

    try:
        index = int(input("Enter the number of the reminder to delete: ")) - 1
        if 0 <= index < len(reminders):
            removed = reminders.pop(index)
            print(f"Deleted reminder: {removed}")
        else:
            print("Invalid choice. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")


def reminder_alert(reminder):
    wait_time = max((reminder.remind_time - datetime.now()).total_seconds(), 0)
    time.sleep(wait_time)
    print("\n=======================")
    print(
        f"REMINDER ALERT: [{reminder.reminder_type}] {reminder.message} at {reminder.remind_time.strftime('%Y-%m-%d %H:%M:%S')}!")
    print("=======================\n")
    # Mark the reminder as expired
    reminder.expired = True
    print(f"Reminder '{reminder.message}' is now marked as expired.")


def main():
    def menu():
        while True:
            display_menu()
            choice = input("Choose an option: ")
            if choice == "1":
                add_reminder(menu)
            elif choice == "2":
                view_reminders(menu)
            elif choice == "3":
                delete_reminder(menu)
            elif choice == "4":
                print("Exiting the Reminder App. Have a great day!")
                break
            else:
                print("Invalid choice. Please try again.")

    menu()


if __name__ == "__main__":
    print("Welcome to the Simple Reminder App!")
    main()
