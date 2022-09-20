def format_name(f_name, l_name):
    """Take a first and last name and format it"""
    # docstring can describe you function what they do
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    # asta o sa returneze None in consola daca nu introducem un first name sau last name
    formated_f_name = (f_name.title())
    formated_l_name = (l_name.title())
    # print(f'{formated_f_name} {formated_l_name}')
    return f'{formated_f_name} {formated_l_name}'
    #nu se executa nimic dupa return
# formated_string = format_name("ADRIAN", "MaCovei")
formated_string = format_name(input("What is your first name?\n"), input("What is your last name?\n"))
print(formated_string)
format_name()