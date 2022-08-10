class Faktriyel():
    def __init__(self):
        pass
    
    def faktoriyel(self, sy):
        fk = "";
        fklist = [];
        sylist = [];
        
        for i in range(sy):
            fklist.append(i + 1)
        
        for i in range(len(fklist)):
            if(i > 2):
                for k in range(2,i):
                    if i%k != 0:
                        sylist.append(k);
                        break
        
        return (fklist,sylist)

print(Faktriyel().faktoriyel(12));