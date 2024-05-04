my_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
my_dict = {}
for num in my_list:
    if num in my_dict:
        my_dict[num]+=1
    else: my_dict[num] = 1
print(my_dict)
