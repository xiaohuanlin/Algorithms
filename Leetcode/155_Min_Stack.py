'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
'''

class MinStack(object):
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min = []
        self.stack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if self.min == [] or self.min[-1] > x:
            self.min.append(x)
        else:
            self.min.append(self.min[-1])
        self.stack.append(x)
        

    def pop(self):
        """
        :rtype: void
        """
        self.min.pop()
        self.stack.pop()
            
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.getMin())
obj.pop()
print(obj.top())
