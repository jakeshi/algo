class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        ret = 0
        last = -1
        
        for i in range(len(s)):
            if s[i] == '(': 
                stack.append(i)
            
            else:  
                if not stack:
                    last = i
                else:
                    stack.pop()
                    if stack==[]:
                        ret = max(ret,i-last)
                    else: # there are multiple remaining left brackets
                        ret = max(ret,i-stack[-1])
                        
        #print("i is {} and ret temp is {},ret is {}".format(0,ret_temp,ret))
        
        return ret

def stringToString(input):
    return input[1:-1].decode('string_escape')

def intToString(input):
    if input is None:
        input = 0
    return str(input)

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = lines.next()
            s = stringToString(line)
            
            ret = Solution().longestValidParentheses(s)

            out = intToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()
