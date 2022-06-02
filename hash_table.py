class HashTable:  
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]
        
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    
    def __getitem__(self, key):
        h = self.get_hash(key)
        for val in self.arr[h]:
            if val[0] == key:
                return val[1]
    
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        st = False
        for idx, ele in enumerate(self.arr[h]):
            if len(ele) == 2 and ele[0] == key:
                self.arr[h][idx] = (key,val)
                st = True
                break
        if not st:
            self.arr[h].append((key,val))
        
    def __delitem__(self, key):
        h = self.get_hash(key)
        for i, ele in enumerate(self.arr[h]):
            if ele[0] == key:
                print("del", i)
                del self.arr[h][i]
        

t = HashTable()
t["march 6"] = 310
t["march 7"] = 420
t["march 62"] = 392
del t["march 6"]
print(t.arr, t["march 62"], t["march 7"])