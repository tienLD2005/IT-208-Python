import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

DATA_FILE = "data.csv"


def evaluate_grade(avg_score):
    """Determine grade level based on average score."""
    if avg_score >= 8:
        return "Excellent"
    elif avg_score >= 6.5:
        return "Good"
    elif avg_score >= 5:
        return "Average"
    else:
        return "Weak"


def load_data():
    """Load student data from CSV."""
    if os.path.exists(DATA_FILE):
        return pd.read_csv(DATA_FILE).to_dict(orient="records")
    return []


def save_data(data):
    """Save student list to CSV."""
    df = pd.DataFrame(data)
    df.to_csv(DATA_FILE, index=False)
    print("Data saved to data.csv")


def display_students(data):
    """Display all students in table format."""
    if not data:
        print("No students available.")
        return

    df = pd.DataFrame(data)
    print(df.to_string(index=False))


def add_student(data):
    """Add a new student."""
    student_id = input("Enter student ID: ")

    if any(s["id"] == student_id for s in data):
        print("Student ID already exists.")
        return

    name = input("Enter student name: ")

    try:
        math = float(input("Math score: "))
        physics = float(input("Physics score: "))
        chemistry = float(input("Chemistry score: "))

        if not all(0 <= x <= 10 for x in [math, physics, chemistry]):
            print("Scores must be in range 0-10.")
            return

        avg_score = round((math + physics + chemistry) / 3, 2)
        grade = evaluate_grade(avg_score)

        data.append({
            "id": student_id,
            "name": name,
            "math": math,
            "physics": physics,
            "chemistry": chemistry,
            "avg_score": avg_score,
            "grade": grade
        })

        print("Student added successfully.")
    except ValueError:
        print("Scores must be numeric.")


def update_student(data):
    """Update student scores."""
    student_id = input("Enter student ID to update: ")

    for s in data:
        if s["id"] == student_id:
            try:
                s["math"] = float(input("New Math score: "))
                s["physics"] = float(input("New Physics score: "))
                s["chemistry"] = float(input("New Chemistry score: "))

                s["avg_score"] = round(
                    (s["math"] + s["physics"] + s["chemistry"]) / 3, 2
                )
                s["grade"] = evaluate_grade(s["avg_score"])

                print("Update successful.")
            except ValueError:
                print("Scores must be numeric.")
            return

    print("Student not found.")


def delete_student(data):
    """Delete student by ID."""
    student_id = input("Enter student ID to delete: ")

    for s in data:
        if s["id"] == student_id:
            confirm = input("Are you sure you want to delete? (y/n): ")
            if confirm.lower() == "y":
                data.remove(s)
                print("Student deleted.")
            return

    print("Student not found.")


def search_student(data):
    """Search student by ID or name."""
    keyword = input("Enter student ID or name: ").lower()

    result = [
        s for s in data
        if keyword in s["id"].lower() or keyword in s["name"].lower()
    ]

    if result:
        display_students(result)
    else:
        print("No students found.")


def sort_students(data):
    """Sort students by average score or name."""
    print("1. Sort by average score (descending)")
    print("2. Sort by name (A-Z)")
    choice = input("Choose option: ")

    if choice == "1":
        data.sort(key=lambda s: s["avg_score"], reverse=True)
        print("Sorted by average score.")
    elif choice == "2":
        data.sort(key=lambda s: s["name"])
        print("Sorted by name.")
    else:
        print("Invalid choice.")


def statistics(data):
    """Count students by grade."""
    df = pd.DataFrame(data)
    counts = df["grade"].value_counts()

    print("\nGRADE STATISTICS:")
    print(counts)

    return counts


def draw_chart(data):
    """Draw bar or pie chart for grade statistics."""
    counts = statistics(data)

    print("\n1. Bar chart")
    print("2. Pie chart")
    choice = input("Choose chart type: ")

    plt.figure()
    if choice == "1":
        counts.plot(kind="bar")
        plt.title("Grade Statistics")
        plt.xlabel("Grade")
        plt.ylabel("Count")

    elif choice == "2":
        counts.plot(kind="pie", autopct="%1.1f%%")
        plt.title("Grade Distribution")

    else:
        print("Invalid choice.")
        return

    plt.tight_layout()
    plt.show(block=False)
    print("Chart opened. Returning to menu...")


def menu():
    """Main program menu."""
    data = load_data()

    while True:
        print("\n====== STUDENT MANAGEMENT MENU ======")
        print("1. Display all students")
        print("2. Add student")
        print("3. Update student")
        print("4. Delete student")
        print("5. Search")
        print("6. Sort")
        print("7. Statistics")
        print("8. Draw chart")
        print("9. Save data")
        print("10. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            display_students(data)
        elif choice == "2":
            add_student(data)
        elif choice == "3":
            update_student(data)
        elif choice == "4":
            delete_student(data)
        elif choice == "5":
            search_student(data)
        elif choice == "6":
            sort_students(data)
        elif choice == "7":
            statistics(data)
        elif choice == "8":
            draw_chart(data)
        elif choice == "9":
            save_data(data)
        elif choice == "10":
            save_data(data)
            print("Exiting program.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    menu()
