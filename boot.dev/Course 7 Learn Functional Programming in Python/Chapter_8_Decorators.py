#lesson 1
def file_type_aggregator(func_to_decorate):
    # dict of file_type -> count
    counts = {}

    def wrapper(doc, file_type):
        if file_type not in counts:
            counts[file_type] = 0
        counts[file_type] += 1
        result = func_to_decorate(doc, file_type)

        return result, counts

    return wrapper

# don't touch above this line

@file_type_aggregator
def process_doc(doc, file_type):
    return f"Processing doc: '{doc}'. File Type: {file_type}"

#lesson 2
def args_logger(*args, **kwargs):
    i = 1
    for arg in args:
        print(f"{i}. {arg}")
        i += 1
    for karg in sorted(kwargs):
        print(f"* {karg}: {kwargs[karg]}")

#lesson 3
def configure_plugin_decorator(func):
    def wrapper(*args):
        dictionary = dict(args)
        return func(**dictionary)
    return wrapper

#lesson 4
def markdown_to_text_decorator(func):
    def wrapper(*args, **kwargs):
        converted_args = list(map(convert_md_to_txt, args))
        def kwarg_item_to_txt(item_tuple):
            key, value = item_tuple
            return (key, convert_md_to_txt(value))
        converted_kwargs = dict(map(kwarg_item_to_txt, kwargs.items()))
        return func(*converted_args, **converted_kwargs)
    return wrapper

# don't touch below this line

def convert_md_to_txt(doc):
    lines = doc.split("\n")
    for i in range(len(lines)):
        line = lines[i]
        lines[i] = line.lstrip("# ")
    return "\n".join(lines)

#lesson 7
from functools import lru_cache

@lru_cache()
def is_palindrome(word):
    if len(word) < 2:
        return True
    if word[0] == word[-1]:
        return is_palindrome(word[1:-1])
    return False

#lesson 8
def replacer(old, new):
    def replace(decorated_func):
        def wrapper(text):
            return decorated_func(text.replace(old,new))
        return wrapper
    return replace

@replacer("&", "&amp;")
@replacer("<", "&lt;")
@replacer(">", "&gt;")
@replacer('"', "&quot;")
@replacer("'", "&#x27;")
def tag_pre(text):
    return f"<pre>{text}</pre>"