# first ex and practice
i = 0
while i < 100:
    print(i)
    i += 10

# second ex and practice
for i in range (0,100,10):
    print(i)

# third ex and practice
i = 0
j = 1
k = 0
while i < 1000:
    print(i)
    k = i + j
    i = j
    j = k

# fourth ex and practice
for i in range (0,10):
    print(i)
    for j in range (0,3):
        print("hi")

# fifth ex and practice
for i in range (0,10):
    for j in range (0,3):
        if j == 1:
            print(j)
            break
    
# sixth ex and practice
for i in range (0,10):
    for j in range (2,3):
        if i % j == 0:
            break
        else:
            print(i)