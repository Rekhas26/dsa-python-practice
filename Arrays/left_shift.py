def left_shift(arr,k):
    start=0
    end = len(arr)-1

    # Reverse the entire array
    while start<end:
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1
    
    # Reverse the k eleemnts
    start,end = len(arr)-k, len(arr)-1
    while start<end:
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1

    # reverse the first eleemnts
    start,end = 0, len(arr)-k-1
    while start<end:
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1
    return arr

arr = [10,20,30,40,50,60,70,49,67,76]
print(left_shift(arr,4))
