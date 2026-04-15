list1=[]
list1=input("Enter a list of numbers separated by commas: ").split(",")
print(list1)
set1=set(list1)
print(sorted(set1,reverse=True))


dict1={1: 63000, "Pixel 10": 68000, 3: 82000, "Pixel 10a": 43000}
hv=0
hk=None
for key in dict1:
    if dict1[key]>hv:
        hv=dict1[key]
        hk=key
print(f"Key with highest value: {hk}, Value: {hv}")
maxf=max(dict1, key=dict1.get)
print(f"Key with highest value using max(): {maxf}, Value: {dict1[maxf]}")
print(dict1[3])

dict1={1: 63000, "Pixel 10": 68000, 3: 82000, "Pixel 10a": 43000}
dict2={4: 75000, "Pixel 11": 90000, 5: 85000, "Pixel 11a": 50000}
merged_dict=dict1 | dict2
print(merged_dict)
