#%%
tv = ["Jaka", "Spadkobiercy", "Familiada"]
i = 0
# for show in tv:
#     new = tv[i]
#     print(new)
#     new = new.upper()
#     tv[i] = new
#     print(tv[i])
#     i += 1


# print (tv)

# # for show in tv:
# #     for i in range(0, len(show)-1):
# #         print(len(show))
# #         show[i].lower()
# #         print(i)
# #         print(show)
# #         print(show[i])
# #         #show[i] = new
# #         #new = new.upper()
# #         #tv[i] = new
# #         #print(tv[i])
# #         i += 2

# mystring = ''

# for idx, x in enumerate(tv):
#     if idx % 2 == 0:
#         mystring  = mystring + x.lower()
#     else:
#         mystring = mystring + x.upper()

# print (tv)


# def myfunc(mylist):
#     mychars = []
#     upper = False
#     for x in mylist:
#         mychars.append(x.upper() if upper else x.lower())
#         upper = not upper
#     return ''.join(mychars)

# myfunc(tv)
# print(tv)
# i = 0
# for idx, x in enumerate(tv):
#     tv[idx] = "".join([x.upper() if i%2!=0 else x.lower() for i,x in enumerate(tv)])

print(tv)
i = 0
x = ''
y = []
for idx, x in enumerate(tv):
    tv[idx] = "".join([x.lower() if i%2!=0 else x.upper() for i,x in enumerate(x)])

print(tv)
print(y)
