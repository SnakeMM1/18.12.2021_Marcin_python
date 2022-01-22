#%%
store = [("shirt", 20), 
        ("pants", 25),
        ("jacket", 100),
        ("socks", 10)]

to_euros =lambda data: (data[0], data[1]/0.82)
store_euros = list(map(to_euros, store)) #map() = applies function in each iterable(list, tuple, etc)
#to_euros_1 = list([round(x, 2) if isinstance(x, float) else x for x in store_euros])

to_euros_2 = [(item[0],round(item[1],5)) for item in store_euros]

to_euros_3 = [(item[0],round(item[1]/0.82,5)) for item in store]


print(list(store_euros))

for i in store_euros:
    print(i)
print()
for i in to_euros_2:
    print(i)
print()
for i in to_euros_3:
    print(i)

#%%
print(round(123.345, 2))
# %%
