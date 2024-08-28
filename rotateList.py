x = [10,20,30,40,50]


rotated = [0] *len(x)
rotated[0] = x[-1]
for i in range(1,len(x)):

    rotated[i] = x[i-1]
    
print(rotated)

