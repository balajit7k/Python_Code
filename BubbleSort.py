lst_values = [15,-2,1,25,6]
length_of_list = len(lst_values)
last_index =length_of_list-1
for x in range(last_index,-1,-1):
    for j in range(0,last_index):
        if(lst_values[j]>lst_values[j+1]):
            temp = lst_values[j]
            lst_values[j] = lst_values[j+1]
            lst_values[j+1] = temp
print(lst_values)

