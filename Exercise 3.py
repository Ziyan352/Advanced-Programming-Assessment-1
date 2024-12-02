import tkinter as tk
from tkinter import messagebox
import os

def load_data():
    if not os.path.exists("studentMarks.txt"):
        messagebox.showerror("Error", "studentMarks.txt file not found.")
        return []
    
    students = []
    with open("studentMarks.txt", "r") as file:
        total_students = int(file.readline().strip())
        for line in file:
            data = line.strip().split(',')
            student_code = int(data[0])
            student_name = data[1].strip()
            course_marks = list(map(int, data[2:5]))
            exam_mark = int(data[5])
            coursework_total = sum(course_marks)
            overall_score = coursework_total + exam_mark
            percentage = (overall_score / 160) * 100
            grade = calculate_grade(percentage)
            students.append({
                "code": student_code,
                "name": student_name,
                "coursework_total": coursework_total,
                "exam_mark": exam_mark,
                "overall_score": overall_score,
                "percentage": percentage,
                "grade": grade
            })
    return students

def calculate_grade(percentage):
    if percentage >= 70:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 50:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "F"

def view_all_records():
    result = ""
    total_percentage = 0
    for student in students:
        total_percentage += student["percentage"]
        result += f"{student['name']} (ID: {student['code']}): Total Coursework: {student['coursework_total']}, Exam: {student['exam_mark']}, Percentage: {student['percentage']:.2f}%, Grade: {student['grade']}\n"
    
    average_percentage = total_percentage / len(students)
    result += f"\nTotal Students: {len(students)}, Average Percentage: {average_percentage:.2f}%"
    result_text.set(result)

def view_individual_record():
    student_name = student_name_entry.get().strip()
    for student in students:
        if student['name'].lower() == student_name.lower():
            result = f"{student['name']} (ID: {student['code']}): Total Coursework: {student['coursework_total']}, Exam: {student['exam_mark']}, Percentage: {student['percentage']:.2f}%, Grade: {student['grade']}"
            result_text.set(result)
            return
    messagebox.showinfo("Not Found", "Student not found.")

def show_highest_score():
    top_student = max(students, key=lambda x: x['overall_score'])
    result = f"{top_student['name']} (ID: {top_student['code']}): Total Coursework: {top_student['coursework_total']}, Exam: {top_student['exam_mark']}, Percentage: {top_student['percentage']:.2f}%, Grade: {top_student['grade']}"
    result_text.set(result)

def show_lowest_score():
    low_student = min(students, key=lambda x: x['overall_score'])
    result = f"{low_student['name']} (ID: {low_student['code']}): Total Coursework: {low_student['coursework_total']}, Exam: {low_student['exam_mark']}, Percentage: {low_student['percentage']:.2f}%, Grade: {low_student['grade']}"
    result_text.set(result)

root = tk.Tk()
root.title("Student Records Management")
root.geometry("600x400")

students = load_data()

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Student Name:").grid(row=0, column=0)
student_name_entry = tk.Entry(frame)
student_name_entry.grid(row=0, column=1)

result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, wraplength=500, justify="left")
result_label.pack(pady=10)

tk.Button(frame, text="View All Records", command=view_all_records).grid(row=1, column=0, padx=5, pady=5)
tk.Button(frame, text="View Individual Record", command=view_individual_record).grid(row=1, column=1, padx=5, pady=5)
tk.Button(frame, text="Show Highest Score", command=show_highest_score).grid(row=1, column=2, padx=5, pady=5)
tk.Button(frame, text="Show Lowest Score", command=show_lowest_score).grid(row=1, column=3, padx=5, pady=5)

root.mainloop()
