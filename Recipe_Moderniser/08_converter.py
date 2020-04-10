# Conversion Function...


# ***** Functions go here ******
def general_converter(how_much, lookup, dictionary, conversion_factor):

    if lookup in dictionary:
        mult_by = dictionary.get(unit)
        how_much = how_much * mult_by * conversion_factor

    return how_much

def unit_checker():

    unit_tocheck = input ("Unit? ")

    # Abbreviation lists
    teaspoon = ["tsp", "teaspoon", "t"]
    tablespoon = ["tbs", "tablespoon", "T", "tbsp"]
    ounce = ["oz", "ounce", "fl oz"]
    cup = ["c"]
    pint = ["p", "pt", "fl pt"]
    quart = ["q", "qt", "fl qt"]
    mls = ["ml", "millilitre", "milliliter"]
    litre = ["litre", "liter", "l"]
    pound = ["pound", "lb", "#"]

    if unit_tocheck == "":
        print("you chose {}". format(unit_tocheck))
        return unit_tocheck

    elif unit_tocheck == "T" or unit_tocheck.lower() in tablespoon:
        return "tbs"
    elif unit_tocheck.lower() in teaspoon:
        return  "tsp"

# ****** Main Routine Goes here *******
unit_central = {
    "tsp": 5,
    "tbs": 15,
    "cup": 237,
    "ounce": 30,
    "pint": 473,
    "quart": 946,
    "pound": 454
}

keep_going = ""
while keep_going == "":
    amount = eval(input("How much? "))
    amount = float(amount)

    # Get unit and change it to match dictionary.
    unit = unit_checker()

    amount = general_converter(amount, unit, unit_central, 1)
    print(amount)

    if unit in unit_central:
        mult_by = unit_central.get(unit)
        amount = amount * mult_by
        print("Amount is {:.2f} mls".format(amount))
    else:
        print("{} is unchanged".format(amount))

    keep_going = input("press <enter> to continue or 'q' to quit ")