lst_values = [15,-2,1,25,6]
int_length_of_list = len(lst_values)
int_last_index = int_length_of_list-1
for int_index in range(1,int_last_index+1):
    current_index_value = lst_values[int_index]
    current_position = int_index
    while(current_position > 0 and lst_values[current_position-1]>current_index_value):
        lst_values[current_position] = lst_values[current_position-1]
        current_position = current_position-1
    lst_values[current_position] = current_index_value