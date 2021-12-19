#%%
import collections

city1 = {'yes':250, 'no':138, None:17}
city2 = {'yes':193, 'no':232, None:19}

counter1 = collections.Counter(city1)
counter2 = collections.Counter(city2)
suma = counter1 + counter2

print(suma)

city3 = {'yes':143, 'no':132, None:190}
counter3 = collections.Counter(city3)

suma1 = (counter3 + suma)
print(suma1.most_common(1))
print(suma1['yes']) # wyjecie z licznika ilosci


name = input(f"Podaj imię")
counter_name = collections.Counter(name.replace(" ","").lower())

print(counter_name)

# %%
