
# def BinariNumber2To10(number):
#     cnt=0
#     binary=0
#     one_number=0
#     while number>0:
#         one_number=number%10
#         binary+=one_number*2**cnt
#         cnt+=1
#         number//=10
#     return binary
# num = int(input())
# print(BinariNumber2To10(num))

# num=input()
# ben=len(num)
# binar=0
# cnt=0
# res=0  
# for i in range(ben):
#     binar=int(num)%10
#     res=int(res)+binar*2**cnt
#     cnt+=1
#     num=int(num)//10
# print(res)


def revers(num):
    res=''
    j=-1
    for i in range(len(num)):
        res+=num[j]
        j-=1
    return res

def binar(num):
    one_num=0
    res=''
    while num>0:
        one_num=num%2
        num=num//2
        res+=str(one_num)
    return revers(res)

number=int(input())
print(binar(number))