def decimal_to_base(A,B):
    result=[]
    
    while A>0:
        Q=A//B
        R=A%B
        result.insert(0,str(R)) 
        A=Q
    
    return ''.join(result)  

A=int(input())
B=int(input())
converted_number=decimal_to_base(A,B)
print(converted_number) 

