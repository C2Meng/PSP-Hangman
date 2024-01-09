
import shutil

def create_user_profile():
    username = input("Enter your username: ")
    while True:
        age = input("Enter your age: ")
        if age.isdigit():
            break
        else:
            print("Invalid input. Please enter a valid integer for age.")
    gender = input("Enter your gender: ")
    while True:
        student = input("Are you a student of MMU? Enter yes or no: ")
        if student in ["yes", "no"]:
            break
        else:
            print("Invalid input. Please enter a valid command, yes or no.")
    student = student.lower()

    if student == "yes":
        while True:
            student_id = input("Enter your Student ID: ")
            if student_id.isdigit() and len(student_id) == 10:
                break
            else:
                print("Invalid input. Please enter a valid Student ID.")
        faculty = input("Enter your faculty: ")
    else:
        student_id = None
        faculty = None


    user_profile = {
        "username": username,
        "age": age,
        "gender": gender,
        "MMU student": student,
        "Student ID": student_id,
        "faculty": faculty
    }

    return user_profile


def display_user_profile(user_profile):
    console_width = shutil.get_terminal_size().columns
    print(f"\n [User Profile]".center(console_width))
    print(f"Username: {user_profile["username"]}".ljust(console_width))
    print(f"Age: {user_profile["age"]}".ljust(console_width))
    print(f"Gender: {user_profile["gender"]}".ljust(console_width))
    print(f"MMU student: {user_profile["MMU student"]}".ljust(console_width))
    print(f"Student ID: {user_profile["Student ID"]}".ljust(console_width))
    print(f"Faculty: {user_profile["faculty"]}".ljust(console_width))

def main():
    # Create a user profile using user input
    user_profile = create_user_profile()

    # Display the user profile information [f(x) = y]
    display_user_profile(user_profile)

main()
