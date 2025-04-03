Student=[]
Database=[Student]


def Add_student():
    ID= input('Enter ID')
    Name= input('Enter Name')
    Address= input('Enter Address')
    Phone_Number= input('Enter phone number')
    Email= input('Enter e-mail')
    Birthdate=input('Enter birthdate (YYYY-MM-DD)')
    Faculty= input('Enter Faculty')
    Courses= input('Enter Courses (comma-separated)')
    Courses_list= Courses.split(",")
    Student.append(ID)
    Student.append(Name)
    Student.append(Address)
    Student.append(Phone_Number)
    Student.append(Email)
    Student.append(Birthdate)
    Student.append(Faculty)
    Student.append(Courses_list)
    print('Student added successfully')
def Update_student():
    ID_check=input('enter ID')
    while True:
        if ID_check in Student:
            Name= input('Enter Name')
            if Name==' ':
                break
            else:
                Student[1]=Name

            Address= input('Enter Address')
            if Address==' ':
                break
            else:
                Student[2]=Address

            Phone_Number= input('Enter phone number')
            if Phone_Number==' ':
                break
            else:
                Student[3]=Phone_Number

            Email= input('Enter e-mail')
            if Email==' ':
                break
            else:
                Student[4]=Email

            Birthdate=input('Enter birthdate (YYYY-MM-DD)')
            if Birthdate==' ':
                break
            else:
                Student[5]=Birthdate

            Faculty= input('Enter Faculty')
            if Faculty==' ':
                break
            else:
                Student[6]=Faculty

            Courses= input('Enter Courses (comma-separated)')
            if Name==' ':
                break
            else:
                Courses_list= Courses.split(",")
                Student[7]=Courses_list
def Show_student():
    ID= input('enter ID')
    if ID in Student:
        print(Student)
    else:
        print('ID not found')
def Remove_student():
    ID= input('enter ID')
    if ID in Student:
        Database.remove(Student)
        print('Student removed successfully!')
    else:
        print('ID not found')


while True:
   print('1. Add student')
   print('2. Update student')
   print('3. show student')
   print('4.Remove student')
   print('5.Exit')
   Choice=input('Enter your choice')
   if Choice== '1':
       Add_student()
   elif Choice== '2':
       Update_student()
   elif Choice=='3':
       Show_student()
   elif Choice=='4':
       Remove_student()
   elif Choice =='5':
       break
   else:
       print('invalued option')

