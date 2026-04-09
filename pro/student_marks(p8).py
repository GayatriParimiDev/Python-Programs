# Program to calculate the pass percentage of a class based on student marks.
# A student passes if marks are at least 40 out of 100.


marks_input = input("Enter the marks of all student (out of 100), separated by spaces: ")


marks = [int(m) for m in marks_input.split()]


passing_marks = 40


passed_students = sum(1 for m in marks if m >= passing_marks)


if len(marks) > 0:
    pass_percentage = (passed_students / len(marks)) * 100
    print(f"Pass percentage: {pass_percentage:.2f}%")
else:
    print("No marks entered. Cannot calculate pass percentage.")
