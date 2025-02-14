#716
#hard

#Design a max stack data structure that supports the stack operations and supports finding the stack's maximum element.

#Implement the MaxStack class:

#MaxStack() Initializes the stack object.
#void push(int x) Pushes element x onto the stack.
#int pop() Removes the element on top of the stack and returns it.
#int top() Gets the element on the top of the stack without removing it.
#int peekMax() Retrieves the maximum element in the stack without removing it.
#int popMax() Retrieves the maximum element in the stack and removes it. If there is more than one maximum element, only remove the top-most one.
#You must come up with a solution that supports O(1) for each top call and O(logn) for each other call.

 

#Example 1:

#Input
#["MaxStack", "push", "push", "push", "top", "popMax", "top", "peekMax", "pop", "top"]
#[[], [5], [1], [5], [], [], [], [], [], []]
#Output
#[null, null, null, null, 5, 5, 1, 5, 1, 5]

#Explanation
#MaxStack stk = new MaxStack();
#stk.push(5);   // [5] the top of the stack and the maximum number is 5.
#stk.push(1);   // [5, 1] the top of the stack is 1, but the maximum is 5.
#stk.push(5);   // [5, 1, 5] the top of the stack is 5, which is also the maximum, because it is the top most one.
#stk.top();     // return 5, [5, 1, 5] the stack did not change.
#stk.popMax();  // return 5, [5, 1] the stack is changed now, and the top is different from the max.
#stk.top();     // return 1, [5, 1] the stack did not change.
#stk.peekMax(); // return 5, [5, 1] the stack did not change.
#stk.pop();     // return 1, [5] the top of the stack and the max element is now 5.
#stk.top();     // return 5, [5] the stack did not change.



#my own solution using python3:

#use a dictionary along with a sorted list 

class MaxStack:

    def __init__(self):
        self.stack = []
        self.s = SortedList()
        self.c = Counter(self.stack)

        
    def push(self, x: int) -> None:
        self.s.add(x)
        self.stack.append(x)
        self.c[x] += 1
        
    def pop(self) -> int:
        if self.stack:
            a = self.stack.pop()
            self.c[a] -= 1
            if self.c[a] == 0:
                del self.c[a]
            self.s.remove(a)
            return a
        
    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        
    def peekMax(self) -> int:
        return self.s[-1]
        
    def popMax(self) -> int:
        self.biggest = self.s[-1]
        if self.biggest == self.stack[0]:
            if self.c[self.biggest] == 1:
                self.s.pop()
                return self.stack.pop(0)
        for i in range(len(self.stack) -1, -1, -1):
            if self.stack[i] == self.biggest:
                self.s.pop()
                return self.stack.pop(i)
        
