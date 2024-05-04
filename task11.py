l1 = [3,6,9,12,15,18,21]
l2 = [4,8,12,16,20,24,28]
new_list = []
for i in range(len(l1)):
    if i%2!=0:
        new_list.append(l1[i])
for i in range(len(l2)):
    if i%2==0:
        new_list.append(l2[i])
print(new_list)