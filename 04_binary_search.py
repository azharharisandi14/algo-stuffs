def create_array(size=10, max=50):
    from random import randint
    return [randint(0, max) for _ in range(size)]

def merge(a, b):
    c = []
    a_idx, b_idx = 0, 0
    while a_idx < len(a) and b_idx < len(b):
        if a[a_idx] < b[b_idx]:
            c.append(a[a_idx])
            a_idx += 1
        else:
            c.append(b[b_idx])
            b_idx += 1
            
    if a_idx == len(a): c.extend(b[b_idx:])
    else: c.extend(a[a_idx:])

    return c

def merge_sort(a):

    # a list of zero or one elements is sorted
    if len(a) <= 1: return a

    # split the list
    left, right = merge_sort(a[:len(a)//2]), merge_sort(a[len(a)//2:])
    
    # merge the now-sorted sublists
    return merge(left, right)

def binary_search(a, n):
    """

    :params a: array
    :params n: element to search
    
    """
    mid = len(a)//2
    
    if len(a) == 1:
        if a[mid] == n:
            return mid
        else:
            return None
        
    elif a[mid] ==  n:
        return mid
    
    else:
        if a[mid] < n:
            response = binary_search(a[mid:], n)
            return mid + response if response is not None else None

        else:
            return binary_search(a[:mid], n)


if __name__ == "__main__":
    a = create_array(size=100)
    a = merge_sort(a)
    # a = [1, 2, 3, 4, 5]
    print(f'Sorted array : {a}')
    
    n = 8
    print(f'Find index of element {n} in the array!')
    index = binary_search(a, n)
    print(f'Element {n} is in index {index} of array {a}')
