class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        n = len(coordinates)
        if n == 2:return True
        try:
            k = (coordinates[1][1]-coordinates[0][1])/(coordinates[1][0]-coordinates[0][0])
        except ZeroDivisionError:
            for i in range(1,n):
                if coordinates[i][0]!=coordinates[0][0]:
                    return False
            return True
        else:
            b = coordinates[0][1] - k*coordinates[0][0]
            for i in range(2,n):
                if coordinates[i][1]!=k*coordinates[i][0]+b:
                    return False
            return True
