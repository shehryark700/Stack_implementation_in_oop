class Stack:
    def __init__(self):
        self.__stack =[]

    def push(self,val):
        self.__stack.append(val)

    def pop(self):
        val = self.__stack[-1]
        del self.__stack[-1]
        return val

class New_Stack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

    def sum(self):
        return self.__sum

    def push(self,val):
        self.__sum += val
        Stack.push(self,val)

    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val

obj = New_Stack()

for i in range(5):
    obj.push(i)
print(obj.sum())

for i in range(5):
    print(obj.pop())