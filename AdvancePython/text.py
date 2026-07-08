    
N = int(input())
    
    # Initialize the empty list
my_list = []
    
    # Iterate through each command
for _ in range(N):
        # Split the input line into a command and its optional arguments
    parts = input().split()
    command = parts[0]
        
        # Match the command name with its corresponding list method
    if command == "insert":
        index = int(parts[1])
        element = int(parts[2])
        my_list.insert(index, element)
    elif command == "print":
        print(my_list)
    elif command == "remove":
        element = int(parts[1])
        my_list.remove(element)
    elif command == "append":
        element = int(parts[1])
        my_list.append(element)
    elif command == "sort":
        my_list.sort()
    elif command == "pop":
        my_list.pop()
    elif command == "reverse":
        my_list.reverse()