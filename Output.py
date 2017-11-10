

# Prints welcome information to the user
def welcome(input_data, rb_name):

    # Giver user feedback that system has accepted the file name and is begining to parse it
    print "\n\nParsing " + input_data + "..."

    # Print the name of the rule base and all the rules underneath
    print("\n" + rb_name + " loaded!\n")

# Prints the answer to the user
def crisp_output(crisp_value, fired_rules):

    print("The following rules fired:\n")

    # Print each fired rule
    for rule in fired_rules:
        print rule

    # Get the set to which the crisp value belongs
    consequence_name = fired_rules[0].split(" ")[-4]

    print("\nRESULT\n\n" + consequence_name + " = " + str(crisp_value) +"\n")