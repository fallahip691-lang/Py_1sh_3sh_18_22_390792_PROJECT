






l_student=[]
student_dict={}
def sign_in(name=str,f_name=str,kode_meli=str,phone_number=str,age=int,city=str,father_name=str,license_=str,grade=int)->dict:
    student_dict[kode_meli] = {
        "name": name,
        "last name":f_name,
        "phone_number": phone_number,
        "age": age,
        "city": city,
        "father_name": father_name,
        "license": license_,
        "grade": grade,
        "count":0}
    l_student.append(student_dict[kode_meli])
    print("successful")

