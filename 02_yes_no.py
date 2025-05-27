def yes_no(Question):

    while True:
        response=input(Question).lower()
        if response == "yes" or response == "y":
            return "yes"
        if response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes (y) or no (n) . \n")

while True:
    want_instructions=yes_no("Do you want instructions? ")
    print(f"You picked {want_instructions}\n")
