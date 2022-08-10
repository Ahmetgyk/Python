import hashlib
import time

class Block:
    
    def __init__(self, timeStamp, data, previousHash=''):
        self.data = data   # list of 3 items such as [1,5,50]
        self.timestamp = timeStamp
        self.previousHash = previousHash
        self.kuvvet = 0
        self.hash = self.addHash()
  
    def addHash(self):
        while True:
            self.kuvvet = self.kuvvet + 1
            ozet = sha256((str(self.timeStamp) + str(self.data) + str(self.previousHash) + str(self.kuvvet)).encode()).hexdigest()
            if ozet[0:2] == "00":
                break
        return ozet

class BlockChain:
    
    def __init__(self):
        self.chain = [self.genesisOlustur()]
    
    def genesisOlustur(self):
        return block(time.ctime(), "AsilTurk", "")
        
    def blockEkle(self, data):
        node = block(time.ctime(), data, self.chain[-1].hash)
        self.chain.append(node)
        
    def kontrol(self):
        for i in range(len(self.chain)):
            if i != 0:
                ilk = self.chain[i - 1].hash