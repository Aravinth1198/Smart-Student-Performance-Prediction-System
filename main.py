from student import get_student_data
from average import calculate_average
from performance import calculate_performance
from display import display_result


students = get_student_data()

for student in students:
    average = calculate_average(student)
    performance = calculate_performance(average)

    display_result(
        student["name"],
        average,
        performance
    )