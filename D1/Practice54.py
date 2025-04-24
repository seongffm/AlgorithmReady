#함수의 기초5
def one_lst(lst):
    play1 = lst
    print(play1)
    #set 함수의 반환값은 set객체 {}
    #sorted함수의 반환값은 list
    play2 = sorted(set(lst))
    print(play2)
one_lst([1, 2, 3, 4, 3, 2, 1])