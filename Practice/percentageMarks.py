student_name = input('Name of the student : ')

def percentageMarks(maths_marks,physics_marks,english_marks):
    '''maths_marks = int(input('Marks of Maths : '))
    total_marks_maths = int(input('Enter total marks of Maths : '))
    physics_marks = int(input('Marks of Physics : '))
    total_marks_physics = int(input('Enter total marks of Physics : '))
    english_marks = int(input('Marks of English : '))
    total_marks_english = int(input('Enter total marks of English : '))
    chemistry_marks = int(input('Marks of Chemistry : '))
    total_marks_chemistry = int(input('Enter total marks of Chemistry : '))
    hindi_marks = int(input('Marks of Hindi : '))
    total_marks_hindi = int(input('Enter total marks of Hindi : '))'''

    #percentage_marks = ''

    #Total = (total_marks_maths + total_marks_english + total_marks_physics)# + total_marks_chemistry + total_marks_hindi)
    percentage_marks = ((maths_marks + physics_marks + english_marks)*100)/300 # + chemistry_marks + hindi_marks)*100)/Total
    if percentage_marks >= 90:
        print(student_name + ' scored ' + str("{:.2f}".format(percentage_marks)) + '%' " - GRADE 'A' in exams")
    elif percentage_marks >= 80:
        print(student_name + ' scored ' + str("{:.2f}".format(percentage_marks)) + '%' " - GRADE 'B' in exams")
    elif percentage_marks >= 70:
        print(student_name + ' scored ' + str("{:.2f}".format(percentage_marks)) + '%' " - GRADE 'C' in exams")
    elif percentage_marks >= 60:
        print(student_name + ' scored ' + str("{:.2f}".format(percentage_marks)) + '%' " - GRADE 'D' in exams")
    elif percentage_marks >= 50:
        print(student_name + ' scored ' + str("{:.2f}".format(percentage_marks)) + '%' " - GRADE 'E' in exams")
    elif percentage_marks >= 40:
        print(student_name + ' scored ' + str("{:.2f}".format(percentage_marks)) + '%' " - GRADE 'F' in exams")
    elif percentage_marks >= 33 and percentage_marks < 40:
        print(student_name + ' scored ' + str("{:.2f}".format(percentage_marks)) + '%' " - GRADE 'G' in exams")
    else:
        print(student_name + ' scored ' + str("{:.2f}".format(percentage_marks)) + '%' " - FAIL in exams")
    return

percentageMarks(25,30,35)