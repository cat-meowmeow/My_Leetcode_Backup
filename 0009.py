class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        if x > 0:            
            y = 0
            xx = x

            while xx > 0:                
                pop = xx % 10
                xx = xx//10
                y = y*10 + pop

            if x == y:
                return True
            else :
                return False
        
        if x == 0:
            return True

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
            
            ret = Solution().isPalindrome(x)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
