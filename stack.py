class stack:
    def __init__(self,arr):
        if arr:
            self.arr = arr
        else:
            self.arr = []
        self.length = len(arr)

    def push(self, value: int):
        self.arr.append(value)

    def pop(self) -> int: 
        if self.size > 0:
            return self.arr.pop()