lst_values = [15,-2,1,25,9]

def mergesort(lst,low,high):
    if(low<high):
        mid = int((low+high)/2)
        mergesort(lst,low,mid)
        mergesort(lst,mid+1,high)
        merge(lst,low,mid,high)

def merge(lst,low,mid,high):
    lst_new_arr = [0 for x in lst]
    i=low
    j=mid+1
    k=low
    while(i<=mid and j <= high):
        if(lst[i]<lst[j]):
            lst_new_arr[k] = lst[i]
            i = i+1
            k = k+1
        else:
            lst_new_arr[k] = lst[j]
            j=j+1
            k=k+1
    
    while(i<=mid):
        lst_new_arr[k] = lst[i]
        i=i+1
        k=k+1

    while(j<=high):
        lst_new_arr[k] = lst[j]
        j=j+1
        k=k+1

    for x in range(low,high+1):
        lst[x] = lst_new_arr[x]


mergesort(lst_values,0,len(lst_values)-1)
print(lst_values)