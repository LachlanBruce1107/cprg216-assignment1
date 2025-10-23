#first person: if following flow chart, go from "gpa_list = []" to the entire "while gpa != -1 loop"
#second person: if following flow chart, go from "if length gpa_list != 0" and complete the for loop
#if you want you can add comments explaining what different parts of the code do, but im also chill with writing them after.
#let me know if any problems show up :)

gpa_dict = dict()

print("Welcome to the Grade Registry Program")

while True:
    user_input = input("Would you like to add a new student? y(yes),n(no) \n").lower()
    
    if user_input == "y" or user_input == "yes":

    elif user_input == "n" or user_input == "no":
        break
    else:
        print("Incorrect Input, please enter y(yes) n(no)")
