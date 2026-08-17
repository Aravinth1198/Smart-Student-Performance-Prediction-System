def calculate_performance(average):
    if average >= 85:
        return "Excellent"
    elif average >= 70:
        return "Very Good"
    elif average >= 50:
        return "Good"
    else:
        return "High Risk"