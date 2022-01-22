# filter() = creation a collections of elements from an iterable for whicha function returns true
# filter(function, iterable)
#%%
#from typing import List


friends =  [("Rachel", 19),
            ("Monika", 18),
            ("Phoebe", 17),
            ("Joey", 16),
            ("Chandler", 21),
            ("Ross", 21)]

age = lambda data:data[1] >= 18

drinking_buddies = list(filter(age, friends))

print(drinking_buddies)

for i in drinking_buddies:
    print(i)


# %%
