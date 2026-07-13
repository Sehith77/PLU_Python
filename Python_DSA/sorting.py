

var = [2, 100, 9, 105, 10, 20, 13, 36, 55, 42]


def search(var, element):
    sorted_var = var.sort()
    mid_index = len(sorted_var)//2
    if sorted_var[mid_index] < element:
        search(sorted_var[mid_index :], element)
        elif sorted_Var[mid_index] > element
        
    
    
    