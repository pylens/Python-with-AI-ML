# Student grade calculator

def getTotal(marks):
    return sum(marks)

def getEverage(marks):
    return sum(marks) / len(marks)

def getGrade(average):

    if average >= 90:
        return "A"
    elif average >=75:
        return "B"
    elif average >= 50:
        return "C"
    else:
        return "F"
    

def studentReport(marks):
    total = getTotal(marks)
    average = getEverage(marks)
    grade = getGrade(average)

    return f"Student exam report: \ntotal : {total}\nAverage : {average}\nGrade : {grade}"

print(studentReport([50, 70, 90, 68]))

