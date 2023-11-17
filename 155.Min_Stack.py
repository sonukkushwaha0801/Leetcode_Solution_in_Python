#Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val , self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
        
# Another way:
class MinStack:

    def __init__(self):
        self.st=[] #stack
        self.min=None #min element

    def push(self, val: int) -> None:
        if len(self.st)==0:
            self.st.append(val)
            self.min=val
        else:
            if val>=self.min:
                self.st.append(val)
            else:
                self.st.append(2*val-self.min)
                self.min=val
                
    def pop(self) -> None:
        x=self.st.pop() 
        if x<self.min:
            self.min=2*self.min-x
    
    def top(self) -> int:
        x=self.st[-1]
        if x>=self.min:
            return x
        return self.min

    def getMin(self) -> int:
        return self.min