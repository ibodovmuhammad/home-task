def In_To_Ten(number):
    cnt=0
    while number>1:
        one_number=number%2
        number=number//2
        cnt=cnt*10+one_number
    chap=cnt*10+1
    res=0
    while chap>0:
        two=chap%10
        res=res*10+two
        chap=chap//10
    return res
number=int(input())
print(In_To_Ten(number))