def calculate_average(student):
    attendance = student["attendance"]
    studying_hours = student["studying_hours"]
    internal_marks = student["internal_marks"]
    assignment_completion = student["assignment_completion"]

    average = (
        attendance
        + studying_hours
        + internal_marks
        + assignment_completion
    ) / 4

    return round(average, 2)