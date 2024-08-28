d=["sam", "ram", "kranthi", "ram", "suman", "krishna", "akbar","sam", "Krishna”]

# print(set(d))

new = []
for name in d:
    if name not in new: 
        new.append(name)
        
print(new)
