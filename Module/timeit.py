#%%
import timeit
# code to kod do wykonania. za pomoca timeit mierzymy ile czasu sie wykonuje


code = """
numbers = []
for i in range(10):
    numbers.append(i)
"""
code1 = """
numbers = [x for x in range(10)]
"""

print(timeit.timeit(code,number= 2000000))
print()
print(timeit.timeit(code1,number= 2000000))
numbers = [x for x in range(10)]


t1 = (timeit.timeit(code,number= 2000000))
t2 = (timeit.timeit(code1,number= 2000000))
#print (numbers)
if t1 > t2:
    print (f"code był szyszy\n {code}")
else: print(code1)

results = {}

# %%
