class HashTable():
    def __init__(self):
        self.size = 11
        self.slots = [None]*11
        self.data = [None]*11
    
    def hashfunction(self,key,size):
        return key%size
    
    def rehase(self,oldhash,size):
        return (oldhash+1) % size
    
    def put(self,key,data):
        hashvalue = self.hashfunction(key,self.size)
        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data
            else:
                nextslot = self.rehase(hashvalue,self.size)
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehase(hashvalue,self.size)
                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data
    
    def get(self,key):
        startposition = self.hashfunction(key,self.size)
        found = False
        stop = False
        data = None
        position = startposition
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found =True
                data = self.data[position]
            else:
                position = self.rehase(position,self.size)
                if position == startposition:
                    stop = True
        return data
    
    def __getitem__(self,key):
        return self.get(key)
    
    def __setitem__(self,key,data):
        return self.put(key,data)


        
            