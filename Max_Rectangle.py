class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        
        #if heights==[]:return 0
       
        # brutal force
        # l = len(heights)
        # #if l ==1: return heights[0]
        # for i in range(l):
        #     for j in range(i+1):
        #         tmp = (i-j+1)*min(heights[j:i+1])
        #         #print('i is {},j is {}, h is {},min h is {},temp is                      {}'.format(i,j,heights[j:i],min(heights[j:i+1]),tmp))
        #         res = max(res,tmp)
                

        heights.append(0)
        stack = [0]
        
        res = 0
        l = len(heights)

        # i records the leftest position of  for each value, the value is a decreasing array
        for i in range(1,l):
            while stack and heights[i] < heights[stack[-1]]:
                #print("i,stack:",i,stack)
                h = heights[stack.pop()]
                w = i if not stack else i - stack[-1] -1
                
                res = max(res, w*h)
                #print("i,stack,h,w,res:",i,stack,h,w,res)
                
            stack.append(i)
                
        return res

def stringToIntegerList(input):
    return json.loads(input)

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
            heights = stringToIntegerList(line)
            
            ret = Solution().largestRectangleArea(heights)

            out = intToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()
