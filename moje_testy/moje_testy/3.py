# sort() method     = used with lists
# sort function     = used with iterables
#%%
students = [("Squidward", "F", 60), 
            ("Sandy", "A", 33), 
            ("Patrick", "D", 36), 
            ("Spongebob", "B", 20),
            ("Mr. Krabs", "C", 78)]

grade = lambda x:x[0]
students.sort(key=grade, reverse=True)

for i in students:
    print(i)
# %%
students = (("Squidward", "F", 60), 
            ("Sandy", "A", 33), 
            ("Patrick", "D", 36), 
            ("Spongebob", "B", 20),
            ("Mr. Krabs", "C", 78))

grade = lambda x:x[0]
sorted_students = sorted(students, key=grade, reverse=True)
for i in sorted_students:
    print(i)

# %%
