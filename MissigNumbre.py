def missing_number(FirstList,SecondList):

    difference= set(FirstList) ^ set(SecondList)

    if FirstList ==[] and SecondList==[]:
        return 0
    elif len(FirstList) == len(SecondList): 
        return 0
    else:
        return (list(difference)[0])

print(missing_number([1,3,6,7], [1,2,3,6,7]))