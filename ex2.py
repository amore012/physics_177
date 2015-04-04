##Aaron Morefield
##Phys 177, Exercise 1
##April 1st, 2015


#Importing, just like the doctor ordered.
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

"""
#In this section, I start work on an input system for n number of students,
#This would make the program more flexible to use. I might later like to
#add in full capabilities, such as names, menus, and complete grading systems
students = raw_input "How many students are you entering grades for?"
"""
#Declaration of Variables at the Beginning of the program
Homework = [0,1,10,3,4,5,6,7]   # Student's Homework grades
Midterm = [8,9,10,10,8,7,6,5]   # Midterm Grades
FinalProject = [8,6,10,5,3,0,9,6] # Final Project grades  
FailedStudents = 0
Outstanding = 0
GradePlot = np.zeros((len(Homework))).astype(float)

#For loop to output each final grade.
for i in range(len(Homework)): 
    FinalGrade = (Homework[i]*0.4 + Midterm[i]*0.2 + FinalProject[i]*0.4)
    if FinalGrade < 5:  #determines if a student is failing.
        FailedStudents = FailedStudents + 1
    if FinalGrade > 9.5:    #determines if a student is Outstanding.
        Outstanding = Outstanding + 1
            
    GradePlot[i] = FinalGrade
    print "Student " + str(i+1) + "'s grade is " + str(FinalGrade) + "."



#Virtual Printer (since real ones run out of ink)
print GradePlot
"""plt.plot(GradePlot)
plt.ylabel('Grades')
plt.show()


people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
y_pos = np.arange(len(people))
performance = 3 + 10 * np.random.rand(len(people))
error = np.random.rand(len(people))

plt.barh(y_pos, performance, xerr=error, align='center', alpha=0.4)
plt.yticks(y_pos, people)
plt.xlabel('Performance')
plt.title('How fast do you want to go today?')

plt.savefig('test.png')
"""
print str(FailedStudents) + " Students have failed."
print str(Outstanding) + "/8 Students are outstanding."
print "Good Bye"