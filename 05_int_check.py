def int_check(question):

    while True:

        try:
            response = float(input(question))
            return response

        except ValueError:
            print( f"Please enter a number")
