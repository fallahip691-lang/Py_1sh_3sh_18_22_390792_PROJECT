





def edit(shomare_class, class_code, days, hours, topics, teacher_list, class_mojtama):

    if shomare_class in class_mojtama:
        print(class_mojtama[shomare_class])

        while True:
            menu = input("1.week day 2.saat 3.dars 4.ostad 5.exit: ")

            match menu:
                case "1":
                    weak_day1 = input("rooz: ")

                    if weak_day1 in days:
                        class_mojtama[shomare_class]["rooz"] = weak_day1
                        print("rooz edited")
                    else:
                        print("rooz eshtebah")

                case "2":
                    menu = input("saat: 1.shoro 2.payan: ")

                    match menu:
                        case "1":
                            saat_1_ = input("saat: ")

                            if saat_1_ in hours:
                                class_mojtama[shomare_class]["saat shoro"] = saat_1_
                                print("saat shoro edited")
                            else:
                                print("saat eshtebah")

                        case "2":
                            saat_2_ = input("saat: ")

                            if saat_2_ in hours:
                                class_mojtama[shomare_class]["saat payan"] = saat_2_
                                print("saat payan edited")
                            else:
                                print("saat eshtebah")

                case "3":
                    topic_ = input("dars: ")

                    if topic_ in topics:
                        class_mojtama[shomare_class]["dars"] = topic_
                        print("dars edited")
                    else:
                        print("dars eshtebah")

                case "4":
                    ostad_ = input("ostad: ")

                    if ostad_ in teacher_list:
                        class_mojtama[shomare_class]["ostad"] = ostad_
                        print("ostad edited")
                    else:
                        print("ostad eshtebah")

                case "5":
                    return class_mojtama

        return class_mojtama

    else:
        print("class not found")
        return class_mojtama
