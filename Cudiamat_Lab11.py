grade = 1 
stdntpassed = 0
list = []
stdnt_num = 1
while grade !=0:
    grade = int(input(f"Enter Grade of student {stdnt_num}: "))
    if grade < 40 or grade > 100:
        print("INVALID GRADE")
        break
    else:
        list.append(grade)
        stdnt_num += 1
        if grade >= 75:
            stdntpassed += 1
    
    add_grde = input("Do you want to add another grade? (Continue/done: ")
    
    if (add_grde.lower() == "continue"):
        continue
    elif (add_grde.lower() == "done"):
        sum_list = sum(list)
        avrg = (sum_list / len(list))
        avrg = round(avrg, 2)
        
        passing = (stdntpassed/len(list)*100)
        passing = round(passing, 2)
        
        print(f"Average grade: {avrg:.2f}")
        print(f"Student Passed: {stdntpassed}")
        print(f"Passing Percent: {passing:.2f}")
        
        break
    else:
        print("INVALID QUOTE")
        break
    
    
    
