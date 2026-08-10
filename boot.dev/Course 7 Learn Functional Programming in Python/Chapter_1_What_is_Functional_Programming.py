#lesson 1
def stylize_title(document):
    return add_border(center_title(document))

# Don't touch below this line

def center_title(document):
    width = 40
    title = document.split("\n")[0]
    centered_title = title.center(width)
    return document.replace(title, centered_title)

def add_border(document):
    title = document.split("\n")[0]
    border = "*" * len(title)
    return document.replace(title, title + "\n" + border)

#lesson 3
def add_prefix(document, documents):
    return documents + (f"{len(documents)}. " + document,)

#lesson 6
def get_median_font_size(font_sizes):
    list_length = len(font_sizes)
    if list_length > 0:
        sorted_list = sorted(font_sizes)
        return sorted_list[(list_length-1)//2]
    return None

#lesson 9
def format_line(line):
    stripped = line.strip()
    capitalized = stripped.upper()
    rm_punc = capitalized.replace(".", "")
    suffixed = f"{rm_punc}..."
    return suffixed

#lesson 13
def choose_parser(file_extension):
    #if file_extension.lower() in ("markdown", "md"):
    #    return "markdown"
    #else:
    #    return "plaintext"
    return "markdown" if file_extension.lower() in ("markdown", "md") else "plaintext"

#lesson 14
def hex_to_rgb(hex_color):
    if is_hexadecimal(hex_color) and len(hex_color) == 6:
        r = int(hex_color[:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:], 16)
        return r, g, b
    raise Exception("not a hex color string")

# Don't edit below this line

def is_hexadecimal(hex_string):
    try:
        int(hex_string, 16)
        return True
    except Exception:
        return False