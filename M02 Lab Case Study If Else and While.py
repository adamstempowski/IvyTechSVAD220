# M02 Lab - Case Study If...Else and While
# Adam Stempowski
# 6/18/2022
# SDEV 220



#Write a python app that will accept student names and GPAs and test if the student qualifies
# for either the Dean's list or the Honor Roll. App has to:
    # Ask for and accept student's last name
    # Quit processing student records if the last name entered is 'ZZZ'
    # Ask for and accept a students first name
    # Ask for and accept student's GPA as a float.
    # Test if the student's GPA is >=3.5, and if so, print that the student has made the deans list.
    # Test if the students gpa is 3.25 or greater, and if so, print that the student has made the honor roll

zzz = False

while zzz == False:
    LastNameIn = input('Please enter a students Last name, or ZZZ to exit: ')
    if LastNameIn == "ZZZ":
        zzz = True
        break
    LastNameStr = str(LastNameIn)
    
    FirstNameIn = input('Please enter a students first name: ')
    FirstNameStr = str(FirstNameIn)

    GPAIn= input('Please enter a students GPA: ')
    GPAFloat = float(GPAIn)

    if GPAFloat >=3.5:
        print(FirstNameStr, LastNameStr, 'has made the Deans list')
    elif 3.25 <= GPAFloat < 3.5:
        print(FirstNameStr, LastNameStr, 'has made the Honor Roll')
    else:
        print(FirstNameStr, LastNameStr, 'did not make any academic lists')
