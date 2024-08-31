def get_students():
    students={}    
    num_students=int(input("enter the num of students : "))
    for i in range(num_students):
        student=input("enter the name of the student :").lower()
        for j in range(2):
            list_of_notes=[]
            note=int(input("enter note : "))
            list_of_notes.append(note)
        students[student]=list_of_notes
    return students
def get_high_note(students):
    recherch=input("enter the name of the student you are looking for : ").lower()
    if recherch in students:
        list_n=students.get(recherch)
        high_note=max(list_n)
        return high_note
    else:
        return "no student with that name"
students=get_students()
print(get_high_note(students))