##Aaron Morefield
##Phys 177, Exercise 1
##April 1st, 2015


#Importing, just like the doctor ordered.

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt


"""
#In this section, I start work on an input system for n number of students,
#This would make the program more flexible to use. I might later like to
#add in full capabilities, such as names, menus, and complete grading systems
"""
print "Welcome to Aaron's grade calculator,"
print "1. Use random numbers to test the program?"
print "2. Input specific numbers to see actual students results?"
print "3. Change the weights of each category before preceding?"
choice = input ("Which would you like to do: ")
while not choice == 1 and not choice == 2 and not choice == 3:
    choice = input("That was not a correct input, please try again: ")

#Declaring standard weights to be used later
hw_w = 0.4 #Standard homework weight
fp_w = 0.4 #Standard Final Project weight
mt_w = 0.2 #Standard Midterm weight
if choice == 3:
    totalWeight = 0
    while totalWeight != 100:
        hw_w = float(raw_input("Please input the homework weight: %"))
        fp_w = float(raw_input("Please input the Final Project weight: %"))
        mt_w = float(raw_input("Please input the Midterm weight: %"))
        totalWeight = hw_w + fp_w + mt_w
        if totalWeight == 100:
            hw_w = hw_w/100.
            fp_w = fp_w/100.
            mt_w = mt_w/100.
            print "Thanks!"
            print ""
            print "Now which would you like to do?"
            choosiest = 0
            while choosiest != 1 and choosiest != 2:
                print "1. Use the random numbers to test the program?"
                print "2. Input specific numbers to see actual students results?"
                choosiest = input("Please select either: ")
                if choosiest == 1 or choosiest == 2:
                    choice = choosiest
                else:
                    print "That was not a valid entry. Please make a valid entry"
        else:
            print "Something didn't quite add up, please ensure the summed weight totals 100%!"

students = input ("How many students are you entering grades for? ")

if choice == 1:
    #Declaration of Variables at the Beginning of the program
    Homework = np.random.randint(0,11,students)   # Student's Homework grades
    Midterm = np.random.randint(0,11, students)   # Midterm Grades
    FinalProject = np.random.randint(0,11, students) # Final Project grades  

if choice == 2:
    #Declaration of Variables at the Beginning of the program
    Homework = np.zeros(students)   # Student's Homework grades
    Midterm = np.zeros(students)   # Midterm Grades
    FinalProject = np.zeros(students) # Final Project grades  
    for i in range(students):
        x=0
        y=0
        z=0
        while x<2:
            gradeholder = input("Please input student %s's homework grade: " %(i+1)) 
            if gradeholder <= 10 and gradeholder >= 0:
                Homework[i] = gradeholder
                x = 2
            else:
                print "That was not a valid grade."
                x = 1
        while y<2:
            gradeholder = input("Please input student %s's midterm grade: " %(i+1)) 
            if gradeholder <= 10 and gradeholder >= 0:
                Midterm[i] = gradeholder
                y = 2
            else:
                print "That was not a valid grade."
                y = 1
        while z<2:
            gradeholder = input("Please input student %s's final project grade: " %(i+1)) 
            if gradeholder <= 10 and gradeholder >= 0:
                FinalProject[i] = gradeholder
                z = 2
            else:
                print "That was not a valid grade."
                z = 1

#print(chr(27) + "[2J")
#Establishing the Bins for later
BinSizes = np.zeros(10)
for i in range(len(BinSizes)):
    BinSizes[i] = 1+i


GradePlot = np.zeros(students).astype(float)
FailedStudents = 0
Outstanding = 0
#For loop to output each final grade.
for i in range(students): 
    FinalGrade = (Homework[i]*hw_w + Midterm[i]*mt_w + FinalProject[i]*fp_w)
    if FinalGrade < 5:  #determines if a student is failing.
        FailedStudents = FailedStudents + 1
    if FinalGrade > 9.5:    #determines if a student is Outstanding.
        Outstanding = Outstanding + 1
    GradePlot[i] = FinalGrade
    GradePlot[i] = round(GradePlot[i],1)
    print "Student " + str(i+1) + "'s overall grade is " + str(FinalGrade) + "."



#Virtual Printer (since real ones run out of ink)
#print "BinSizes are : %s" %(BinSizes)
#print GradePlot

np.savetxt('StudentsGrades.txt', GradePlot, header='These are the students grades', footer='That is all')
plt.hist(GradePlot, bins = students, histtype = 'bar', range = (0,10))

plt.savefig('test.png')
print str(FailedStudents) + " Students have failed."
#print "hw_w = %s, fp_w = %s, mt_w = %s" %(hw_w, fp_w, mt_w)
print  "%s/%s Students are outstanding." %(Outstanding, students)
print "Good Bye"