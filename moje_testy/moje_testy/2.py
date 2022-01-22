#import numpy as np
#%%
vals = [[1,2,3],[4,5,2],[3,2,6]]
print(f'{vals}\n')
vals_exp = [y for x in vals for y in x]
print(vals_exp)
print(f'\n')

vals_exp = [ y*2 for x in vals for y in x]
print(vals_exp)
print(f'\n')

vals_exp1 = []
# vals_exp = [x for y in vals for y in x]
# print(vals_exp)
# print(f'\n')
for x in vals:
    for y in x:
        vals_exp1.append(y*2)
print(vals_exp1)
print(f'\n')
# %%
text = [['bar','foo','fooba'],['Rome','Madrid','Houston'], ['aa','bb','cc','dd']]
text_1 = [y for x in text if len(x)>3 for y in x]
print(text_1)

text_2 = [y for x in text for y in x if len(y)>4]
print(text_2)

text_3 = [y.upper() for x in text if len(x) == 3 for y in x if y.startswith('f')]
print(text_3)