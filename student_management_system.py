import tkinter as tk

from tkinter import messagebox

students = []

def add_student():
    name = name_entry.get()
    roll = roll_entry.get()
    course = course_entry.get()
    if name and roll and course:
        for student in students:
            if student.startswith(roll):
                messagebox.showerror("Duplicate Roll Number","This roll number already exists!")
                return
        record = f"{roll} - {name} - {course}"

        students.append(record)
        listbox.insert(tk.END, record)

        name_entry.delete(0, tk.END)
        roll_entry.delete(0, tk.END)
        course_entry.delete(0, tk.END)
        messagebox.showinfo("Success", "Student Added!")
    else:
        messagebox.showerror("Missing Information","Please fill all fields!")

def delete_student():
    selected = listbox.curselection()
    if selected:
        confirm = messagebox.askyesno("Confirm Delete","Are you sure you want to delete this student?")

        if confirm:
            index = selected[0]

            listbox.delete(index)
            students.pop(index)
            messagebox.showinfo("Success", "Student Deleted!")
    else:
        messagebox.showerror("No Selection", "Please select a student first!")

def search_student():
    roll = roll_entry.get()

    for student in students:
        if student.startswith(roll):
            messagebox.showinfo("Student Found",student)
            return
    messagebox.showerror("Not Found","Student Not Found!")

def update_student():
    selected = listbox.curselection()

    if selected:
        index = selected[0]

        roll = roll_entry.get()
        name = name_entry.get()
        course = course_entry.get()
        if roll and name and course: 
            new_record = f"{roll} - {name} - {course}"

            students[index] = new_record

            listbox.delete(index)
            listbox.insert(index, new_record)

            messagebox.showinfo("Success", "Student Updated!")
        else:
            messagebox.showerror("Missing Information", "Please fill all fields!")
   
    else:
            messagebox.showerror("No Selection", "Please select a student first!")

def count_students():
    total = len(students)
    messagebox.showinfo("Total Students", f"Total Students: {total}")

def save_students():
    with open("students.txt", "w") as file:
        for student in students:
            file.write(student + "\n")

    messagebox.showinfo("Saved", "Students saved successfully!")

def load_students():
    try:
        with open("students.txt", "r") as file:
            for student in file:
                student = student.strip()

                students.append(student)
                listbox.insert(tk.END, student)

    except FileNotFoundError:
        pass

def clear_students():
    confirm = messagebox.askyesno("Confirm Clear","Are you sure you want to clear all students?")
    
    if confirm:
        students.clear()
    
        listbox.delete(0, tk.END)
       
        name_entry.delete(0, tk.END)
        roll_entry.delete(0, tk.END)
        course_entry.delete(0, tk.END)
    
        messagebox.showinfo("Success", "All Students Cleared!")
    
root = tk.Tk()
root.title("Student Management System")
root.geometry("400x350")
root.attributes('-topmost', True)

tk.Label(root, text="Roll Number").pack()
roll_entry = tk.Entry(root)
roll_entry.pack()

tk.Label(root, text="Student Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Course").pack()
course_entry = tk.Entry(root)
course_entry.pack()



tk.Button(root, text="Add Student", command=add_student).pack(pady=5)

tk.Button(root, text="Delete Student", command=delete_student).pack(pady=5)

tk.Button(root, text="Search Student", command=search_student).pack(pady=5)

tk.Button(root, text="Update Student", command=update_student).pack(pady=5)

tk.Button(root, text="Count Students", command=count_students).pack(pady=5)

tk.Button(root, text="Save Students", command=save_students).pack(pady=5)

tk.Button(root, text="Clear All Students", command=clear_students).pack(pady=5)

listbox = tk.Listbox(root)
listbox.pack(fill=tk.BOTH, expand=True)

load_students()

root.mainloop()