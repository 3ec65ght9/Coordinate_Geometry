def int_check(question):

    while True:

        try:
            response = float(input(question))
            return response

        except ValueError:
            print( f"Please enter a number")




def midpoint(x1, y1, x2, y2):


    # calculate midpoint
    mid_x = (x1 + x2) / 2
    mid_y = (y1 + y2) / 2
    return mid_x, mid_y


print()

# ask user for first point
x_1 = float(input("x1-A: "))

# Ask user for second point
y_1 = float(input("y1-B: "))

# ask user for third point
x_2 = float(input("x2-D: "))

# Ask user for fourth point
y_2 = float(input("y2-C: "))

midpoint_coordinates = midpoint(x_1, y_1, x_2, y_2)

print(f"the midpoint is: {midpoint_coordinates}")