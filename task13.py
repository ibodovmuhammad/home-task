listing = [11, 45, 8, 23, 14, 12, 78, 45, 89]
list1 = []
list1=listing[0:3]
list2 = []
list2=listing[3:6]
list3 = []
list3=listing[6:]
for i in range(1):
    print("Chunk 1",list1)
    print("After reversing it ",list1[::-1])
    print("Chunk 2",list2)
    print("After reversing it ",list2[::-1])
    print("Chunk 3",list3)
    print("After reversing it ",list3[::-1])