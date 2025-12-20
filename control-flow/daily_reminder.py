task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

def message():
     print(f"{task} is a {priority} priority task", end = "")

match priority:
    case "high":
        message()
    case "medium":
        message()
    case "low":
        message()
if time_bound == "yes":
    print(" that requires immediate action")
else:
    print(" that you can do at your free time")
