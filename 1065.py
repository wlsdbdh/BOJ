N = int(input())
count = 0

for i in range (1, N+1) :
    if i < 100 :
        count += 1
    else :
        number = list(map(int, str(i)))
        if number[1] - number[0] == number[2] - number[1] :
            count += 1
            
print (count)
