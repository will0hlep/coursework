#lesson 1
def factorial_r(x):
    if x == 0:
        return 1
    return x * factorial_r(x - 1)

#lesson 4
def zipmap(keys, values):
    if keys == [] or values == []:
        return {}
    dictionary_to_be_returned = zipmap(keys[1:], values[1:])
    dictionary_to_be_returned[keys[0]] = values[0]
    return dictionary_to_be_returned

#lesson 8
def sum_nested_list(lst):
    total = 0
    for element in lst:
        if isinstance(element, list):
            total += sum_nested_list(element)
        else:
            total += element
    return total

#lesson 12
def list_files(parent_directory, current_filepath=""):
    filepaths = []
    for i in parent_directory:
        new_filepath = current_filepath + '/' + i
        if parent_directory[i] == None:
            filepaths.append(new_filepath)
        else:
            filepaths.extend(list_files(parent_directory[i], new_filepath))
    return filepaths

#lesson 14
def find_longest_word(document, longest_word=""):
    seperated_document = document.split(' ',maxsplit=1)
    if document == "" or document.strip(" ") == "":
        return longest_word
    if len(longest_word) < len(seperated_document[0]):
        longest_word = seperated_document[0]
    if len(seperated_document) > 1:
        longest_word = find_longest_word(seperated_document[1], longest_word)
    return longest_word

#lesson 15
def count_nested_levels(nested_documents, target_document_id, level=1):
    for document_id in nested_documents:
        if document_id == target_document_id:
            return level
        deep_level = count_nested_levels(nested_documents[document_id], target_document_id, level + 1)
        if deep_level != -1:
            return deep_level
    return -1