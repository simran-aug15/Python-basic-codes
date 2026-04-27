#write a program to find out whether a student has passed or failed if it required a total of 40% and least is 33% to pass.assume 3 subjects
def get_marks(subject_name):

    while True:

        try:

            marks = int(input(f"Enter marks for {subject_name} (0-100): "))

            if 0 <= marks <= 100:

                return marks

            else:

                print("Marks must be between 0 and 100. Try again.")

        except ValueError:

            print("Invalid input. Please enter a number.")

subjects = ["Math", "Science", "English"]

marks = [get_marks(sub) for sub in subjects]

total_percentage = 100 * sum(marks) / 300

failed_subjects = [subjects[i] for i in range(3) if marks[i] < 33]

print(f"\nTotal Percentage: {total_percentage:.2f}%")

if total_percentage >= 40 and not failed_subjects:

    print("Result: PASS ")

else:

    print("Result: FAIL ")

    if total_percentage < 40:

        print(f"  - Overall percentage {total_percentage:.2f}% is below 40%")

    for sub in failed_subjects:

        print(f"  - Scored below 33% in {sub}")
