task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

def message(custom_msg):
    print(f"{custom_msg}: {task} is a {priority} priority task", end = "")

match priority:
    case "high":
        message("Reminder")
    case "medium":
        message("Alert")
    case "low":
        message("Note")
if time_bound == "yes":
    print(" that requires immediate action")
else:
    print(" that you can do at your free time")
