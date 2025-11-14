def sum(a,b):
    '''The sum of two numbers and global keyword'''
    print("hi")
    global z
    z=123
    return a+b
    
z =98
print(sum(3,13))
print(z)
print(sum.__doc__)


