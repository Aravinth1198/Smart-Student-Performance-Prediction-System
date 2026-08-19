import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

data = pd.read_csv("training_data.csv")

x = data[[
    "attendance",
    "study_hours",
    "internal_marks",
    "assignment_completion",
    "previous_score"
]]

y = data["performance"]

scaler = StandardScaler()

x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42
)

x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)