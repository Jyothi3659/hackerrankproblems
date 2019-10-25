def array_func(arr):
    final_count = -85236974002456
    total = 0
    for i in range(len(arr)-2):
        for j in range(len(arr[i])-2):
            total += (arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2])
            if final_count < total:
                final_count = total
                total = 0
            else:
                total = 0
    return final_count
# print(array_func([[1,1,1,0,0,0],[0,1,0,0,0,0],[1,1,1,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]))
# print(array_func([[1,1,1,0,0,0],[0,1,0,0,0,0],[1,1,1,0,0,0],[0,0,2,4,4,0],[0,0,0,2,0,0],[0,0,1,2,4,0]]))
print(array_func([[1,1,1,0,0,0],[0,1,0,0,0,0],[1,1,1,0,0,0],[0,9,2,-4,-4,0],[0,0,0,-2,0,0],[0,0,-1,-2,-4,0]]))
print(array_func([[-1,-1,0,-9,-2,-2],[-2,-1,-6,-8,-2,-5],[-1,-1,-1,-2,-3,-4],[-1,-9,-2,-4,-4,-5],[-7,-3,-3,-2,-9,-9],[-1,-3,-1,-2,-4,-5]]))