task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")
result = f"Reminder: \'{task}\' "
match priority:
    case "high":
        result+= "is a high priority task"
    case "medium":
        result+= "is a medium priority task"
    case "low":
        result+= "is a low priority task"

if time_bound == 'yes':
    result+= " that requires immediate attention today!"
    print(result)
else:
    result += ". Consider completing it when you have free time."
    print(result)