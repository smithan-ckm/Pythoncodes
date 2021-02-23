# Given an array containing None values fill in the None values with most recent 
array1 = [1,None,2,3,None,None,5,None]

def s(array):
    next = 0            
    res = []                 
    for i in array: 
        if i is not None:    
            res.append(i)
            next = i
        else:
            res.append(next)
    return res

print(s(array1))
