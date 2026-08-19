def validate_user_input(name, student_id, attendance, study_hours, internal_marks, assignment, previous_score):

    errors = []

    if not name:
        errors.append("Student Name is required")
    elif not name.replace(" ", "").isalpha():
        errors.append("Student Name should contain only letters")

    if not student_id:
        errors.append("Student ID is required")
    elif not student_id.isdigit():
        errors.append("Student ID should be a number")

    try:
        attendance = float(attendance)
        if attendance < 0 or attendance > 100:
            errors.append("Attendance should be between 0 and 100")
    except ValueError:
        errors.append("Attendance should be a valid number")

    try:
        study_hours = float(study_hours)
        if study_hours < 0 or study_hours > 24:
            errors.append("Study hours should be between 0 and 24")
    except ValueError:
        errors.append("Study hours should be a valid number")

    try:
        internal_marks = float(internal_marks)
        if internal_marks < 0 or internal_marks > 100:
            errors.append("Internal marks should be between 0 and 100")
    except ValueError:
        errors.append("Internal marks should be a valid number")

    try:
        assignment = float(assignment)
        if assignment < 0 or assignment > 100:
            errors.append("Assignment completion should be between 0 and 100")
    except ValueError:
        errors.append("Assignment completion should be a valid number")

    try:
        previous_score = float(previous_score)
        if previous_score < 0 or previous_score > 100:
            errors.append("Previous academic score should be between 0 and 100")
    except ValueError:
        errors.append("Previous academic score should be a valid number")

    return errors