#lesson 1
valid_extensions = ["docx", "pdf", "txt", "pptx", "ppt", "md"]
valid_conversions = {
    "docx": ["pdf", "txt", "md"],
    "pdf": ["docx", "txt", "md"],
    "txt": ["docx", "pdf", "md"],
    "pptx": ["ppt", "pdf"],
    "ppt": ["pptx", "pdf"],
    "md": ["docx", "pdf", "txt"],
}

def convert_file_format(filename, target_format):
    valid_extensions = ["docx", "pdf", "txt", "pptx", "ppt", "md"]
    valid_conversions = {
        "docx": ["pdf", "txt", "md"],
        "pdf": ["docx", "txt", "md"],
        "txt": ["docx", "pdf", "md"],
        "pptx": ["ppt", "pdf"],
        "ppt": ["pptx", "pdf"],
        "md": ["docx", "pdf", "txt"],
    }
    current_format = filename.split(".")[-1]
    if (
        current_format in valid_extensions
        and target_format in valid_conversions[current_format]
    ):
        return filename.replace(current_format, target_format)
    return None

#lesson 5
def add_format(default_formats, new_format):
    updated_formats = default_formats.copy()
    updated_formats[new_format] = True
    return updated_formats

def remove_format(default_formats, old_format):
    updated_formats = default_formats.copy()
    updated_formats[old_format] = False
    return updated_formats

#lesson 8
def convert_case(text, target_format):
    if not text or not target_format:
        raise ValueError(f"no text or target format provided")
    if target_format == "uppercase":
        return text.upper()
    if target_format == "lowercase":
        return text.lower()
    if target_format == "titlecase":
        return text.title()
    raise ValueError(f"unsupported format: {target_format}")

#lesson 11
doc = """I *love* Markdown.
I **really love** Markdown.
I ***really really love*** Markdown."""

def remove_emphasis(doc):
    lines = doc.split("\n")
    new_lines = map(remove_line_emphasis, lines)
    return "\n".join(new_lines)

# Don't touch below this line

def remove_line_emphasis(line):
    words = line.split()
    new_words = map(remove_word_emphasis, words)
    return " ".join(new_words)

def remove_word_emphasis(word):
    return word.strip("*")

#lesson 12
def word_count_memo(document, memos):
    new_memos = memos.copy()
    if document not in new_memos:
        new_memos[document] = word_count(document)
    return new_memos[document], new_memos

# Don't edit below this line

def word_count(document):
    count = len(document.split())
    return count

#lesson 15
default_commands = {}
default_formats = ["txt", "md", "html"]
saved_documents = {}

# Don't edit above this line

def add_custom_command(commands, new_command, function):
    new_commands = commands.copy()
    new_commands[new_command] = function
    return commands.copy()

def add_format(formats, format):
    new_formats = formats.copy()
    new_formats.append(format)
    return new_formats

def save_document(docs, file_name, doc):
    new_docs = docs.copy()
    new_docs[file_name] = doc
    return new_docs

def add_line_break(line):
    return line + "\n\n"

#lesson 16
def sort_dates(dates):
    date_list = dates.copy()
    sorted_dates = sorted(date_list, key = lambda x: x[6:] + x[:2] + x[3:5])
    return sorted_dates