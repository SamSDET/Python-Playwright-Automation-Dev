
while True:
    try:
        a = int(input("Enter Number 1: "))
        b = int(input("Enter Number 2: "))
        print(f"The division is {a / b}")
    except ValueError:
        print("Please dont perform bad typecasts")
    except ZeroDivisionError:
        print("Hey dont divide with zero")
    except Exception as e:
        print("Invalid Inpsut", e)

