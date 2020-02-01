# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range (0,len(arr)):
        min_index = i
        for j in range (i,len(arr)):
            if (arr[j]<arr[min_index]):
                min_index = j
            j+=1
        temp = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = temp
        i+=1
    return arr


# TO-DO:  implement the Bubble Sort function below
# comments bubble sort
# [3,21,6,33,5]
# 3,6,21,5,33
# 3,6,5,21,33
# 3,5,6,21,33

#     for i=0 to arr len
#  arr[i]>arr[i+1] then

def bubble_sort( arr ):
    for i in range (0,len(arr)-1):
        for j in range (0,len(arr)-1-i):
            if arr[j]>arr[j+1]:
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
            j+=1
        i+=1
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    return arr