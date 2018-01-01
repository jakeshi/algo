
def MaxRectangleArea(self, height):
    height.append(0)
    stack = [0]
    ret = 0
    for i in range(1, len(height)):
        while stack and height[i] < height[stack[-1]]:
            h = height[stack.pop()]
            w = i if not stack else i - stack[-1] -1
            ret = max(r, w*h)
        stack.append(i)
    return ret
