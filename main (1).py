def sort_students(student_list):
    """
    Sorts a list of student objects based on their CGPA in descending order.
    
    Args:
        student_list (list): List of student objects, where each object has attributes: name (string),
                            roll_number (string), and cgpa (float).
    
    Returns:
        list: Sorted list of student objects.
    """
    sorted_students = sorted(student_list, key=lambda x: x['cgpa'], reverse=True)
    return sorted_students

# Example usage:
students = [
    {'name': 'Alice', 'roll_number': 'A123', 'cgpa': 3.8},
    {'name': 'Bob', 'roll_number': 'B456', 'cgpa': 3.5},
    {'name': 'Charlie', 'roll_number': 'C789', 'cgpa': 4.0}
]

sorted_students = sort_students(students)
for student in sorted_students:
    print(f"Name: {student['name']}, Roll Number: {student['roll_number']}, CGPA: {student['cgpa']}")
