#Nicholas Boes - HW Grade Objects

from Grades_With_Objects_Classes import grades

def get_type_of_grade():
    #Checks to make sure input is HW or Exam
    loop = True
    while loop:
        gr_type = input("Enter the grade type (HW or Exam)->")
        if gr_type != "HW" and gr_type != "Exam":
            print(f"Illegal input: {gr_type} | State HW or Exam!")
        else:
            break
    return gr_type

def show_these_grades(g_type, scores):
    #Gets the scores and displays them
    ct = 0
    sc_tot = 0
    for sc in scores:
        if g_type == sc.get_grade_type():
            ct += 1
            score = (sc.get_score() / sc.get_total()) * 100
            sc_tot += score
            print(f"Name: {sc.get_name()} | Score: {score}")
    avg = round(sc_tot / ct, 2)
    print(f"Grade Ct: {ct} | Avg: {avg}")

def main():
    #Appends grade objects to list
    my_grades = []
    my_grades.append(grades("HW", "HW1", 90, 100))
    my_grades.append(grades("HW", "HW2", 8, 10))
    my_grades.append(grades("HW", "HW3", 80, 100))
    my_grades.append(grades("Exam", "Exam1", 90, 100))
    my_grades.append(grades("Exam", "Exam2", 95, 100))
    #Gets user input and displays the grades
    gr_type = get_type_of_grade()
    show_these_grades(gr_type, my_grades)
main()
