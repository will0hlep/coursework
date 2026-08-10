#lesson 1
def converted_font_size(font_size):
    def inner_converted_font_size(doc_type):
        if doc_type == "txt":
            return font_size
        if doc_type == "md":
            return font_size * 2
        if doc_type == "docx":
            return font_size * 3
        raise ValueError("invalid doc type")
    return inner_converted_font_size

#lesson 2
def lines_with_sequence(char):
    def with_char(length):
        sequence = char * length
        def with_length(doc):
            count = 0
            for line in doc.split():
                if sequence in line:
                    count += 1
            return count
        return with_length
    return with_char

#lesson 5
def create_markdown_image(alt_text):
    image_syntax__ = '![' + alt_text + ']'
    def inner_func(url):
        url = url.replace('(','%28')
        url = url.replace(')','%29')
        url = '(' + url + ')'
        image_syntax_ = image_syntax__ + url
        def innermost_func(title = None):
            image_syntax = image_syntax_
            if title != None:
                image_syntax = image_syntax[:-1] + ' "' + title + '")'
            return image_syntax
        return innermost_func
    return inner_func

#lesson 6
def new_resizer(max_width, max_height):
    def inner_func(min_width = 0, min_height = 0):
        if min_width > max_width or min_height > max_height:
            raise Exception("minimum size cannot exceed maximum size")
        def innermost_func(width, height):
            width = max(min(width, max_width), min_width)
            height = max(min(height, max_height), min_height)
            return width, height
        return innermost_func
    return inner_func