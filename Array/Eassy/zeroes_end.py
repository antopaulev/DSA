arr = [0, 1, 0, 3, 12]
def move_zeroes(arr):
    n = len(arr)
    temp = []
    for i in range(0,n):
        if arr[i] != 0:
            temp.append(arr[i])
    nt = len(temp)
    for i in range(0, nt):
        arr[i] = temp[i]
    for i in range(nt, n):      
        arr[i] = 0

move_zeroes(arr)
print(arr)
