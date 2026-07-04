
alpha = {}

for i in range(int(input("Enter number of students: "))):

    line = input("Enter name and marks with space: ").split()
    name = line[0]
    scores = [float(mark) for mark in line[1:]]
    alpha[name] = scores

    
query_name = input("Enter the name of the student to query: ")
if query_name in alpha:
    average = sum(alpha[query_name]) / len(alpha[query_name])
    print(f"{query_name}'s average score: {average:.2f}")