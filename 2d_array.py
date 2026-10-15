lis= [[12, 23, 32, 13, 43, 45], [12, 23, 32, 13, 43, 45], [12, 23, 32, 13, 43, 45],[12, 23, 32, 13, 43, 45]]

def insertion(index, idx, element, li):
    
    ref_arr =[0] * (len(li[index]) +1)

    i = 0
    while(i< idx):
        ref_arr[i] = li[index][i]
        i +=1
    
    ref_arr[i]= element

    i+=1
    while(i<len(ref_arr)):
        ref_arr[i]= li[index][i-1]
        i +=1

    li[index] = ref_arr  
   
    return li  

print(lis)
print(insertion(index=2, idx= 1, element="A", li=lis))    
