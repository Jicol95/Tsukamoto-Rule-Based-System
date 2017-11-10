import PyParse
import Output
import Input
import PyFuzz
import PyInfer


# main() interact with all the functions needed for a fuzzy rule base system, responsible for piping through functions
# arguments and assigning return values to variables. It is also used to handle I/O

def main():
    # Checks that the file exists in the same directory
    input_data = Input.sanitize()

    # txt_parsed is a dictionary type which is horrifically nested so be careful! Has the structured version of txt file
    txt_parsed = PyParse.parse(input_data)

    # Making variables which break the dictionary down into sub-sets
    membership_functions = txt_parsed["membership_functions"]
    rb_name = txt_parsed["rb_name"]
    rule_base = txt_parsed["rule_base"]
    crisp_values = txt_parsed["crisp_data"]

    # Prints the txt file in a user readable way to confirm that the text has been parsed
    Output.welcome(input_data, rb_name)

    # Returns the fuzzy reprsentation of the crisp values as an array
    fuzzified_crisp_values = PyFuzz.fuzzify(crisp_values, membership_functions)

    # Takes the fuzzy_values, rule_base and crisp values and returns the rules that fired and the
    # set, membership_function and membership value of the consequence value
    weighted_average_variables_and_fired_rules = PyInfer.rule_fire(fuzzified_crisp_values, rule_base)

    # Unpack the array returned by PyInfer.rule_fire() also performes the logical operators
    weighted_avarage_variables = weighted_average_variables_and_fired_rules[0]
    fired_rules = weighted_average_variables_and_fired_rules[1]

    # Returns the crisp value corresponding to the membership value of the consequence of a fired rule
    memberships_as_crisp_values = PyInfer.membership_to_crisp_value(weighted_avarage_variables, membership_functions)

    # Deffuzification using weighted average (see: Tsukamoto)
    crisp_output = PyFuzz.defuzzify(memberships_as_crisp_values, weighted_avarage_variables)

    # Returns the answer with some formatting
    Output.crisp_output(crisp_output, fired_rules)


if __name__ == '__main__':
    main()
