T = int(input()) # 테스트 케이스 
for _ in range(T):
    N, M = map(int,input().split()) # N : 행렬 배열, M: 분사 범위 
    max_value = 0 # 최대 파리 잡은 개수 
    matrix = []
    for _ in range(N):  # 행렬 자료구조 저장 
        array = list(map(int,input().split()))
        matrix.append(array)
    
    print("행렬:",matrix)

    for idx, row in enumerate(matrix):
        value = row[idx:idx+M] + row[idx:idx-M] + row[idx-M:idx]