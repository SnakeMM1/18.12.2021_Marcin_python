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

# print(timeit.timeit(code,number= 2000000))
# print()
# print(timeit.timeit(code1,number= 2000000))
xnumbers = [x for x in range(10)]


t1 = (timeit.timeit(code,number= 200000))
t2 = (timeit.timeit(code1,number= 200000))
#print (numbers)
# if t1 < t2:
#     print (f"code był szyszy\n {code}")
# else: print(f"code1 był szyszy\n {code1}")

results = {'code': t1, 'code1': t2}
r = results.items()
print(r, type(r))

#print (results)
print(sorted(results.items()))
print(sorted(results.items(), key = lambda x : x[1])[0][0])
# lambda sortuje po wartosciach bo jest 1. potem [0] pierwsze to pierwsza tupla, drugie [0] to pierwszy element w pierwszej tupli
# sortujemy slownik i dostajemy liste tupli



# %%
