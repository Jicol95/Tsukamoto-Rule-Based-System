def rule_fire(fuzzified_crisp_values,rule_base):

    rule_fire = []
    answers = []

    for rule in rule_base:
        counter = 0
        instances_of_and = rule.count("and")
        for entry in fuzzified_crisp_values:
            for tuple in fuzzified_crisp_values[entry]:
                if (entry + " is " + tuple[0]) in rule and tuple[1] > 0 and instances_of_and >= 1 and rule not in rule_fire:
                    counter +=1
                    if counter == (instances_of_and + 1):
                        rule_fire.append(rule)

    for rule in rule_base:
        instances_of_or = rule.count(" or ")
        for entry in fuzzified_crisp_values:
            for tuple in fuzzified_crisp_values[entry]:
                if (entry + " is " + tuple[0]) in rule and tuple[1] > 0 and instances_of_or >= 1 and rule not in rule_fire:
                    rule_fire.append(rule)

    for rule in rule_fire:

        antecedent_name = rule.split(" ")
        antecedent_name = antecedent_name[-4] + " " + antecedent_name[-1]

        and_values = []
        or_values = []

        for name in fuzzified_crisp_values:

            if "and" in rule and name in rule:

                for tuple in fuzzified_crisp_values[name]:

                    if tuple[1] > 0 and tuple[0] in rule:
                        and_values.append(tuple[1])
        try:
            maximum = min(and_values)
            answers.append((antecedent_name, maximum))

        except:
            pass

        for name in fuzzified_crisp_values:
            if " or " in rule and name in rule:

                for tuple in fuzzified_crisp_values[name]:

                    if tuple[1] > 0 and tuple[0] in rule:
                        or_values.append(tuple[1])

        try:
            minimum = max(or_values)
            answers.append((antecedent_name, minimum))
        except:
            pass

    answers_and_fired_rules = [answers, rule_fire]
    return answers_and_fired_rules

def membership_to_crisp_value(weighted_avarage_variables, membership_functions):

    answer = []


    for consequent_values in weighted_avarage_variables:

        member_of = consequent_values[0].split(" ")[0]
        membership = consequent_values[0].split(" ")[1]
        value = float(consequent_values[1])

        for four_tuple in membership_functions[member_of]:
            if four_tuple["name"] == membership:
                function = four_tuple["value"]
                comparison = 0
                i = 0
                while comparison < value:
                    a = int(function[0])
                    b = int(function[1])
                    alpha = int(function[2])
                    beta = int(function[3])

                    if (i in range(a-alpha, a)):
                        comparison = float((value - a + alpha) / alpha)
                    elif (i in range(a,b)):
                        comparison = 1
                    elif (i in range(b, b+beta)):
                        comparison = float((b + beta - value) / beta)

                    i += 1

                answer.append(i)

    return  answer

