#lesson 4
class HashMap:
    def key_to_index(self, key):
        hash = 0
        for i in key:
            hash += ord(i)
        return hash % self.size

    # don't touch below this line

    def __init__(self, size):
        self.size = size
        self.hashmap = [None for i in range(self.size)]

    def __repr__(self):
        buckets = []
        for v in self.hashmap:
            if v != None:
                buckets.append(v)
        return str(buckets)

#lesson 5
class HashMap:
    def insert(self, key, value):
        self.hashmap[self.key_to_index(key)] = (key, value)

    # don't touch below this line

    def __init__(self, size):
        self.size = size
        self.hashmap = [None for i in range(size)]

    def key_to_index(self, key):
        sum = 0
        for c in key:
            sum += ord(c)
        return sum % self.size

    def __repr__(self):
        final = ""
        for i, v in enumerate(self.hashmap):
            if v != None:
                final += f" - {i}: {str(v)}\n"
            else:
                final += f" - {i}: None\n"
        return final

#lesson 6
class HashMap:
    def get(self, key):
        if self.hashmap[self.key_to_index(key)]:
            return self.hashmap[i][1]
        raise Exception("sorry, key not found")

    # don't touch below this line

    def __init__(self, size):
        self.hashmap = [None for i in range(size)]

    def key_to_index(self, key):
        sum = 0
        for c in key:
            sum += ord(c)
        return sum % len(self.hashmap)

    def insert(self, key, value):
        i = self.key_to_index(key)
        self.hashmap[i] = (key, value)

    def __repr__(self):
        final = ""
        for i, v in enumerate(self.hashmap):
            if v != None:
                final += f" - {str(v)}\n"
        return final

#lesson 9
class HashMap:
    def insert(self, key, value):
        self.resize()
        index = self.key_to_index(key)
        if self.hashmap[index] is None:
            self.filled_buckets += 1
        self.hashmap[index] = (key, value)

    def resize(self):
        if self.current_load() >= 0.05:
            tmp = self.hashmap
            self.size = 1 if self.size == 0 else 10 * self.size
            self.hashmap = [None for i in range(self.size)]
            for pair in tmp:
                if pair != None:
                    index = self.key_to_index(pair[0])
                    self.hashmap[index] = (pair[0], pair[1])

    def current_load(self):
        if self.filled_buckets == 0:
            return 1
        return self.filled_buckets/self.size

    # don't touch below this line

    def __init__(self, size):
        self.size = size
        self.filled_buckets = 0
        self.hashmap = [None for i in range(size)]

    def key_to_index(self, key):
        sum = 0
        for c in key:
            sum += ord(c)
        return sum % self.size

    def __repr__(self):
        final = ""
        for i, v in enumerate(self.hashmap):
            if v != None:
                final += f" - {str(v)}\n"
        return final

#lesson 10
class HashMap:
    def insert(self, key, value):
        ori_index = self.key_to_index(key)
        index = ori_index
        first_iteration = True
        while self.hashmap[index] is not None and self.hashmap[index][0] != key:
            if not first_iteration and index == ori_index:
                raise Exception("hashmap is full")
            first_iteration = False
            index += 1
            index %= self.size
        self.hashmap[index] = (key, value)

    def get(self, key):
        ori_index = self.key_to_index(key)
        index = ori_index
        first_iteration = True
        while self.hashmap[index][0] is not key:
            if not first_iteration and index == ori_index:
                raise Exception("hashmap is full")
            first_iteration = False
            index += 1
            index %= self.size
        return self.hashmap[index][1]

    # don't touch below this line

    def __init__(self, size):
        self.size = size
        self.hashmap = [None for i in range(self.size)]

    def key_to_index(self, key):
        sum = 0
        for c in key:
            sum += ord(c)
        return sum % self.size

    def __repr__(self):
        final = ""
        for i, v in enumerate(self.hashmap):
            if v != None:
                final += f" - {str(v)}\n"
        return final