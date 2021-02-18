studentNames = []
studentMidTerms = []
studentFinals = []
studentHomeworks = []
info = []

for i in range(0,5):
    name = input("Enter Full Name:  ")
    midTerm = int(input("Mid Term  Note: "))
    final = int(input("Final Note: "))
    homework = int(input("Homework Note: "))

    studentNames.append(name)
    studentMidTerms.append(midTerm)
    studentFinals.append(final)
    studentHomeworks.append(homework)
 
    print("")
    print("Bilgiler kaydediliyor...")
    print(" FullName:{} " " MidTerm:{} " " Final:{} " " Homework:{}\n ".format(studentNames,studentMidTerms,studentFinals,studentHomeworks))
    dic = {"FullName": name, "MidTerm": midTerm, "FinalNote": final,"HomeworkNote": homework}
    info.append(dic)


midTermSorted = sorted(info, key=lambda k: k['MidTerm'], reverse=True)
print("")
print("{} is the best midterm score with {}".format(midTermSorted[0]["FullName"],midTermSorted[0]["MidTerm"]))

finalSorted = sorted(info, key=lambda k: k['FinalNote'], reverse=True)
print("")
print("{} is the best final score with {}".format(finalSorted[0]["FullName"],finalSorted[0]["FinalNote"]))

homeworkSorted = sorted(info, key=lambda k: k['HomeworkNote'], reverse=True)
print("")
print("{} is the best homework score with {}".format(homeworkSorted[0]["FullName"],homeworkSorted[0]["HomeworkNote"]))
