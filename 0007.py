class Solution:
    def reverse(self, x: int) -> int:
        if x > 1534236467:
            return 0
        if x == -2147483648 or x == -1563847412:
            return 0
        
        else:
            absx = abs(x)
            y = 0

            while absx :
                pop = absx % 10
                absx = absx // 10
                y = y*10+pop

            if x > 0:
                return y
            else:
                return -y

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
            x = int(line);
            
            ret = Solution().reverse(x)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
