import re

def read_template(file):
    """This function takes in a path to text file and returns
    a stripped string of the file’s contents."""
    try:
        with open(file, 'r') as f:
            template = f.read()
            return template
    except FileNotFoundError:
        raise FileNotFoundError

template_file = read_template('assets/template.txt')


def parse_template(text):
    """This function takes a template test and return two values.
    and return two values one the template without argument between {} and the second for the arguments"""
    pattern = "[^{\}]+.(?=})"
    stripped = re.sub(pattern, "", text)
    test = re.findall(pattern, text)
    parts= ()
    for item in test:
        parts += (item,)
    return  (stripped, parts)

def merge(stripped, parts):
    """This function takes two values. a template and tuple and return one string filled with the elements of tuple"""
    result = stripped
    for item in parts:
       result= result.replace("{}", f"{item}", 1)
    return result

def print_prompts():
    user_inputs = []
    striped, parts = parse_template(template_file)
    for element in parts:
        user_input = input(f'Enter {element}: ')
        user_inputs += (user_input,)
    return user_inputs

def handle_inputs():

    msg = """
    \n***************************************\n
    ****      Welcome to Madib Game      ****
    \n
    \n 
    Madlibs is a template word game\n 
    where user(you) need to input different\n 
    words in command line. and you will get\n 
    a story that was created\n 
    using your words entered.\n \n
    Please type 'y' to play:\n"""

    if input(msg).lower() == "y":
        user_inputs = print_prompts()
        stripped, parts = parse_template(template_file)
        formatted_template = merge(stripped, user_inputs)
        print(formatted_template)
        return formatted_template


def write_file(file, contents):
    with open(file, 'w') as f:
        template = (f.write(contents))

write_file('assets/result.txt', handle_inputs())