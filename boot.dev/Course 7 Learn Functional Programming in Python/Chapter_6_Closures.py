#lesson 1
def word_count_aggregator():
    count = 0
    def inner_func(words):
        nonlocal count
        count += len(words.split())
        return count
    return inner_func

#lesson 4
def new_collection(initial_docs):
    copy_of_initial_docs = initial_docs.copy()
    def inner_func(string):
        copy_of_initial_docs.append(string)
        return copy_of_initial_docs
    return inner_func

#lesson 5
import copy

def css_styles(initial_styles):
    styles = copy.deepcopy(initial_styles)
    def add_style(selector, property, value):
        if selector not in styles:
            styles[selector] = {}
        styles[selector][property] = value
        return styles
    return add_style