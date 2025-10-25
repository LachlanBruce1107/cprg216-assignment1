'''
Lachlan Bruce, Madelaine Smith, Raina Gradon-Jones.
Oct 24th, 2025
This program calculates the average GPA of a group of students. It works by first asking the user if they want to add a new student,
if the user inputs yes, then they are asked to input the name of the student they want to get the average GPA of. After the user
inputs the name, they then enter the GPA's from different subjects, these numbers are added to a list,
this continues in a loop until the user inputs -1 to stop inputting grades. After this the grades are 
averaged by taking the sum of the GPAs in the list divided by the amount of GPAs in the list, the average number is then put into a 
dictionary with the students name as the key. After this the process repeats, and the user is asked if they would like to 
add another student, if they answer no then the main loop is broken, and then another loop is run to print all the students and 
their average GPA from the dictionary. once all the names and GPA's are printed, the program ends.
'''

gpa_dict = dict()

print("Welcome to the Grade Registry Program")

#main loop for inputting students
while True:
    user_input = input("Would you like to add a new student? y(yes),n(no) \n").lower()
    
    #put in new student
    if user_input == "y" or user_input == "yes":
        gpa_list = []
        name = input("Enter the student's name: \n")
        gpa = float(input("Enter student GPA for each subject. Enter -1 to stop entering GPA. \n"))
        #small loop that puts the GPAs into the list
        while gpa != -1:
            gpa_list.append(gpa)
            gpa = float(input())
        #checks to make sure there are values in the gpa_list, so you dont divide by 0
        if len(gpa_list) != 0:
            average_gpa = sum(gpa_list) / len(gpa_list)
        #defaults to 0 if no GPA's are inputted
        else:
            average_gpa = 0
        #adds name and gpa to dictionary
        gpa_dict[name] = average_gpa
    #exits the loop if user inputs no
    elif user_input == "n" or user_input == "no":
        break
    else:
        print("Incorrect Input, please enter y(yes) n(no)")

#for loop that prints name and GPA, rounds GPA to 2 digits
for person in gpa_dict:
    print(person,round(gpa_dict[person],2))
