class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle=list()
        
        for i in range(0,rowIndex+1):
            row=list()
            for j in range (0,i+1):
                if j == i or j==0:
                    row.append(1)
                else:
                    row.append(triangle[i-1][j-1]+triangle[i-1][j])
            triangle.append(row)
        return row




def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            rowIndex = int(line);
            
            ret = Solution().getRow(rowIndex)

            out = integerListToString(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
