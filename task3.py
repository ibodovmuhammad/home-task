my_dict={}
while True:
    your_key=input("input your key-->")
    if your_key=='stop':
        break
    your_value=input("input your value-->")
    my_dict[your_key]=your_value
print(my_dict)