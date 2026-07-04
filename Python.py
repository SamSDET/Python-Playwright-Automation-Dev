n = int(input())
arr = map(int, input().split())
a = list(arr)
first = -101
second =-101
for items in a:
    if items > first:
        second=first
        first=items
    elif items>second and items<first:
        second=items
    
print(second)
    
    
