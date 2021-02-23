array1 = [0,1,0,3,12]
array2 = [1,7,0,0,8,0,10,12,0,4]

def solution(array):
    for i in array:
        if i==0:
            array.remove(0)
            array.append(0)
    return array

print(solution(array1))
print(solution(array2))
