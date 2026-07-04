students =[]
for _ in range(int(input("Enter number of students: "))):
    line = input("Enter name and marks separated by space: ").split()
    name = line[0]
    marks = float(line[1])
    students.append([name, marks])

unique_marks = set(x[1] for x in students)
print("Unique marks:", unique_marks)
sorted_marks = sorted(unique_marks)
print("Sorted unique marks:", sorted_marks)
target = sorted_marks[1]
matchingname=[]
for x in students:
    if x[1] == target:
        matchingname.append(x[0])

x=sorted(matchingname)
print("Students with the second lowest marks:", x)

