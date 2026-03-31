from datetime import datetime, timedelta

subjects = []

def add_subject():
    name = input("Subject name: ")
    deadline_input = input("Deadline (YYYY-MM-DD): ")
    difficulty = int(input("Difficulty (1-5): "))
    hours = int(input("Total study hours: "))

    deadline = datetime.strptime(deadline_input, "%Y-%m-%d")

    subjects.append({
        "name": name,
        "deadline": deadline,
        "difficulty": difficulty,
        "hours": hours
    })

def get_priority(subject):
    days_left = (subject["deadline"] - datetime.now()).days
    if days_left <= 0:
        days_left = 1
    return (subject["difficulty"] * 2) + (10 / days_left)

def create_plan():
    for subject in subjects:
        subject["priority"] = get_priority(subject)

    ordered = sorted(subjects, key=lambda x: x["priority"], reverse=True)

    plan = {}
    current_day = datetime.now()

    for subject in ordered:
        remaining = subject["hours"]

        while remaining > 0:
            day_key = current_day.strftime("%Y-%m-%d")

            if day_key not in plan:
                plan[day_key] = []

            hours_today = min(2, remaining)
            plan[day_key].append((subject["name"], hours_today))

            remaining -= hours_today
            current_day += timedelta(days=1)

    return plan

def display_plan(plan):
    print("\nYour Study Plan:\n")

    for day, tasks in plan.items():
        print(day)
        for subject, hours in tasks:
            print(f"  {subject}: {hours} hour(s)")
        print()

def show_tips():
    print("Tips:")
    print("- Give more time to difficult subjects")
    print("- Start early for upcoming deadlines")
    print("- Stay consistent every day")

def main():
    while True:
        print("\n1. Add subject")
        print("2. Generate plan")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_subject()
        elif choice == "2":
            if not subjects:
                print("No subjects added yet.")
            else:
                plan = create_plan()
                display_plan(plan)
                show_tips()
        elif choice == "3":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
