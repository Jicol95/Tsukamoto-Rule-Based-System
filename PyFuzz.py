import numpy


def fuzzify(crisp_values, membership_functions):
    # This dictionary will contain the fuzzified values paired with the function name
    big_picture = {}

    # loop from 0 to the length of crisp values
    for i in range(0, len(crisp_values)):

        # Get the name of crisp value journey_time etc
        delimiter = crisp_values[i]["name"]

        # For each type of crisp value
        if delimiter in membership_functions:

            # Get the value of each crisp value type
            value = float(crisp_values[i]["value"])

            # Instantiate an array to contain membership touples
            memberships = []

            i = -1

            for dictionaries in membership_functions[delimiter]:

                # Assign values to each entry in the 4-tuple membership function
                a = int(dictionaries["value"][0])
                b = int(dictionaries["value"][1])
                alpha = int(dictionaries["value"][2])
                beta = int(dictionaries["value"][3])

                # If value is outwith the bounds of the set membership is 0
                if (value < (a - alpha)):
                    memberships.append((dictionaries["name"], 0))

                # If value is in the first triangle of the trapezoid then append membership calculated with trig
                elif (value in range(a - alpha, a)):
                    memberships.append((dictionaries["name"], round(float((value - a + alpha) / alpha), 2)))

                # If value is in rectangle/square of the trapezoid then membership = 1
                elif (value in range(a, b)):
                    memberships.append((dictionaries["name"], 1))

                elif (value == b):
                    memberships.append((dictionaries["name"], 1))

                # If value is in the second triangle of the trapezoid then append membership calculated with trig
                elif (value in range(b, b + beta)):
                    memberships.append((dictionaries["name"], round(float((b + beta - value) / beta), 2)))

                elif (value == b + beta):
                    memberships.append((dictionaries["name"], round(float((b + beta - value) / beta), 2)))

                # If value is outwith the bounds of the set membership is 0
                elif (value > (b + beta)):
                    memberships.append((dictionaries["name"], 0))

                i += 1

                if i == (len(dictionaries)):
                    memberships_done = memberships
                    big_picture[delimiter] = memberships_done
    return big_picture


# arg1 = [{'name': 'journey_time'}]
# answer = fuzzify()
# print fuzzify()


def defuzzify(answers, weighted_averages):
    print answers
    print weighted_averages
    # Convert each value in list to float
    for i in range(len(weighted_averages)):
        weighted_averages[i] = float(weighted_averages[i][1])

    # Convert each value in list to float
    for i in range(len(answers)):
        answers[i] = float(answers[i])

    # Construct the numerator of the weighted average equation
    numerator = sum(numpy.multiply(weighted_averages, answers))

    # Construct the denomenator of the weighted average equation
    denomenator = sum(weighted_averages)

    # Calulate the crisp output
    crisp_output = numerator / denomenator

    return crisp_output
