





from sign_in import *
from quistions import *
from find import *
from rank import *




def exam():
    grade=0
    while True:
        print("online test")
        menu=input("1.sign in 2.quiz 3.show your grades 4.rankings ")
        match menu:
            case "1":
                name=input("name:").strip().upper()
                f_name=input("last name:").strip().upper()
                kode_meli=input("kode meli:")
                if len(kode_meli)<10 or kode_meli==False:
                    print("kode meli irad darad dobare vared kon")
                else:
                    phone_number=input("phone number:")
                    if len(phone_number)<11 or phone_number==False:
                        print("phone number irad darad dobare vared kon")
                    else:
                        age=int(input("age:"))
                        city=input("city:").strip().upper()
                        father_name=input("father name:").strip().upper()
                        license_=input("license:").strip().upper()
                        sign_in(name,f_name,kode_meli,phone_number, age, city, father_name, license_)
            case "2":
                kode_meli=input("kode meli:")
                print("for exit type exit")
                if kode_meli in student_dict:
                    student = student_dict[kode_meli]
                    if student["count"] > 2:
                        print("bish az had mojaz")
                    else:
                        grade, count = quiz(grade=0, student=student)
                        student["grade"] = grade
                        student["count"] = count
                        print(student_dict[kode_meli])
                        print("your grade is ",grade)
                else:
                    print("not found")
            case "3":
                find(kode_meli=kode_meli,student=student_dict)
            case "4":
                rank(student=l_student)





