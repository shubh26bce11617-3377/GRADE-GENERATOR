students={}
n=int(input("Enter number of students: "))
for i in range(n):
    name=input("Enter student name: ")
    mark=float(input("Enter marks: "))
    students[name]=mark
total=0
for mark in students.values():
    total=total+mark
avg=total / n
print()
print("Class Average:",avg)
print()
for name in students:
    mark=students[name]
    diff=mark-avg
    if diff>=15:
        grade="A"
    elif diff>=5:
        grade="B"
    elif diff>=-5:
        grade="C"
    elif diff>=-15:
        grade="D"
    else:
        grade="F"
    print("Name:",name)
    print("Marks:",mark)
    print("Grade:",grade)
    print()
highname=""
highmark=-1
lowname=""
lowmark=101
for name in students:
    mark=students[name]
    if mark>highmark:
        highmark=mark
        highname=name
    if mark<lowmark:
        lowmark=mark
        lowname=name
print("Class Statistics")
print("----------------")
print("Highest Marks:",highmark)
print("Highest Scorer:",highname)
print("Lowest Marks:",lowmark)
print("Lowest Scorer:",lowname)