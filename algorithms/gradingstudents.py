def gradingStudents(grades):
    diff = 0
    for each in range(len(grades)):
        if grades[each] >= 38:
            diff = 5-(grades[each]%5)
            if diff < 3:
                grades[each] = grades[each] + diff
    return grades


