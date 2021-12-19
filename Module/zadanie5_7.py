#%%

import os

#os.mkdir('Months')
months_list = [f'{str(i).zfill(2)}_raport' for i in range(1,13)]

for month in months_list:
    path = os.path.join('Months', month)
    os.mkdir(path)

print(months_list)
# %%
