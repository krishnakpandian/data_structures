class queue:
    def __init__(self, arr: List[int]):
        if arr:
            self.arr = arr
        else:
            self.arr = []
        self.size = len(arr)
        
    def enqueue(self, value: int):
        self.arr.append(value)

    def dequeue(self) -> int: 
        if self.size > 0:
            return self.arr.pop(0)
    
        