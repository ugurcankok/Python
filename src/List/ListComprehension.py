# [expression for item in list]
# [expression for item in list condition]
# [expression if condition else result for item in list]
# [(expression1, expression2) for item in list] for item in list]]

list = [0,1,2,3,4,5]

print([i for i in list])
print([i*10 for i in list if i%2 == 0])
print([i if i%2 == 0 else "odd number" for i in list])
print([i*1.18 for i in list if i >0])
