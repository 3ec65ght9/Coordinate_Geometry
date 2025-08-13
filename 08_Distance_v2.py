import math

def int_check(question):

    while True:

        try:
            response = float(input(question))
            return response

        except ValueError:
            print( f"Please enter a number")


def distance(x1, y1, x2, y2):

    distance_d =  math.sqrt((x2 - x1)**2) + math.sqrt((y2 - y1)**2)
    return distance_d


print()

# ask user for first point
x_1 = float(input("x1-A: "))

# Ask user for second point
y_1 = float(input("y1-B: "))

# ask user for third point
x_2 = float(input("x2-D: "))

# Ask user for fourth point
y_2 = float(input("y2-C: "))

distance_coordinates = distance(y_2, y_1, x_2, x_1)
print(f"The gradient is: {distance_coordinates}")
