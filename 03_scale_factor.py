# To

# Ask user for servings made by recipe (and check this is a number that is more than 1)
# Ask user for servings desired (check this is a number)
# Calculate the scale factor
# Warn the user if the sf is less than 0.25 or more than 4

# Functions go here

# Number Checking Function
def num_check(question):

    error = "Please enter a number that is more than zero"

    valid = False
    while not valid:
        try:
            response = float(input(question))
                print
            if response <= 0:

            return response

        except ValueError:
            print(error)

        if response == "":
            continue
        elif has_errors !="":
            print(error)
            continue
        else:
            return response


# Main Routine goes here

serving_size = num_check("What is the recipe serving size? ")
desired_size = num_check("How many servings are needed? ")

scale_factor = desired_size / serving_size

print("Scale Factor: {}".format(scale_factor))