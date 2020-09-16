class Iterator:
    def __init__(self, limit=0):
        self.limit = limit
        self.val = 0
    def __iter__(self):
        return self

    def __next__(self):
        value = self.val
        if self.val > self.limit:
            raise StopIteration
        self.val += 1
        return value

for i in Iterator(15):
    print(i)


