





def rank(student: list):
    students = student

    if not all(isinstance(s.get("grade"), (int, float)) for s in students):
        print("Invalid grade")
        return

    students = sorted(
        students,
        key=lambda x: x["grade"],
        reverse=True
    )

    for student_ in students:
        print(student_["name"], student_["grade"])