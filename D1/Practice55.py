#함수의 기초6
lst = [2,4,6,8,10]
print(lst)
def seek(lst,num):
    if lst.count(num)!=0:
        print(f"{num} => True")
    else:
        print(f"{num} => False")
seek(lst,5)
seek(lst,10)