# i=1
# while(i<=4):
#     print(i,end="")
#
#     j=1
#     while(j<=4):
#         print(j,end='')
#         j+=1
#     i += 1
# print()

for i in range(1, 5 ):
    print(''.join(str(j) for j in range(i, 5)))
