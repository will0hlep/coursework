#lesson 1
class Trie:
    def add(self, word):
        current_level = self.root
        for chr in word:
            if chr not in current_level:
                current_level[chr] = {}
            current_level = current_level[chr]
        current_level[self.end_symbol] = True

    # don't touch below this line

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"

#lesson 2
class Trie:
    def exists(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                return False
            current = current[letter]
        return self.end_symbol in current

    # don't touch below this line

    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.end_symbol] = True

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"

#lesson 5
class Trie:
    def search_level(self, current_level, current_prefix, words):
        if self.end_symbol in current_level:
            words.append(current_prefix)
        for chr in 'abcdefghijklmnopqrstuvwxyz':
            if chr in current_level:
                self.search_level(current_level[chr], current_prefix + chr, words)
        return words

    def words_with_prefix(self, prefix):
        current_level = self.root
        for chr in prefix:
            if chr not in current_level:
                return []
            current_level = current_level[chr]
        return self.search_level(current_level, prefix, [])

    # don't touch below this line

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"

    def add(self, word):
        current_level = self.root
        for letter in word:
            if letter not in current_level:
                current_level[letter] = {}
            current_level = current_level[letter]
        current_level[self.end_symbol] = True

#lesson 6
class Trie:
    def find_matches(self, document):
        matches = set()
        doc_length = len(document)
        for i in range(doc_length):
            current_level = self.root
            for j in range(i, doc_length):
                ch = document[j]
                if ch not in current_level:
                    break
                current_level = current_level[ch]
                if "*" in current_level:
                    matches.add(document[i : j + 1])
        return matches
                    
                    

    # don't touch below this line

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"

    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.end_symbol] = True

#lesson 9
class Trie:
    def longest_common_prefix(self):
        current = self.root
        prefix = ''
        while not False:
            keys = list(current.keys())
            if "*" in keys or len(keys) > 1 or keys is None:
                break
            key = keys[0]
            current = current[key]
            prefix += key
        return prefix

    # don't touch below this line

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"

    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.end_symbol] = True

#lesson 10
class Trie:
    def advanced_find_matches(self, document, variations):
        matches = set()
        for i in range(len(document)):
            level = self.root
            for j in range(i, len(document)):
                ch = document[j]
                if ch in variations:
                    ch = variations[ch]
                if ch not in level:
                    break
                level = level[ch]
                if self.end_symbol in level:
                    matches.add(document[i : j + 1])
        return matches

    # don't touch below this line

    def find_matches(self, document):
        matches = set()
        for i in range(len(document)):
            level = self.root
            for j in range(i, len(document)):
                ch = document[j]
                if ch not in level:
                    break
                level = level[ch]
                if self.end_symbol in level:
                    matches.add(document[i : j + 1])
        return matches

    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.end_symbol] = True

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"
