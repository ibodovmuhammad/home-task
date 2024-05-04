my_list = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
new_list=[]
zero=0
cnt=0
for i in range(len(my_list)):
    if my_list[i]!=0:
        new_list.append(my_list[i])
    if my_list[i]==0:
        cnt+=1
for i in range(cnt):
    new_list.append(zero)
print(new_list)