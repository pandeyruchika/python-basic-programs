students=[]
def add():
    name= input("Enter student's name:")
    rno= int(input("Enter roll no:"))
    marks= int(input("Enter total marks obtained:"))
    perc= (marks/500)*100
    student = {
        "rno":rno,
        "name": name,
        "marks": marks,
        "percentage":perc}
    students.append(student)
    print("details added successfully...")

def search():
    n=int(input("enter roll number to be searched:"))
    for i in students:
        if i["rno"]==n:
            print(i)
            return
    print("student not found")

while True:
    print("1. Add student details \n2. View student details \n3. search student details \n4. Exit")

    choice= int(input("Enter your choice:"))
    
    if choice==1:
        add()
    elif choice==2:
        print("Current students list:")
        print(students)
    elif choice==3:
        search()
    elif choice==4:
        print("exiting...")
        break