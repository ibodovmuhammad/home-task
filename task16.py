my_dictionary = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}
my_list = []
for v in my_dictionary.values():
    if v not in my_list:
        my_list.append(v)
print(my_list)