# # # num = int(input())
# # # for i in range(1,num+1):
# # #     print(f"Curent number is: {i} and the cube is {i**3}")

# # my_list = input().split()
# # for i in range(len(my_list)):
# #     if int(my_list[i])%5==0:
# #         print(my_list[i])
        


# #         my_str = "Emma is good developer. Emma is a writer"
# # cnt=0
# # for i in range(len(my_str)):
# #     if my_str[i: i+4]=="Emma":
# #         cnt+=1
# # print(f"Emma appeared {cnt} times")



# # # my_str = "Emma is good developer. Emma is a writer"
# # # cnt = my_str.count("Emma")
# # # print(cnt)



# # number = int(input())
# # b=0
# # for i in range(number):
# #     b+=1
# #     print(end="\n")
# #     for j in range(i):
# #         print(b,end=" ")

# number = int(input())
# b=0
# i=1
# while i<=number:
#     print(end="\n")
#     b+=1
#     j=1
#     while j<=i:
#         print(b,end=" ")
#         j+=1
#     i+=1



# strin = "google come"
# my_list = list(strin)
# my_dict = {}
# for i in my_list:
#     if i in my_dict:
#         my_dict[i]+=1
#     else:
#         my_dict[i]=1
# print(my_dict)


# letter = input()
# if len(letter)>3:
#     if letter[-1]=='g' and letter[-2]=='n' and letter[-3]=='i':
#         print(letter+'ly')
#     else:
#         print(letter+'ing')
# else:
#     print(letter)


# number = input()
# for i in range(len(number)):
#     print(number[i-1],end=" ")

# number=int(input())
# res=number
# chap=0
# while number>0:
#     chap=chap*10+number%10
#     number//=10
# if chap==number:
#     print(f"Original number {res}")
#     print(f"Yes. Given number is a palindrome")
# else:
#     print(f"Original number {res}")
#     print(f"No. Given number is not palindrome")


# def my_len(len1):
#     my_len=0
#     for i in len1:
#         my_len+=1
#     return my_len
# n=input()
# print(my_len(n))

# number=int(input())
# yesterday=0
# for i in range(number):
#     print(f"Current number {i} previous number {yesterday} suma: {i+yesterday}")
#     yesterday=i

# number=int(input())
# i=0
# prev = 0
# while i<=number:
#     print(f"Current number {i} previous number {prev} suma:{prev+i}")
#     prev = i
#     i+=1

# striv=input()
# for i in range(len(striv)):
#     if i%2==0:
#         print(striv[i])


# star=input()
# inat=int(input())
# for i in range(len(star)):
#     if i>inat:
#         print(star[i])


# def string(stringer,number):
#     for i in range(len(stringer)):
#         if i>number:
#             print(stringer[i],end='')
# str1=input()
# num=int(input())
# string (str1,num)

# def string(stringer,number):
#     for i in range(number,len(stringer)):
#         print(stringer[i],end='')
# str1=input()
# num=int(input())
# string (str1,num)

# n=input()
# if n[0]==n[-1]:
#     print(True)
# else:
#     print(False)

# str1 = input()
# str2 = input()
# l_str1 = str1[0:2]
# l_str2 = str2[0:2]
# print(l_str2+str1[2:],l_str1+str2[2:])

# my_string = input()
# n = int(input())
# new_string = ''
# for letter in range(0, len(my_string)):
#     if letter != n:
#         new_string += my_string[letter]
# print(new_string)

# def my_len(len1):
#     my_len=0
#     for i in len1:
#         my_len+=1
#     return my_len
# n=input()
# print(my_len(n))

# number=int(input())
# yesterday=0
# for i in range(number):
#     print(f"Current number {i} previous number {yesterday} suma: {i+yesterday}")
#     yesterday=i

# number=int(input())
# i=0
# prev = 0
# while i<=number:
#     print(f"Current number {i} previous number {prev} suma:{prev+i}")
#     prev = i
#     i+=1

# striv=input()
# for i in range(len(striv)):
#     if i%2==0:
#         print(striv[i])


# star=input()
# inat=int(input())
# for i in range(len(star)):
#     if i>inat:
#         print(star[i])


# def string(stringer,number):
#     for i in range(len(stringer)):
#         if i>number:
#             print(stringer[i],end='')
# str1=input()
# num=int(input())
# string (str1,num)

# def string(stringer,number):
#     for i in range(number,len(stringer)):
#         print(stringer[i],end='')
# str1=input()
# num=int(input())
# string (str1,num)

# n=input()
# if n[0]==n[-1]:
#     print(True)
# else:
#     print(False)

# str1 = input()
# str2 = input()
# l_str1 = str1[0:2]
# l_str2 = str2[0:2]
# print(l_str2+str1[2:],l_str1+str2[2:])


# my_string = input()
# n = int(input())
# new_string = ''
# for letter in range(0, len(my_string)):
#     if letter != n:
#         new_string += my_string[letter]
# print(new_string)


# number = int(input())
# i=1
# b=0
# while i<=number:
#     print(end="\n")
#     j=1
#     while j<=i:
#         print("*",end=" ")
#         j+=1
#     i+=1
# i=1
# while number>=i:
#     print(end="\n")
#     j=1
#     while j<=number-1:
#         print("*",end=" ")
#         j+=1
#     number-=1


# my_list = [10,20,60,30,20,40,30,60,70,80]
# new_lest = []
# for i in range(len(my_list)):
#     if my_list[i] in my_list[i+1:]:
#         new_lest.append(my_list[i])
# print(new_lest)

# my_list = [10,20,60,30,20,40,30,60,70,80]
# new_list = []
# duplicat_list = []
# for i in my_list:
#     if i not in new_list:
#         new_list.append(i)
#     else:
#         duplicat_list.append(i)
# print(duplicat_list)




