def int_check(question):

    while True:

        try:
            response = float(input(question))
            return response

        except ValueError:
            print( f"Please enter a number")



print()

# ask user for first point
x_1 = float(input("x1-A: "))

# Ask user for second point
y_1 = float(input("y1-B: "))

# ask user for third point
x_2 = float(input("x2-D: "))

# Ask user for fourth point
y_2 = float(input("y2-C: "))
