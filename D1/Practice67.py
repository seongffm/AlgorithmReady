lst=[1,2,3,4,5,6,7,8,9,10]
lst2 = list(filter(lambda x: x%2==0,lst))
lst3 = list(map(lambda x: x**2,lst2))
print(lst3)