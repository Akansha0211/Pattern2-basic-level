#pattern 1
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=' ')
    print()
for i in range(1,6):
    for j in range(5,i-1,-1):
        print(j,end=' ')
    print()

#Pattern2
for i in range(1,6):
    for j in range(1,i+1):
        print(i,end=' ')
    print()        
for i in range(5,0,-1):
    for j in range(1,i+1):
        print(i,end=' ')
    print()
