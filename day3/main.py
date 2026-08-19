import tkinter as tk
from tkinter import messagebox
import csv
import os
from validation import validate_user_input
from model import predict_performance

window = tk.Tk()
window.title("Student Performance Prediction System")
window.geometry("19890x1080")
window.configure(bg="#eef2f7")
#window.resizable(False, False)


class Dashboard:

    def clear_fields(self):
        self.name_entry.delete(0, tk.END)
        self.id_entry.delete(0, tk.END)
        self.attendance_entry.delete(0, tk.END)
        self.study_entry.delete(0, tk.END)
        self.internal_entry.delete(0, tk.END)
        sealf.assignment_entry.delete(0, tk.END)
        self.previous_entry.delete(0, tk.END)

        self.prediction_label.config(text="--")
        self.risk_label.config(text="--")
        self.recommendation_label.config(text="--")

    def predict(self):

        name = self.name_entry.get().strip()
        student_id = self.id_entry.get().strip()
        attendance = self.attendance_entry.get().strip()
        study_hours = self.study_entry.get().strip()
        internal_marks = self.internal_entry.get().strip()
        assignment = self.assignment_entry.get().strip()
        previous_score = self.previous_entry.get().strip()

        errors = validate_user_input(
            name,
            student_id,
            attendance,
            study_hours,
            internal_marks,
            assignment,
            previous_score
        )

        if errors:
            messagebox.showerror("Input Error", "\n".join(errors))
            return

        attendance = float(attendance)
        study_hours = float(study_hours)
        internal_marks = float(internal_marks)
        assignment = float(assignment)
        previous_score = float(previous_score)

        result = predict_performance(
            attendance,
            study_hours,
            internal_marks,
            assignment,
            previous_score
        )

        if result == "Excellent":
            risk = "Low Risk"
            recommendation = "Excellent performance. Keep maintaining the same effort."

        elif result == "Very Good":
            risk = "Low Risk"
            recommendation = "Very good performance. Focus on reaching excellence."

        elif result == "Good":
            risk = "Medium Risk"
            recommendation = "Good performance. Improve weak academic areas."

        else:
            risk = "High Risk"
            recommendation = "Immediate academic improvement is recommended."

        self.prediction_label.config(text=result)
        self.risk_label.config(text=risk)
        self.recommendation_label.config(text=recommendation)

        file_exists = os.path.exists("student_inputs.csv")

        with open("student_inputs.csv", "a", newline="") as file:

            writer = csv.writer(file)

            if not file_exists:
                writer.writerow([
                    "student_id",
                    "student_name",
                    "attendance",
                    "study_hours",
                    "internal_marks",
                    "assignment_completion",
                    "previous_score",
                    "prediction",
                    "risk"
                ])

            writer.writerow([
                student_id,
                name,
                attendance,
                study_hours,
                internal_marks,
                assignment,
                previous_score,
                result,
                risk
            ])

        messagebox.showinfo(
            "Prediction Completed",
            "Student data saved and performance predicted successfully."
        )

    def __init__(self, master):

        self.frame = tk.Frame(
            master,
            bg="#eef2f7",
            width=1050,
            height=700
        )

        self.frame.pack(fill="both", expand=True)

        title = tk.Label(
            self.frame,
            text="STUDENT PERFORMANCE PREDICTION",
            font=("Segoe UI", 25, "bold"),
            bg="#eef2f7",
            fg="#172b4d"
        )

        title.pack(pady=(25, 5))

        subtitle = tk.Label(
            self.frame,
            text="Machine Learning Based Academic Performance Analysis",
            font=("Segoe UI", 12),
            bg="#eef2f7",
            fg="#65748b"
        )

        subtitle.pack(pady=(0, 20))

        input_frame = tk.Frame(
            self.frame,
            bg="white",
            bd=1,
            relief="solid"
        )

        input_frame.place(x=70, y=120, width=450, height=440)

        tk.Label(
            input_frame,
            text="Student Information",
            font=("Segoe UI", 17, "bold"),
            bg="white",
            fg="#172b4d"
        ).grid(row=0, column=0, columnspan=2, pady=20)

        tk.Label(
            input_frame,
            text="Student Name",
            font=("Segoe UI", 11),
            bg="white"
        ).grid(row=1, column=0, padx=20, pady=10, sticky="w")

        self.name_entry = tk.Entry(
            input_frame,
            font=("Segoe UI", 11),
            width=25
        )

        self.name_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(
            input_frame,
            text="Student ID",
            font=("Segoe UI", 11),
            bg="white"
        ).grid(row=2, column=0, padx=20, pady=10, sticky="w")

        self.id_entry = tk.Entry(
            input_frame,
            font=("Segoe UI", 11),
            width=25
        )

        self.id_entry.grid(row=2, column=1, padx=10, pady=10)

        tk.Label(
            input_frame,
            text="Attendance (%)",
            font=("Segoe UI", 11),
            bg="white"
        ).grid(row=3, column=0, padx=20, pady=10, sticky="w")

        self.attendance_entry = tk.Entry(
            input_frame,
            font=("Segoe UI", 11),
            width=25
        )

        self.attendance_entry.grid(row=3, column=1, padx=10, pady=10)

        tk.Label(
            input_frame,
            text="Study Hours / Day",
            font=("Segoe UI", 11),
            bg="white"
        ).grid(row=4, column=0, padx=20, pady=10, sticky="w")

        self.study_entry = tk.Entry(
            input_frame,
            font=("Segoe UI", 11),
            width=25
        )

        self.study_entry.grid(row=4, column=1, padx=10, pady=10)

        tk.Label(
            input_frame,
            text="Internal Marks (%)",
            font=("Segoe UI", 11),
            bg="white"
        ).grid(row=5, column=0, padx=20, pady=10, sticky="w")

        self.internal_entry = tk.Entry(
            input_frame,
            font=("Segoe UI", 11),
            width=25
        )

        self.internal_entry.grid(row=5, column=1, padx=10, pady=10)

        tk.Label(
            input_frame,
            text="Assignment (%)",
            font=("Segoe UI", 11),
            bg="white"
        ).grid(row=6, column=0, padx=20, pady=10, sticky="w")

        self.assignment_entry = tk.Entry(
            input_frame,
            font=("Segoe UI", 11),
            width=25
        )

        self.assignment_entry.grid(row=6, column=1, padx=10, pady=10)

        tk.Label(
            input_frame,
            text="Previous Score (%)",
            font=("Segoe UI", 11),
            bg="white"
        ).grid(row=7, column=0, padx=20, pady=10, sticky="w")

        self.previous_entry = tk.Entry(
            input_frame,
            font=("Segoe UI", 11),
            width=25
        )

        self.previous_entry.grid(row=7, column=1, padx=10, pady=10)

        result_frame = tk.Frame(
            self.frame,
            bg="#172b4d"
        )

        result_frame.place(x=560, y=120, width=420, height=440)

        tk.Label(
            result_frame,
            text="Prediction Result",
            font=("Segoe UI", 19, "bold"),
            bg="#172b4d",
            fg="white"
        ).pack(pady=25)

        tk.Label(
            result_frame,
            text="Performance",
            font=("Segoe UI", 11),
            bg="#172b4d",
            fg="#b8c7dc"
        ).pack()

        self.prediction_label = tk.Label(
            result_frame,
            text="--",
            font=("Segoe UI", 24, "bold"),
            bg="#172b4d",
            fg="#36d399"
        )

        self.prediction_label.pack(pady=5)

        tk.Label(
            result_frame,
            text="Risk Level",
            font=("Segoe UI", 11),
            bg="#172b4d",
            fg="#b8c7dc"
        ).pack(pady=(20, 0))

        self.risk_label = tk.Label(
            result_frame,
            text="--",
            font=("Segoe UI", 17, "bold"),
            bg="#172b4d",
            fg="#ffcc66"
        )

        self.risk_label.pack()

        tk.Label(
            result_frame,
            text="Recommendation",
            font=("Segoe UI", 11),
            bg="#172b4d",
            fg="#b8c7dc"
        ).pack(pady=(25, 5))

        self.recommendation_label = tk.Label(
            result_frame,
            text="--",
            font=("Segoe UI", 10),
            bg="#172b4d",
            fg="white",
            wraplength=340
        )

        self.recommendation_label.pack()

        predict_button = tk.Button(
            self.frame,
            text="PREDICT PERFORMANCE",
            font=("Segoe UI", 12, "bold"),
            bg="#2563eb",
            fg="white",
            activebackground="#1d4ed8",
            activeforeground="white",
            relief="flat",
            width=25,
            height=2,
            command=self.predict
        )

        predict_button.place(x=200, y=590)

        clear_button = tk.Button(
            self.frame,
            text="CLEAR",
            font=("Segoe UI", 12, "bold"),
            bg="#64748b",
            fg="white",
            relief="flat",
            width=15,
            height=2,
            command=self.clear_fields
        )

        clear_button.place(x=500, y=590)

        exit_button = tk.Button(
            self.frame,
            text="EXIT",
            font=("Segoe UI", 12, "bold"),
            bg="#dc2626",
            fg="white",
            relief="flat",
            width=15,
            height=2,
            command=window.destroy
        )

        exit_button.place(x=700, y=590)


Dashboard(window)

window.mainloop()