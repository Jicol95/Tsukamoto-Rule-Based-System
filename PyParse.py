import re

def parse(txt):

    # Open file with named defined by function arg
    txt_extracted = open(txt, 'r')

    # List the whole file, each entry divided by double newline
    txt_listed = re.split(r'\n\n', txt_extracted.read())

    # For every example the rule base name will be the first element of the list
    rb_name = txt_listed[0]

    # The rules wil follow
    rules = txt_listed [1]

    # Real world values will be the last section so is dependant on no of rules etc
    crisp_data = txt_listed[len(txt_listed)-1]

    # Create empty dictionary to store membership functions
    membership_functions = {}

    # Create empty dictionary to contain rb_name, rules, crisp_data and nested dictionary membership_functions
    txt_parsed = {}

    # Iterate through text list begining at [2] unit -1 the length with a step of 2 each iter
    for i in range(2, len(txt_listed)-1,2):

        #empty list to contain membership functions
        functions = []

        #group the functions by section
        function_grouped_by_name = txt_listed[i+1].split("\n")

        #print function_grouped_by_name

        #Iterate through the length of the grouped functions until the end of the grouping
        for j in range(0, len(function_grouped_by_name)):

            # Declare list value and assign it the name of each funtion and the four-touple values
            value = function_grouped_by_name[j].split(" ")

            #Declare key which is a dictionary containing the set name and four-touple value of that name as a list
            key = {"name" : value[0], "value" : [value[1],value[2],value[3],value[4]]}

            #add each dictionary entry to the list functions
            functions.append(key)


        membership_functions[txt_listed[i].strip()] = functions


    # Convert crisp data to list using \n a delimiter
    crisp_data = crisp_data.split("\n")


    crisp = []

    for i in range(0,len(crisp_data)):

        # Declare x and turn crisp_data into a list using = as delimiter
        x = crisp_data[i].split(" = ")

        # If there is still a member of x
        if x is not None:

            # append a dictionary of with the name as the name if the crisp_value and the value as the crisp value
            crisp.append({"name" : x[0], "value":x[1]})

    # Add named sections to dictionary using the variables as the values
    txt_parsed['rb_name'] = rb_name
    txt_parsed['membership_functions'] = membership_functions
    txt_parsed['rule_base'] = rules.split("\n")
    txt_parsed['crisp_data'] = crisp

    #return the dictionary
    return txt_parsed




