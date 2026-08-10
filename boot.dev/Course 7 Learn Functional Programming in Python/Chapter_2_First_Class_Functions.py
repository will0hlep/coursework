#lesson 1
def file_to_prompt(file, to_string):
    prompt = to_string(file)
    return f"```\n{prompt}\n```"

#lesson 2
def file_type_getter(file_extension_tuples):
    extension_to_type = {}
    for i in range(len(file_extension_tuples)):
        for j in file_extension_tuples[i][1]:
            extension_to_type[j] = file_extension_tuples[i][0]
    return lambda name: extension_to_type.get(name, "Unknown")

#lesson 5
def change_bullet_style(document):
    lines = document.split("\n")
    return "\n".join(map(convert_line, lines))

# Don't edit below this line

def convert_line(line):
    old_bullet = "-"
    new_bullet = "*"
    if len(line) > 0 and line[0] == old_bullet:
        return new_bullet + line[1:]
    return line

#lesson 6
def remove_invalid_lines(document):
    lines = document.split("\n")
    filtered = filter(lambda x: not x.startswith("-"), lines)
    rejoined = "\n".join(filtered)
    return rejoined

#lesson 7
import functools

def join(doc_so_far, sentence):
    return doc_so_far + ". " + sentence

def join_first_sentences(sentences, n):
    if n == 0:
        return ""
    return functools.reduce(join, sentences[:n])+"."

#lesson 10
valid_formats = [
    "docx",
    "pdf",
    "txt",
    "pptx",
    "ppt",
    "md",
]

# Don't edit above this line

def pair_document_with_format(doc_names, doc_formats):
    zipped_list = list(zip(doc_names, doc_formats))
    filtered_list = list(filter(lambda x: x[1] in valid_formats, zipped_list))
    return filtered_list

#lesson 11
def restore_documents(originals, backups):
    combined_list = originals + backups
    upper_case_list = map(lambda x: x.upper(), combined_list)
    filtered_set = filter(lambda x: not x.isdigit(), upper_case_list)
    return set(filtered_set)