import pandas as pd
import joblib
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

data = pd.read_csv("training_data.csv")

x = data[[
    "attendance",
    "study_hours",
    "internal_marks",
    "assignment_completion",
    "previous_score"
]]

y = data["performance"]

x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

model = Pipeline([
    ("scaler", StandardScaler()),
    ("classifier", SVC(
        kernel="rbf",
        C=10,
        gamma="scale"
    ))
])

model.fit(x_train, y_train)

accuracy = model.score(x_test, y_test)

print("SVM Accuracy:", accuracy)

joblib.dump(model, "student_performance_model.pkl")

def predict_performance(attendance, study_hours, internal_marks, assignment, previous_score):

    model = joblib.load("student_performance_model.pkl")

    data = [[
        attendance,
        study_hours,
        internal_marks,
        assignment,
        previous_score
    ]]

    result = model.predict(data)

    return result[0]