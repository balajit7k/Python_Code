lst_unsorted = [15,-1,36,20,2,0,-14,25]

for outer_index in range(len(lst_unsorted)-1):
    outer_number = lst_unsorted[outer_index]
    low_index = outer_index
    for inner_index in range(outer_index+1,len(lst_unsorted)):
        #inner_number = lst_unsorted[inner_index]
        if lst_unsorted[inner_index] < lst_unsorted[low_index]:
            low_index = inner_index
    lst_unsorted[low_index],lst_unsorted[outer_index] = lst_unsorted[outer_index],lst_unsorted[low_index]
    #temp = lst_unsorted[low_index]
    #lst_unsorted[low_index] = lst_unsorted[outer_index]
    #lst_unsorted[outer_index] = temp

for int_number in lst_unsorted:
    print(int_number)


