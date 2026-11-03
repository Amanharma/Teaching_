li_1 = [[12] * 2] 
li_2 = [[12] * 2] 


# def mul(ls, ls_1):
#     ref_lis = [[0]*5] *5
#     i = 0
#     k=0
#     while(i<len(ls)):
#         j = 0
#         while(j<len(ls)):
        
def traversing(li):

    i = 0
    while(i<len(li_1)):
        print(li_1[i], end =" ")   
        i +=1 

traversing(li= li_1)
print("+", end=" ")
traversing(li= li_2)
