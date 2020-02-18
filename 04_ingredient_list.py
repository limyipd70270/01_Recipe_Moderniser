# Ingredients List


# Not blank Function goes here
def not_blank(question, error_msg, num_ok):
    error = error_msg

    valid = False
    while not valid:
        response = input(question)
        has_errors = ""

        if num_ok != "yes":
            # look at each character in string and if it's a number, complain
            for letter in response:
                 if letter.isdigit() == True:
                     has_errors = "yes"
                     break

        if response == "":
            print(error)
        elif has_errors !="":
            print(error)
            continue
        else:
            return response



# Main Routine...

# Set up empty ingredient list

# Look to ask users to enter an ingredient

# Ask user for ingredient (via not blank function)

# If exit code is typed...

# Check that list contains at least two items

# If list contains at least two items break out of loop

# If exit code is not entered, add ingredient to lst

# Output list
