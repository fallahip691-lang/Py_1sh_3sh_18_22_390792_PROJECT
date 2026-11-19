



def find(kode_meli=str , student=dict):
    kode_meli=input("kode meli:")
    if kode_meli in student:
        print(student[kode_meli])
    else:
        print("not found")