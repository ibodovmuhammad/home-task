list1=[1,2,3]
list2=[4,5,6]
list3=[10,11,12]
list4=[7,8,9]
sum1=0
sum2=0
sum3=0
sum4=0
for i in range(len(list1)):
    sum1+=list1[i]
    sum2+=list2[i]
    sum3+=list3[i]
    sum4+=list4[i]
if sum1>=sum2 and sum1>=sum3 and sum1>=sum4:
    print(list1)
elif sum2>=sum1 and sum2>=sum3 and sum2>=sum4:
    print(list2)
elif sum3>=sum1 and sum3>=sum2 and sum3>=sum4:
    print(list3)
else:
    print(list4)