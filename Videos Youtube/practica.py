def get_missing_element(seq): 
    for i in range(10):
        if i not in seq:
            return i

print(get_missing_element([9,2,4,5,7,0,8,6,1]))