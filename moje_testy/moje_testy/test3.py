import array as arr
a = arr.array("I",[3,6,9])
type(a)
print(a)


array_char = arr.array("u",["c","a","t","s"])
array_char.tounicode()
print(array_char[0])
print(array_char[1])
print(array_char[2])
print(array_char[3])
print(array_char[::-1])

graph = { "a" : ["c", "d"],
          "b" : ["d", "e"],
          "c" : ["a", "e"],
          "d" : ["a", "b"],
          "e" : ["b", "c"]
        }

def define_edges(graph):
    edges = []
    for vertices in graph:
        for neighbour in graph[vertices]:
            edges.append((vertices, neighbour))
    return edges

print(define_edges(graph))

class Tree:
    def __init__(self, info, left=None, right=None):
        self.info = info
        self.left  = left
        self.right = right

    def __str__(self):
        return (str(self.info) + ', Left child: ' + str(self.left) + ', Right child: ' + str(self.right))

tree = Tree(1, Tree(2, 2.1, 2.2), Tree(3, 3.1))
tree = Tree(1, Tree(2, 2.1, 2.2),Tree(3, 3.1, 3.2))
print(tree)

x_dict = {'Edward':11, 'Jorge':22, 'Prem':33, 'Joe':44}
del x_dict['Joe']

x_dict.update ({'Joe': 44})



print(x_dict['Edward']) # Prints the value stored with the key 'Edward'.


print(x_dict)
for i in x_dict:
    print (i, x_dict[i])
print(x_dict)
#You can apply many other inbuilt functionalies on dictionaries:
print('\n')

x_dict1 = dict((y,x) for x,y in x_dict.items())
for i in x_dict1:
    print (i, x_dict1[i])
print(x_dict1)
print('\n')

x_dict = {y:x for x,y in x_dict1.items()}
for i in x_dict:
    print (i, x_dict[i])
print(x_dict)
print('\n')
len(x_dict)

print(x_dict.keys())

print(x_dict.values())

print(x_dict.items())

CountryCodeDict1 = {"India": 91, "UK" : 44 , "USA" : 1, "Spain" : 34}
CountryCodeDict2 = {"Germany": 49, "Russia" : 7 , "Austria" : 43}
CountryCodeDict1.update(CountryCodeDict2)
print(CountryCodeDict1)