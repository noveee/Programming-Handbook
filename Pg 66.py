# Challenge 1 
def square():
    """
    Takes input from the user, x,and converts it into an integer 
    It is then squared and giving a value, y, which is printed

    """
    x = int(input("Enter a number: "))
    y = x ** 2
    print (y)

square() 

# Challenge 2 
def printer():
    """
    Takes input from the user, x, and prints it
    """
    x = input("Anything you wanna say?\n")
    print(x)
    
printer()

# Challenge 3
def addsub(x, y, z, a = 0, b = 0):
    """
    :param x, y, z, a, b: integers
    Adds together x, y, and z, and prints the result
    Subtracts b from a and prints the result

    """
    add = x + y + z
    sub = a - b 
    print(x, "+", y, "+", z, "=", add)
    print(a, "-", b, "=", sub)
print(addsub(1, 2, 3, 3, 6))

# Challenge 4
def div2(x):
    """
    :param x: integer
    Divids x by 2
    """
    return x / 2
def multi4(y):
    """
    :param y: integer
    Multiplies y by 4
    """
    return y * 4
x = div2(2)
print(multi4(x))

# Challenge 5 
def converter():
    """
    Takes input from the user, x, and converts it to a float, then prints it
    Raises an exception if anything other than a number is inputted
    """
    try:
        x = input("Number you want converted to a float: ")
        x = float(x)
        print(x)
    except ValueError:
        print("Not a valid number")
converter()
# Challenge 6, add docstrings to all functions
