
def rank(student=dict):
    students = sorted(
            student.values(),key=lambda x: x["grade"],reverse=True)
    for student_ in students:
            print(student_["name"], student_["grade"])