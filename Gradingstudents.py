def gradingstudents(grades):
    res =[]
    for grade in grades:
        if grade >= 38 and grade%5 >= 3:
            grade = grade + 5 - (grade%5)
        res.append(grade)
    return res


grades = [73,67,38,33]
print(gradingstudents(grades))