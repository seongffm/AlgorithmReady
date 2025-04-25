#함수의 기초 8
num_lst = input()
lst = num_lst.split(', ')
for i in lst:
    print(f"square({i}) => {int(i)**2}")