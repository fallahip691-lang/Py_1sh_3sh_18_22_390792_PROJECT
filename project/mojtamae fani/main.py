



from add import *
from delete import *
from find import *
from edit import *







classes=[]
class_mojtama={}
class_code = ["101", "102", "103", "104", "105", "106", "107", "108", "109", "110", "111", "112", "113", "114", "115"]
days = ["shanbe", "yekshanbe", "doshanbe", "seshanbe", "chaharshanbe", "panhshanbe", "jome"]
hours = ["7:00", "7:30", "8:00", "8:30", "9:00", "9:30", "10:00", "10:30", "11:00", "11:30", "12:00", "12:30", "13:00", "13:30", "14:00", "14:30", "15:00", "15:30", "16:00", "16:30", "17:00", "17:30", "18:00", "18:30", "19:00", "19:30", "20:00", "20:30", "21:00", "21:30", "22:00"]
topics = ["web1", "web2", "web3", "seo", "python", "data"]
teacher_list = ["Ekhtiary", "Mostafavy", "Mohamady", "Esmaily"]
admin = {"user": "admin", "password": "admin12345"}
code = ["101","102","103","104","105","106","107","108","109","110"]
class_mojtama = {
    "101": {
        "shomare class": "101",
        "rooz": "shanbe",
        "saat shoro": "7:00",
        "saat payan": "10:00",
        "ostad": "Ekhtiary",
        "dars": "python"
    },
    "102": {
        "shomare class": "102",
        "rooz": "shanbe",
        "saat shoro": "10:00",
        "saat payan": "13:00",
        "ostad": "Mostafavy",
        "dars": "web1"
    },
    "103": {
        "shomare class": "103",
        "rooz": "yekshanbe",
        "saat shoro": "8:00",
        "saat payan": "11:30",
        "ostad": "Mohamady",
        "dars": "data"
    },
    "104": {
        "shomare class": "104",
        "rooz": "yekshanbe",
        "saat shoro": "13:00",
        "saat payan": "16:00",
        "ostad": "Esmaily",
        "dars": "seo"
    },
    "105": {
        "shomare class": "105",
        "rooz": "doshanbe",
        "saat shoro": "7:30",
        "saat payan": "11:00",
        "ostad": "Ekhtiary",
        "dars": "web2"
    },
    "106": {
        "shomare class": "106",
        "rooz": "doshanbe",
        "saat shoro": "14:00",
        "saat payan": "17:00",
        "ostad": "Mostafavy",
        "dars": "python"
    },
    "107": {
        "shomare class": "107",
        "rooz": "seshanbe",
        "saat shoro": "9:00",
        "saat payan": "12:30",
        "ostad": "Mohamady",
        "dars": "web3"
    },
    "108": {
        "shomare class": "108",
        "rooz": "chaharshanbe",
        "saat shoro": "14:00",
        "saat payan": "17:00",
        "ostad": "Esmaily",
        "dars": "data"
    },
    "109": {
        "shomare class": "109",
        "rooz": "panhshanbe",
        "saat shoro": "8:00",
        "saat payan": "11:30",
        "ostad": "Ekhtiary",
        "dars": "seo"
    },
    "110": {
        "shomare class": "110",
        "rooz": "jome",
        "saat shoro": "17:00",
        "saat payan": "20:30",
        "ostad": "Mostafavy",
        "dars": "web1"
    }
}

classes = list(class_mojtama.values())

users = {}

def mojtama():
    menu=input(" 1.login as admin 2.login as user 3.sign in")
    match menu:
        case"1":
            while True:
                user=input("user:")
                password=input("password:")
                if user == admin["user"]:
                        if password == admin["password"]:
                            print("welcome admin:", user)
                            while True:
                                menu=input("1.add 2.delete 3.find 4.edit 5.show 6.exit")
                                match menu:
                                    case "1":
                                            print(class_code)
                                            print(days)
                                            print(hours)
                                            print(topics)
                                            print(teacher_list)
                                            entekhab( class_code,days,hours,topics,teacher_list,classes,code,class_mojtama)
                                    case "2":
                                        shomare_class = input("shomare class: ")
                                        delete(shomare_class,class_mojtama,classes,code)
                                    case "3":
                                        shomare_class = input("shomare class: ")
                                        find(shomare_class,class_mojtama,classes)
                                    case "4":
                                        shomare_class = input("shomare class: ")
                                        edit(shomare_class,class_code,days,hours,topics,teacher_list,class_mojtama)
                                    case "5":
                                        print(classes)
                                    case "6":
                                        break
                        else:
                            print("password incorrect")
                            break

        case"2":
            while True:
                user=input("user:")
                password=input("password:")
                if user in users:
                    if password == users[user]["password"]:
                        print("welcome", user)
                        while True:
                            menu=input("1show 2.exit")
                            match menu:
                                case "1":
                                    print(classes)
                                case "2":
                                    break
                        break
                    else:
                        print("password incorrect")
                        break
                else:
                    print("not found")
                    break
        case "3":
            user = input("username: ")
            password = input("password: ")

            if user not in users:
                users[user] = {
                    "username": user,
                    "password": password
                }
                print("sign up successful")
            else:
                print("username tekrary")

