#N student take K apple and distribute them among each other evenly. The remaining (the undivisible) part remains in the basket.
#How many apples will remain in the baskett. The program read number N and K. It should print the two answer for the above question.
stu=int(input("enter a number of student in class:"))
app=int(input("enter the number of apples:"))
div=(app/stu)
remain=(app%stu)
print("Each student get :",div)
print("the remaining apple",remain)
