# 행렬의 곱셈

def solution(arr1, arr2):
    a = [[0 for i in range(len(arr2[0]))] for i in range(len(arr1))]
    
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr1[0])):
                a[i][j]+=arr1[i][k]*arr2[k][j]
    
    return a