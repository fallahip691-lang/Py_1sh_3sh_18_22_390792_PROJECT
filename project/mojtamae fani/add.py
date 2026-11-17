







def entekhab(class_code=list,days=list,hours=list,topics=list,teacher_list=list,classes=list,code=list,class_mojtama=dict)->dict:

    while True:
        while True:
            shomare_class = input("shomare class: ")
            if shomare_class in class_code:
                if shomare_class not in code:
                    while True:
                        weak_day = input("rooz: ")
                        if weak_day in days:
                            while True:
                                saat_1 = input("saate shoro: ")
                                if saat_1 in hours:
                                    while True:
                                        saat_2 = input("saate payan: ")
                                        if saat_2 in hours:
                                            if   saat_1!=saat_2:
                                                teachers = input("ostad: ").title()
                                                if teachers in teacher_list:
                                                    while True:
                                                        topic = input("dars: ")
                                                        if topic in topics:
                                                            
                                                        
                                                            code.append(shomare_class)
                                                            class_mojtama[shomare_class] = {
                                                                "shomare class": shomare_class,
                                                                "rooz": weak_day,
                                                                "saat shoro": saat_1,
                                                                "saat payan": saat_2,
                                                                "ostad": teachers,
                                                                "dars": topic
                                                            }
                                                        
                                                            classes.append(class_mojtama[shomare_class])
                                                            print(class_mojtama[shomare_class])
                                                            return class_mojtama
                                                        else:
                                                            print("dars eshtebah")
                                                            break
                                                    else:
                                                        print("ostad eshtebah")
                                                        break
                                                else:
                                                    print("saatha ekhtelal dare")
                                                    break
                                            else:
                                                print("saat payan eshtebah")
                                                break
                                        else:
                                            print("saat shoro eshtebah")
                                            break
                                    else:
                                        print("rooz eshtebah")
                                        break
                                else:
                                    print("code tekrary")
                                    break
                            else:
                                print("code eshtebah")
                                break

        
