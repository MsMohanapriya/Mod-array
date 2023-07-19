def ModArray(array,dividend):
    result=0
    # power=1
    for i in range(len(array)):
        result=(result*10 + array[i])%dividend
        # power=(power*10)%dividend        
    return result
array=list(map(int,input("enter the number: ").split()))
dividend=int(input("enter the dividend: "))
print(ModArray(array,dividend))