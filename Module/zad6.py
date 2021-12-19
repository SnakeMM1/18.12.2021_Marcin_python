#%%
import os

#print(sorted(results.items(), key = lambda x : x[1])[0][0])
file_names = sorted([name for name in os.listdir() if name.startswith('m')])
file_names1 = sorted([name for name in os.listdir() if name[0] == 'm'], reverse=True)
print(file_names)
print(file_names1)
# %%
