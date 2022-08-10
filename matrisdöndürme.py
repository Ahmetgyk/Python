matris = [[1, 2, 6], [4, 2, 6], [9, 8, 9]]

[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
[[7, 4 ,1], [8, 5, 2], [9, 6, 3]]

#    [1, 2, 3]
#    [4, 5, 6]
#    [7, 8, 9]

#    [7, 4 ,1]
#    [8, 5, 2]
#    [9, 6, 3]

class Rotate():
    def __init__(self):
        pass
    
    def rotate(self, mtrs):
        rmt = [[0 for x in range(len(mtrs))] for y in range(len(mtrs))];
        
        for y in range(len(mtrs)):
            for x in range(len(mtrs)):
                rmt[y][x] = mtrs[(len(mtrs) - 1) - x][y];
        
        return rmt

print(Rotate().rotate(matris));