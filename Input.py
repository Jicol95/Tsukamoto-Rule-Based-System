import PyParse


def sanitize():
    while True:
        try:
            # Ask user for name of file to be parsed
            input_data = raw_input("Enter filename :")

            # test to see if the file exists
            txt_parsed = PyParse.parse(input_data)

        except:
            print("\n WARNING!: File not found, make sure file is in the same directory as main.py.\n")
            continue
        else:
            break

    return input_data
