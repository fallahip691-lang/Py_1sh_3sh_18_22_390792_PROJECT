import time
import threading

count=0

def quiz(grade:int,student):
    print("for exit type exit")

    count = student["count"]
    count += 1
    student["count"] = count
    def timer():
        global seconds
        seconds = 1200
        while seconds > 0:
            
            time.sleep(1)
            seconds -= 1 
        print()
        print("-----vaght tamom shod------")
       
        


    timer_thread = threading.Thread(target=timer)
    timer_thread.start()
    grade=0
    grade=max(0,grade)
    
    while True:
        if count==1:
                t1=input(" 1.how many ballondior lionel messi have? 1.2  2.5  3.6 4.8 ")
                match t1:
                    case"1":
                        if grade >0:
                            grade-=1
                    case "2":
                        if grade >0:
                            grade-=1
                    case "3":
                        if grade >0:
                            grade-=1
                    case "4":
                        grade=grade+1
                    
                    case "exit":
                        seconds = 0
                        break
                if seconds == 0:
                    break
                
                  

                t2=input(" 1.capital of iran? 1.yazd  2.shiraz  3.tehran 4.sfahan ")
                match t2:
                    case"1":
                        if grade >0:
                            grade-=1
                    case "2":
                        if grade >0:
                            grade-=1
                    case "3":
                        grade=grade+1
                    case "4":
                        if grade >0:
                            grade-=1
                    
                    case "exit":
                        seconds = 0
                        break
                if seconds == 0:
                    break
                  
                t3 = input("3. What is the capital of France? 1.Berlin  2.Paris  3.Rome  4.Madrid ")
                match t3:
                    case "1":
                        if grade > 0:
                            grade-=1
                    case "2":
                        grade = grade + 1
                    case "3":
                        if grade > 0:
                            grade-=1
                    case "4":
                        if grade > 0:
                            grade-=1
                    case "exit":
                        seconds = 0
                        break
                if seconds == 0:
                    break

                t4 = input("4. How many planets are in the Solar System? 1.7  2.8  3.9  4.10 ")
                match t4:
                    case "1":
                        if grade > 0:
                            grade-=1
                    case "2":
                        grade = grade + 1
                    case "3":
                        if grade > 0:
                            grade-=1
                    case "4":
                        if grade > 0:
                            grade-=1
                    case "exit":
                        seconds = 0
                        break
                if seconds == 0:
                    break

                t5 = input("5. Which language is used for web page structure? 1.Python  2.HTML  3.C++  4.Java ")
                match t5:
                    case "1":
                        if grade > 0:
                            grade-=1
                    case "2":
                        grade = grade + 1
                    case "3":
                        if grade > 0:
                            grade-=1
                    case "4":
                        if grade > 0:
                            grade-=1
                    case "exit":
                        seconds = 0
                        break
                if seconds == 0:
                    break

                t6 = input("6. What is 12 * 8? 1.86  2.92  3.96  4.108 ")
                match t6:
                    case "1":
                        if grade > 0:
                            grade-=1
                    case "2":
                        if grade > 0:
                            grade-=1
                    case "3":
                        grade = grade + 1
                    case "4":
                        if grade > 0:
                            grade-=1
                    case "exit":
                        seconds = 0
                        break
                if seconds == 0:
                    break

                t7 = input("7. Which animal is the largest animal? 1.Elephant  2.Blue whale  3.Giraffe  4.Shark ")
                match t7:
                    case "1":
                        if grade > 0:
                            grade-=1
                    case "2":
                        grade = grade + 1
                    case "3":
                        if grade > 0:
                            grade-=1
                    case "4":
                        if grade > 0:
                            grade-=1
                    case "exit":
                        seconds = 0
                        break
                if seconds == 0:
                    break

                t8 = input("8. What is the chemical symbol for water? 1.CO2  2.O2  3.H2O  4.NaCl ")
                match t8:
                    case "1":
                        if grade > 0:
                            grade-=1
                    case "2":
                        if grade > 0:
                            grade-=1
                    case "3":
                        grade = grade + 1
                    case "4":
                        if grade > 0:
                            grade-=1
                    case "exit":
                        seconds = 0
                        break
                if seconds == 0:
                    break

                t9 = input("9. Which planet is known as the Red Planet? 1.Venus  2.Mars  3.Jupiter  4.Saturn ")
                match t9:
                    case "1":
                        if grade > 0:
                            grade-=1
                    case "2":
                        grade = grade + 1
                    case "3":
                        if grade > 0:
                            grade-=1
                    case "4":
                        if grade > 0:
                            grade-=1
                    case "exit":
                        seconds = 0
                        break
                if seconds == 0:
                    break

                t10 = input("10. What is the fastest land animal? 1.Lion  2.Cheetah  3.Horse  4.Tiger ")
                match t10:
                    case "1":
                        if grade > 0:
                            grade-=1
                    case "2":
                        grade = grade + 1
                    case "3":
                        if grade > 0:
                            grade-=1
                    case "4":
                        if grade > 0:
                            grade-=1
                    case "exit":
                        seconds = 0
                        break
                if seconds == 0:
                    break

                t11 = input("11. How many sides does a hexagon have? 1.5  2.6  3.7  4.8 ")
                match t11:
                    case "1":
                        if grade > 0:
                            grade-=1
                    case "2":
                        grade = grade + 1
                    case "3":
                        if grade > 0:
                            grade-=1
                    case "4":
                        if grade > 0:
                            grade-=1
                    case "exit":
                        seconds = 0
                        break
                if seconds == 0:
                    break

                t12 = input("12. Which country invented pizza? 1.France  2.Germany  3.Italy  4.Spain ")
                match t12:
                    case "1":
                        if grade > 0:
                            grade-=1
                    case "2":
                        if grade > 0:
                            grade-=1
                    case "3":
                        grade = grade + 1
                    case "4":
                        if grade > 0:
                            grade-=1
                    case "exit":
                        seconds = 0
                        break
                if seconds == 0:
                    break

                t13 = input("13. What is the largest ocean? 1.Atlantic  2.Indian  3.Arctic  4.Pacific ")
                match t13:
                    case "1":
                        if grade > 0:
                            grade-=1
                    case "2":
                        if grade > 0:
                            grade-=1
                    case "3":
                        if grade > 0:
                            grade-=1
                    case "4":
                        grade = grade + 1
                    case "exit":
                        seconds = 0
                        break
                if seconds == 0:
                    break

                t14 = input("14. Which gas do plants absorb? 1.Oxygen  2.Carbon dioxide  3.Nitrogen  4.Hydrogen ")
                match t14:
                    case "1":
                        if grade > 0:
                            grade-=1
                    case "2":
                        grade = grade + 1
                    case "3":
                        if grade > 0:
                            grade-=1
                    case "4":
                        if grade > 0:
                            grade-=1
                    case "exit":
                        seconds = 0
                        break
                if seconds == 0:
                    break

                t15 = input("15. How many days are in a leap year? 1.364  2.365  3.366  4.367 ")
                match t15:
                    case "1":
                        if grade > 0:
                            grade-=1
                    case "2":
                        if grade > 0:
                            grade-=1
                    case "3":
                        grade = grade + 1
                    case "4":
                        if grade > 0:
                            grade-=1
                    case "exit":
                        seconds = 0
                        break
                if seconds == 0:
                    break

                t16 = input("16. Who wrote Romeo and Juliet? 1.Charles Dickens  2.William Shakespeare  3.Mark Twain  4.J.K. Rowling ")
                match t16:
                    case "1":
                        if grade > 0:
                            grade-=1
                    case "2":
                        grade = grade + 1
                    case "3":
                        if grade > 0:
                            grade-=1
                    case "4":
                        if grade > 0:
                            grade-=1
                    case "exit":
                        seconds = 0
                        break
                if seconds == 0:
                    break

                t17 = input("17. What is the square root of 144? 1.10  2.11  3.12  4.14 ")
                match t17:
                    case "1":
                        if grade > 0:
                            grade-=1
                    case "2":
                        if grade > 0:
                            grade-=1
                    case "3":
                        grade = grade + 1
                    case "4":
                        if grade > 0:
                            grade-=1
                    case "exit":
                        seconds = 0
                        break
                if seconds == 0:
                    break

                t18 = input("18. Which is the smallest continent? 1.Asia  2.Europe  3.Australia  4.Africa ")
                match t18:
                    case "1":
                        if grade > 0:
                            grade-=1
                    case "2":
                        if grade > 0:
                            grade-=1
                    case "3":
                        grade = grade + 1
                    case "4":
                        if grade > 0:
                            grade-=1
                    case "exit":
                        seconds = 0
                        break
                if seconds == 0:
                    break

                t19 = input("19. What is the currency of Japan? 1.Dollar  2.Yen  3.Euro  4.Pound ")
                match t19:
                    case "1":
                        if grade > 0:
                            grade-=1
                    case "2":
                        grade = grade + 1
                    case "3":
                        if grade > 0:
                            grade-=1
                    case "4":
                        if grade > 0:
                            grade-=1
                    case "exit":
                        seconds = 0
                        break
                if seconds == 0:
                    break

                t20 = input("20. How many bones are in an adult human body? 1.196  2.206  3.216  4.226 ")
                match t20:
                    case "1":
                        if grade > 0:
                            grade-=1
                    case "2":
                        grade = grade + 1
                    case "3":
                        if grade > 0:
                            grade-=1
                    case "4":
                        if grade > 0:
                            grade-=1
                    case "exit":
                        seconds = 0
                        break
                if seconds == 0:
                    break

                t21 = input("21. Which is the closest star to Earth? 1.Sirius  2.Sun  3.Polaris  4.Vega ")
                match t21:
                    case "1":
                        if grade > 0:
                            grade-=1
                    case "2":
                        grade = grade + 1
                    case "3":
                        if grade > 0:
                            grade-=1
                    case "4":
                        if grade > 0:
                            grade-=1
                    case "exit":
                        seconds = 0
                        break
                if seconds == 0:
                    break

                t22 = input("22. What is 15 squared? 1.125  2.200  3.225  4.250 ")
                match t22:
                    case "1":
                        if grade > 0:
                            grade-=1
                    case "2":
                        if grade > 0:
                            grade-=1
                    case "3":
                        grade = grade + 1
                    case "4":
                        if grade > 0:
                            grade-=1
                    case "exit":
                        seconds = 0
                        break
                if seconds == 0:
                    break

                t23 = input("23. Which organ pumps blood? 1.Lungs  2.Brain  3.Heart  4.Liver ")
                match t23:
                    case "1":
                        if grade > 0:
                            grade-=1
                    case "2":
                        if grade > 0:
                            grade-=1
                    case "3":
                        grade = grade + 1
                    case "4":
                        if grade > 0:
                            grade-=1
                    case "exit":
                        seconds = 0
                        break
                if seconds == 0:
                    break

                t24 = input("24. What is the main language of Brazil? 1.Spanish  2.Portuguese  3.English  4.French ")
                match t24:
                    case "1":
                        if grade > 0:
                            grade-=1
                    case "2":
                        grade = grade + 1
                    case "3":
                        if grade > 0:
                            grade-=1
                    case "4":
                        if grade > 0:
                            grade-=1
                    case "exit":
                        seconds = 0
                        break
                if seconds == 0:
                    break

                t25 = input("25. Which metal is liquid at room temperature? 1.Iron  2.Gold  3.Mercury  4.Silver ")
                match t25:
                    case "1":
                        if grade > 0:
                            grade-=1
                    case "2":
                        if grade > 0:
                            grade-=1
                    case "3":
                        grade = grade + 1
                    case "4":
                        if grade > 0:
                            grade-=1
                    case "exit":
                        seconds = 0
                        break
                if seconds == 0:
                    break
        elif count == 2:           
                t1 = input("1. How many players are on a football team on the field? 1.9  2.10  3.11  4.12 ")
                match t1:
                        case "1":
                            if grade > 0:
                                grade-=1
                        case "2":
                            if grade > 0:
                                grade-=1
                        case "3":
                            grade = grade + 1
                        case "4":
                            if grade > 0:
                                grade-=1
                        case "exit":
                            seconds = 0
                            break
                if seconds == 0:
                        break
                t2 = input("2. Which is the tallest mountain in the world? 1.K2  2.Everest  3.Kilimanjaro  4.Denali ")
                match t2:
                    case "1":
                        if grade > 0:
                            grade-=1
                    case "2":
                        grade = grade + 1
                    case "3":
                        if grade > 0:
                            grade-=1
                    case "4":
                        if grade > 0:
                            grade-=1
                    case "exit":
                        seconds = 0
                        break
                if seconds == 0:
                    break
                t3 = input("3. What does CPU stand for? 1.Computer Power Unit  2.Central Processing Unit  3.Control Program Utility  4.Core Processing User ")
                match t3:
                    case "1":
                        if grade > 0:
                            grade-=1
                    case "2":
                        grade = grade + 1
                    case "3":
                        if grade > 0:
                            grade-=1
                    case "4":
                        if grade > 0:
                            grade-=1
                    case "exit":
                        seconds = 0
                        break
                if seconds == 0:
                    break
                t4 = input("4. Which planet has the most famous rings? 1.Mars  2.Earth  3.Saturn  4.Mercury ")
                match t4:
                    case "1":
                        if grade > 0:
                            grade-=1
                    case "2":
                        if grade > 0:
                            grade-=1
                    case "3":
                        grade = grade + 1
                    case "4":
                        if grade > 0:
                            grade-=1
                    case "exit":
                        seconds = 0
                        break
                if seconds == 0:
                    break
                t5 = input("5. What is the boiling point of water at sea level? 1.50°C  2.75°C  3.100°C  4.150°C ")
                match t5:
                    case "1":
                        if grade > 0:
                            grade-=1
                    case "2":
                        if grade > 0:
                            grade-=1
                    case "3":
                        grade = grade + 1
                    case "4":
                        if grade > 0:
                            grade-=1
                    case "exit":
                        seconds = 0
                        break
                if seconds == 0:
                    break
                t6 = input("6. Which country has the city of Cairo? 1.Morocco  2.Egypt  3.Turkey  4.Greece ")
                match t6:
                    case "1":
                        if grade > 0:
                            grade-=1
                    case "2":
                        grade = grade + 1
                    case "3":
                        if grade > 0:
                            grade-=1
                    case "4":
                        if grade > 0:
                            grade-=1
                    case "exit":
                        seconds = 0
                        break
                if seconds == 0:
                    break
                t7 = input("7. What is the opposite of ancient? 1.Old  2.Modern  3.Historic  4.Traditional ")
                match t7:
                    case "1":
                        if grade > 0:
                            grade-=1
                    case "2":
                        grade = grade + 1
                    case "3":
                        if grade > 0:
                            grade-=1
                    case "4":
                        if grade > 0:
                            grade-=1
                    case "exit":
                        seconds = 0
                        break
                if seconds == 0:
                    break
                t8 = input("8. Which instrument has keys, pedals, and strings? 1.Guitar  2.Piano  3.Flute  4.Drum ")
                match t8:
                    case "1":
                        if grade > 0:
                            grade-=1
                    case "2":
                        grade = grade + 1
                    case "3":
                        if grade > 0:
                            grade-=1
                    case "4":
                        if grade > 0:
                            grade-=1
                    case "exit":
                        seconds = 0
                        break
                if seconds == 0:
                    break
                t9 = input("9. What is the largest desert in the world? 1.Sahara  2.Gobi  3.Antarctic Desert  4.Arabian Desert ")
                match t9:
                    case "1":
                        if grade > 0:
                            grade-=1
                    case "2":
                        if grade > 0:
                            grade-=1
                    case "3":
                        grade = grade + 1
                    case "4":
                        if grade > 0:
                            grade-=1
                    case "exit":
                        seconds = 0
                        break
                if seconds == 0:
                    break
                t10 = input("10. Which programming language is named after a snake? 1.Java  2.Python  3.Ruby  4.Swift ")
                match t10:
                    case "1":
                        if grade > 0:
                            grade-=1
                    case "2":
                        grade = grade + 1
                    case "3":
                        if grade > 0:
                            grade-=1
                    case "4":
                        if grade > 0:
                            grade-=1
                    case "exit":
                        seconds = 0
                        break
                if seconds == 0:
                    break
                t11 = input("11. How many minutes are in two hours? 1.60  2.90  3.120  4.180 ")
                match t11:
                    case "1":
                        if grade > 0:
                            grade-=1
                    case "2":
                        if grade > 0:
                            grade-=1
                    case "3":
                        grade = grade + 1
                    case "4":
                        if grade > 0:
                            grade-=1
                    case "exit":
                        seconds = 0
                        break
                if seconds == 0:
                    break
                t12 = input("12. Which bird is famous for its ability to mimic speech? 1.Eagle  2.Parrot  3.Penguin  4.Owl ")
                match t12:
                    case "1":
                        if grade > 0:
                            grade-=1
                    case "2":
                        grade = grade + 1
                    case "3":
                        if grade > 0:
                            grade-=1
                    case "4":
                        if grade > 0:
                            grade-=1
                    case "exit":
                        seconds = 0
                        break
                if seconds == 0:
                    break
                t13 = input("13. What is the freezing point of water? 1.0°C  2.10°C  3.32°C  4.100°C ")
                match t13:
                    case "1":
                        grade = grade + 1
                    case "2":
                        if grade > 0:
                            grade-=1
                    case "3":
                        if grade > 0:
                            grade-=1
                    case "4":
                        if grade > 0:
                            grade-=1
                    case "exit":
                        seconds = 0
                        break
                if seconds == 0:
                    break
                t14 = input("14. Which country is famous for the Eiffel Tower? 1.Italy  2.France  3.Germany  4.Belgium ")
                match t14:
                    case "1":
                        if grade > 0:
                            grade-=1
                    case "2":
                        grade = grade + 1
                    case "3":
                        if grade > 0:
                            grade-=1
                    case "4":
                        if grade > 0:
                            grade-=1
                    case "exit":
                        seconds = 0
                        break
                if seconds == 0:
                    break
                t15 = input("15. What is 100 divided by 4? 1.20  2.25  3.30  4.40 ")
                match t15:
                    case "1":
                        if grade > 0:
                            grade-=1
                    case "2":
                        grade = grade + 1
                    case "3":
                        if grade > 0:
                            grade-=1
                    case "4":
                        if grade > 0:
                            grade-=1
                    case "exit":
                        seconds = 0
                        break
                if seconds == 0:
                    break
                t16 = input("16. Which is the largest planet? 1.Earth  2.Mars  3.Jupiter  4.Venus ")
                match t16:
                    case "1":
                        if grade > 0:
                            grade-=1
                    case "2":
                        if grade > 0:
                            grade-=1
                    case "3":
                        grade = grade + 1
                    case "4":
                        if grade > 0:
                            grade-=1
                    case "exit":
                        seconds = 0
                        break
                if seconds == 0:
                    break
                t17 = input("17. What is the capital of Germany? 1.Munich  2.Berlin  3.Hamburg  4.Frankfurt ")
                match t17:
                    case "1":
                        if grade > 0:
                            grade-=1
                    case "2":
                        grade = grade + 1
                    case "3":
                        if grade > 0:
                            grade-=1
                    case "4":
                        if grade > 0:
                            grade-=1
                    case "exit":
                        seconds = 0
                        break
                if seconds == 0:
                    break
                t18 = input("18. Which part of a computer displays images? 1.Keyboard  2.Mouse  3.Monitor  4.Printer ")
                match t18:
                    case "1":
                        if grade > 0:
                            grade-=1
                    case "2":
                        if grade > 0:
                            grade-=1
                    case "3":
                        grade = grade + 1
                    case "4":
                        if grade > 0:
                            grade-=1
                    case "exit":
                        seconds = 0
                        break
                if seconds == 0:
                    break
                t19 = input("19. How many colors are in a rainbow? 1.5  2.6  3.7  4.8 ")
                match t19:
                    case "1":
                        if grade > 0:
                            grade-=1
                    case "2":
                        if grade > 0:
                            grade-=1
                    case "3":
                        grade = grade + 1
                    case "4":
                        if grade > 0:
                            grade-=1
                    case "exit":
                        seconds = 0
                        break
                if seconds == 0:
                    break
                t20 = input("20. Which animal is known as the king of the jungle? 1.Tiger  2.Lion  3.Elephant  4.Wolf ")
                match t20:
                    case "1":
                        if grade > 0:
                            grade-=1
                    case "2":
                        grade = grade + 1
                    case "3":
                        if grade > 0:
                            grade-=1
                    case "4":
                        if grade > 0:
                            grade-=1
                    case "exit":
                        seconds = 0
                        break
                if seconds == 0:
                    break
                t21 = input("21. What is the chemical symbol for gold? 1.Ag  2.Fe  3.Au  4.Gd ")
                match t21:
                    case "1":
                        if grade > 0:
                            grade-=1
                    case "2":
                        if grade > 0:
                            grade-=1
                    case "3":
                        grade = grade + 1
                    case "4":
                        if grade > 0:
                            grade-=1
                    case "exit":
                        seconds = 0
                        break
                if seconds == 0:
                    break
                t22 = input("22. Which ocean is between Africa and Australia? 1.Atlantic  2.Pacific  3.Indian  4.Arctic ")
                match t22:
                    case "1":
                        if grade > 0:
                            grade-=1
                    case "2":
                        if grade > 0:
                            grade-=1
                    case "3":
                        grade = grade + 1
                    case "4":
                        if grade > 0:
                            grade-=1
                    case "exit":
                        seconds = 0
                        break
                if seconds == 0:
                    break
                t23 = input("23. What is the main source of energy for Earth? 1.Moon  2.Sun  3.Wind  4.Ocean ")
                match t23:
                    case "1":
                        if grade > 0:
                            grade-=1
                    case "2":
                        grade = grade + 1
                    case "3":
                        if grade > 0:
                            grade-=1
                    case "4":
                        if grade > 0:
                            grade-=1
                    case "exit":
                        seconds = 0
                        break
                if seconds == 0:
                    break
                t24 = input("24. Which device is used to measure temperature? 1.Barometer  2.Thermometer  3.Speedometer  4.Compass ")
                match t24:
                    case "1":
                        if grade > 0:
                            grade-=1
                    case "2":
                        grade = grade + 1
                    case "3":
                        if grade > 0:
                            grade-=1
                    case "4":
                        if grade > 0:
                            grade-=1
                    case "exit":
                        seconds = 0
                        break
                if seconds == 0:
                    break
                t25 = input("25. What is the capital of Australia? 1.Sydney  2.Melbourne  3.Canberra  4.Perth ")
                match t25:
                    case "1":
                        if grade > 0:
                            grade-=1
                    case "2":
                        if grade > 0:
                            grade-=1
                    case "3":
                        grade = grade + 1
                    case "4":
                        if grade > 0:
                            grade-=1
                    case "exit":
                        seconds = 0
                        break
                if seconds == 0:
                    break
        elif     count>2:
                print("bish az had mojaz")
                break
            


    return grade ,count







