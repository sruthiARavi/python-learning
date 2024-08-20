def format_name(f_name, l_name):
    # doc string
    """Take a first and last name and format it
    to return in Title case format"""

    def check_if_valid_input(name1, name2):
        # You can define function within function
        if name1 == "" or name2 == "":
            # return "You did not provide valid input(s)"
            return False
        else:
            return True

    if not check_if_valid_input(f_name, l_name):
        return "You did not provide valid input(s)"
    f_name = f_name.title()  # turn to camel case
    l_name = l_name.title()
    # print(f_name + " " + l_name)
    return f"{f_name} {l_name}"


output = format_name("ABcd", "efggH")
print(output)
print(format_name("", "name"))
