project = float(input("Enter the Project Score \n"))
internal = float(input("Enter the Internal Score \n"))
external = float(input("Enter the External Score \n"))

if project<50 or internal<50 or external<50 :
    if project<50 :
        print("You are failed in ",project)
    if internal<50 :
        print("You are failed in ",internal)
    if external<50 :
        print("You are failed in ",external)
else :
    total = project+internal+external
    pro_per = 0.7*total
    int_per = 0.1*total
    ext_per = 0.2*total
    grade_marks = pro_per+int_per+ext_per
    if grade_marks > 90 :
        print("A Grade")
    elif grade_marks >= 80 :
        print("B Grade")
    else :
        print("C Grade")