lst_data = ["60,com","100,google.com", "50,abcd.google.com", "10,acd.abcd.google.com","40,microsoft.com","50,xyz.microsoft.com","20,123.abcd.google.com","50,summa.in","200,in","50,mass.in"]
dict_visit_count = {}

for str_data in lst_data:
    arr_data = str_data.split(",")
    visit_count = int(arr_data[0])
    url = arr_data[1]
    arr_url = url.split(".")
    int_last_index = len(arr_url) - 1
    int_current_index = int_last_index
    str_key = ""
    indi_visit_count = 0
    while int_current_index >= 0:
        if int_last_index == int_current_index:
            str_key = arr_url[int_last_index]
        else:
            arr_url_temp = arr_url[int_current_index:]
            str_key = '.'.join(arr_url_temp)
        if str_key in dict_visit_count:
            indi_visit_count= int(dict_visit_count[str_key])
            indi_visit_count = indi_visit_count + int(visit_count)
            dict_visit_count[str_key] = indi_visit_count
        else:
            dict_visit_count[str_key] = visit_count
        int_current_index = int_current_index-1
        
for key, value in dict_visit_count.items():
    print(key + "---" + str(value))
    