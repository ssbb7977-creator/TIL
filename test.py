#11
#12
grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
row = len(grid)
col = len(grid[0])
# print(grid)
# print(row)
# print(col)
count = 0   # 겹침 개수
count_1 = 0 # 1의 개수  
for i in range(row):
    for j in range(col):
        print(i)
        print(j)
        if grid[i][j] == 1:
            count_1 += 1    
        if grid[i][j] == 1 and grid[i][j-1] == 1:
            count +=1 
        if grid[i][j] == 1 and grid[i][j+1] == 1:
            count +=1
        if grid[i][j] == 1 and grid[i-1][j] == 1:
            count +=1
        if grid[i][j] == 1 and grid[i+1][j] == 1:
            count +=1
print(count_1*4)
print(count)
print(count_1*4 - count)