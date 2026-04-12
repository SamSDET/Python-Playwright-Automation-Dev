fruits =['apple',"banana","orange"]
print(fruits[0])
fruits[1]="grape"
print(fruits)
print(len(fruits))

list1=[x for x in range(1,11)]
print(list1)
print(list1[:3])
print(list1[-3:])

list2=[5,2,9,1,7]
list2.sort()
print(list2)
list2.append(10)
print(list2)
list2.remove(2)
print(list2)

tuple1=(10,20)
print(tuple1[0])
list4=list(tuple1)
print(list4)
list4.append(30)
print(list4)
tuple2= tuple(list4)
print(tuple2)

Set1={1,2,3,3,4,5}
print(Set1)
Set1.add(6)
Set1.remove(2)
print(Set1)

a={1,2,3}
b={3,4,5}
union_set=a.union(b)
print(union_set)
intersection_set=a.intersection(b)
print(intersection_set)
difference_set=a.difference(b)
print(difference_set)

student ={"name": "Alice", "age": 20, "grade": "A"}
print(student["name"])
student["grade"]="B+"
print(student)
student['city']="New York"
print(student)

threefriends ={"Harry":9090843212,"Ron":9087654321,"Hermione":9076543210}
print(threefriends.keys())
print(threefriends.values())
for key,value in threefriends.items():
    print(f"{key}: {value}")

















