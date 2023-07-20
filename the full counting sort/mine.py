
def countSort(arr):
    sorted_arr =  [[] for i in range(0,100)]
    result_arr=[]
    for i in range(len(arr)):
        if i < len(arr)/2:
            sorted_arr[int(arr[i][0])].append("-")
        else:
            sorted_arr[int(arr[i][0])].append(arr[i][1])
    print(" ".join([' '.join(x) for x in sorted_arr if len(x)>0]))
