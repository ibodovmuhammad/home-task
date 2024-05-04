# def zarb(n):
#     for j in n:
#         print(end="\n")
#         j=int(j)
#         for i in range(1,11):
#             print(f"{j}*{i}={j*i}")
# n=input().split()
# zarb(n)

# def arif(n_list):
#     sum=0
#     cnt=0
#     for i in range(len(n_list)):
#         sum+=int(n_list[i])
#         cnt+=1
#     print(sum//cnt)
# n=input().split()
# arif(n)

# def arif(n_list):
#     sum=0
#     for i in n_list:
#         sum+=int(i)
#     return sum/len(n_list)
# n=input().split()
# print(arif(n))

# n = input().split()
# small=n[0]
# for i in range(len(n)):
#     if int(n[i])<int(small):
#         small=n[i]
# print(f"minimum_number: {small}")

number = input().split()
minimum=number[0]
for element in number:
    if element<minimum:
        minimum=element
print(minimum)