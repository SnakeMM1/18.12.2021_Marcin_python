class Stack: 
   def __init__(self): 
    self.__items__ = []
 
   def is_empty(self):  
    return not self.__items__
  
   def push(self, item):  
    self.__items__.append(item) 
  
#    def pop1(self):  
#     return self.__items__.pop()
   def pop2(self): 
        val = self.__items__[-1]
        del self.__items__[-1]
        return val 

   def size(self):  
    return len(self.__items__)
   def peek(self):  
    return self.__items__[-1] 
   def __str__(self):  
    return str(self.__items__)
    

# s = Stack()

# s.push("cytryna")
# s.push("pomarancza")
# print(s)
# print(s.size())
# print(s.peek())
# s.pop1()
# print(s)
# print(s.size())
# print(s.peek())

maly = Stack()
inny = Stack()
zabawny = Stack()
maly.push(19)
inny.push (maly.pop2() +1)
inny.push (77)
inny.push (333)
print(inny.pop2())
print(maly)
print(inny)
print(zabawny)
zabawny.push(inny.pop2() - 2)

print(zabawny.pop2())
print(zabawny)