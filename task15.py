number = [47, 64, 69, 37, 76, 83, 95, 97]
my_dict = {'Jhon': 47, 'Emma': 69, 'Kelly': 76, 'Jason': 97}
new_list = []
for i in number:
    if i in my_dict.values():
        new_list.append(i)
print(new_list)