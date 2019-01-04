# n = list(range(1,5))


# ## Q1
# n.reverse()
# # for i in n :
# #     a = "*"*i
# #     print(a)

# ## Q2
# # for i in n :
# #     a = "*"*i
# #     print(a)

## Q3
for i in range(1,6):
    for j in range(1,6-i):
        print(" ", end = "")
    for j in range(1,i+1):
        print("$",end="")
    print()        
