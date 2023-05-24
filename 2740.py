n, m = map(int, input().split())
x = [list(map(int, input().split())) for _ in range (n)]

m, k = map(int, input().split())
y = [list(map(int, input().split())) for _ in range (m)]

answer = [[0] * k for _ in range (n)]  

for i in range (n) :
    for j in range (k) :
        for l in range (m) :
            answer [i][j] += x[i][l] * y[l][j]
            
for i in answer :
    for j in i :
        print (j, end = ' ')
    print ()
