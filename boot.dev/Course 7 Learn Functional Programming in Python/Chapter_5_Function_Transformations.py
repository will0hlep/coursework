#lesson 1
def get_logger(formatter):
    logger = lambda first, second: print(formatter(first, second))
    return logger

# Don't edit below this line

def test(first, errors, formatter):
    print("Logs:")
    logger = get_logger(formatter)
    for err in errors:
        logger(first, err)
    print("====================================")

def colon_delimit(first, second):
    return f"{first}: {second}"

def dash_delimit(first, second):
    return f"{first} - {second}"

def main():
    db_errors = [
        "out of memory",
        "cpu is pegged",
        "networking issue",
        "invalid syntax",
    ]
    test("Doc2Doc FATAL", db_errors, colon_delimit)

    mail_errors = [
        "email too large",
        "non alphanumeric symbols found",
    ]
    test("Doc2Doc WARNING", mail_errors, dash_delimit)

main()

#lesson 4
def doc_format_checker_and_converter(conversion_function, valid_formats):
    def inner_func(filename, content):
        if filename.split('.')[-1] in valid_formats:
            return conversion_function(content)
        raise ValueError ('invalid file format')
    return inner_func

# Don't edit below this line

def capitalize_content(content):
    return content.upper()

def reverse_content(content):
    return content[::-1]

#lesson 7
def get_filter_cmd(filter_one, filter_two):
    def filter_cmd(content, option = '--one'):
        if option == '--one':
            return filter_one(content)
        if option == '--two':
            return filter_two(content)
        if option == '--three':
            return filter_two(filter_one(content))
        raise Exception('invalid option')
    return filter_cmd

# don't touch below this line

def replace_bad(text):
    return text.replace("bad", "good")

def replace_ellipsis(text):
    return text.replace("..", "...")

def fix_ellipsis(text):
    return text.replace("....", "...")