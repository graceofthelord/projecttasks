# task 2: list all the prime numbers from 1-50
for i in range(1,51):
    for j in range (2,i):
        if i % j == 0:
            break
    else:
        print(i)